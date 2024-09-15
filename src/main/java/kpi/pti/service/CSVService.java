package kpi.pti.service;

import java.util.Arrays;
import java.util.List;
import kpi.pti.utils.CSVReaderUtil;

public class CSVService {

  public static List<Double> getOpenTextsProbabilities() {
    return CSVReaderUtil.readAllProbabilities()
        .map(List::getFirst)
        .map(strings -> Arrays.stream(strings).map(Double::parseDouble).toList())
        .orElseThrow(
            () -> new RuntimeException("Failed to read texts probabilities from CSV file"));
  }

  public static List<Double> getKeysProbabilities() {
    return CSVReaderUtil.readAllProbabilities()
        .map(List::getLast)
        .map(strings -> Arrays.stream(strings).map(Double::parseDouble).toList())
        .orElseThrow(() -> new RuntimeException("Failed to read keys probabilities from CSV file"));
  }
}
