package kpi.pti.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.apache.commons.lang3.tuple.Pair;

public class ProbabilityCalculationService {

  public Map<Integer, Double> calculateCypherTextProbabilities(
      Double[] openTextsProbabilities, Double[] keysProbabilities, Integer[][] cypherTable) {
    Map<Integer, Double> cypherTexToProbability = new HashMap<>();
    for (int i = 0; i < keysProbabilities.length; i++) {
      for (int j = 0; j < openTextsProbabilities.length; j++) {
        var keysIndex = i;
        var openTextsIndex = j;
        cypherTexToProbability.compute(
            cypherTable[i][j],
            (key, probability) -> {
              if (probability == null) {
                probability = openTextsProbabilities[openTextsIndex] * keysProbabilities[keysIndex];
              } else {
                probability +=
                    openTextsProbabilities[openTextsIndex] * keysProbabilities[keysIndex];
              }

              return probability;
            });
      }
    }
    return cypherTexToProbability;
  }

  public Map<Pair<Integer, Integer>, Double> calculateOpenTextEncryptedToCypherTextProbabilities(
      Double[] openTextsProbabilities, Double[] keysProbabilities, Integer[][] cypherTable) {
    Map<Integer, List<Pair<Integer, Integer>>> cypherTextToOpenTextsAndKeys =
        getCypherTextToOpenTextsAndKeys(cypherTable);

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
                        keyIndexAndOpenTextIndex ->
                            keysProbabilities[keyIndexAndOpenTextIndex.getLeft()]
                                * openTextsProbabilities[keyIndexAndOpenTextIndex.getRight()])
                    .mapToDouble(Double::doubleValue)
                    .sum();
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
