package kpi.pti.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.IntStream;
import org.apache.commons.lang3.tuple.Pair;

public class ProbabilityCalculationService {

  public Double calculateCypherTextProbabilities(
      Double[] openTextsProbabilities, Double[] keysProbabilities) {

    return IntStream.range(0, openTextsProbabilities.length)
        .mapToDouble(i -> openTextsProbabilities[i] * keysProbabilities[i])
        .sum();
  }

  public Map<Pair<Integer, Integer>, Double> calculateOpenTextEncryptedToCypherTextProbabilities(
      Double[] openTextsProbabilities, Double[] keysProbabilities, Integer[][] cypherTable) {
    Map<Integer, List<Pair<Integer, Integer>>> cypherTextToOpenTextsAndKeys = getCypherTextToOpenTextsAndKeys(
        cypherTable);

    Map<Pair<Integer, Integer>, Double> openTextEncryptedToCypherTextProbabilities =
        new HashMap<>();
    for (int i = 0; i < cypherTable.length; i++) {
      var openTextIndex = i;
      cypherTextToOpenTextsAndKeys.forEach(
          (cyperText, keyIndexAndOpenTextIndexes) -> {
            var probability =
                keyIndexAndOpenTextIndexes.stream()
                    .filter(
                        keyIndexAndOpenTextIndex ->
                            keyIndexAndOpenTextIndex.getRight().equals(openTextIndex))
                    .map(
                        keyIndexAndOpenTextIndex -> {
                          System.out.printf(
                              "key probability %s \n",
                              keysProbabilities[keyIndexAndOpenTextIndex.getLeft()]);
                          System.out.printf(
                              "open text probability %s\n",
                              openTextsProbabilities[keyIndexAndOpenTextIndex.getRight()]);
                          System.out.printf(
                              "P*K %s\n",
                              keysProbabilities[keyIndexAndOpenTextIndex.getLeft()]
                                  * openTextsProbabilities[keyIndexAndOpenTextIndex.getRight()]);
                          return keysProbabilities[keyIndexAndOpenTextIndex.getLeft()]
                              * openTextsProbabilities[keyIndexAndOpenTextIndex.getRight()];
                        })
                    .mapToDouble(Double::doubleValue)
                    .sum();
            System.out.printf(
                "Result openTIndex %s,cypherText %s, probability %s \n",
                openTextIndex, cyperText.toString(), probability);
            System.out.println("++++++++++");
            openTextEncryptedToCypherTextProbabilities.put(
                Pair.of(openTextIndex, cyperText), probability);
          });
    }

    return openTextEncryptedToCypherTextProbabilities;
  }

  private static Map<Integer, List<Pair<Integer, Integer>>> getCypherTextToOpenTextsAndKeys(
      Integer[][] cypherTable) {
    Map<Integer, List<Pair<Integer, Integer>>> cypherTextToOpenTextsAndKeys = new HashMap<>();

    for (int i = 0; i < cypherTable.length; i++) {
      for (int j = 0; j < cypherTable[i].length; j++) {
        int cypherText = cypherTable[i][j];
        int keyIndex = i;
        int openTextIndex = j;

        cypherTextToOpenTextsAndKeys.compute(
            cypherText,
            (key, value) -> {
              if (value == null) {
                value = new ArrayList<>();
              }
              value.add(Pair.of(keyIndex, openTextIndex));
              return value;
            });
      }
    }
    return cypherTextToOpenTextsAndKeys;
  }
}