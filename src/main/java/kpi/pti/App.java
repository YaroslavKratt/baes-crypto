package kpi.pti;

import kpi.pti.service.CSVService;
import kpi.pti.service.ProbabilityCalculationService;

public class App {

  public static void main(String[] args) {
    try {
      var probabilityCalculationService = new ProbabilityCalculationService();

      probabilityCalculationService.calculateOpenTextEncryptedToCypherTextProbabilities(
          CSVService.getOpenTextsProbabilities(),
          CSVService.getKeysProbabilities(),
          CSVService.getCypherTable());

      probabilityCalculationService.calculateCypherTextProbabilities(
          CSVService.getOpenTextsProbabilities(),
          CSVService.getKeysProbabilities(),
          CSVService.getCypherTable());
    } catch (Exception e) {
      System.out.printf("Something went wrong: %s\n", e.getMessage());
      System.out.printf("Exception: %s\n", e);
    }
  }
}
