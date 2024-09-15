package kpi.pti;

import kpi.pti.service.CSVService;
import kpi.pti.service.ProbabilityCalculationService;

public class App {

  public static void main(String[] args) {
    try {
      var probabilityCalculationService = new ProbabilityCalculationService();
      probabilityCalculationService.calculateKeyAndOpenTextProbabilities(
          CSVService.getOpenTextsProbabilities(), CSVService.getKeysProbabilities());
    } catch (Exception e) {
      System.out.printf("Something went wrong: %s\n", e.getMessage());
    }
  }
}
