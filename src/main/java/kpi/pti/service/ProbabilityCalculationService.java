package kpi.pti.service;

import java.util.stream.IntStream;

public class ProbabilityCalculationService {

  public Double[] calculateKeyAndOpenTextProbabilities(
      Double[] openTextsProbabilities, Double[] keysProbabilities) {

    return IntStream.range(0, openTextsProbabilities.length)
        .mapToObj(i -> openTextsProbabilities[i] * keysProbabilities[i])
        .toArray(Double[]::new);
  }
}
