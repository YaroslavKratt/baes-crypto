package kpi.pti;

import kpi.pti.service.CSVService;

public class App {

  public static void main(String[] args) {
    try {
      CSVService.getKeysProbabilities();
      CSVService.getOpenTextsProbabilities();
    } catch (Exception e) {
      System.out.printf("Something went wrong: %s\n", e.getMessage());
    }
  }
}
