package kpi.pti.utils;

import com.opencsv.CSVReader;
import java.io.Reader;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Optional;

public class CSVReaderUtil {
  private static final String PROB_PATH = "prob_11.csv";
  private static final String TABLE_PATH = "table_11.csv";

  public static Optional<List<String[]>> readAllProbabilities() {
    try {
      return Optional.of(readAllLines(getPathFromFileName(PROB_PATH)));
    } catch (Exception e) {
      System.out.printf(
          "Something went wrong while reading probabilities from file: %s\n", e.getMessage());
    }
    return Optional.empty();
  }

  private static List<String[]> readAllLines(Path filePath) throws Exception {
    try (Reader reader = Files.newBufferedReader(filePath)) {
      try (CSVReader csvReader = new CSVReader(reader)) {
        return csvReader.readAll();
      }
    }
  }

  private static Path getPathFromFileName(String fileName) throws URISyntaxException {
    return Paths.get(ClassLoader.getSystemResource(PROB_PATH).toURI());
  }
}
