import csv
from pathlib import Path


class CSVReaderUtil:
  PROB_PATH = "../test_data/prob_11.csv"
  TABLE_PATH = "../test_data/table_11.csv"

  @staticmethod
  def read_all_probabilities():
    return CSVReaderUtil.read_from_file(CSVReaderUtil.PROB_PATH)

  @staticmethod
  def read_all_table():
    return CSVReaderUtil.read_from_file(CSVReaderUtil.TABLE_PATH)

  @staticmethod
  def read_from_file(file_path):
    try:
      path = CSVReaderUtil.get_path_from_file_name(file_path)
      return CSVReaderUtil.read_all_lines(path)
    except Exception as e:
      print(f"Error reading file '{file_path}': {e}")
      return None

  @staticmethod
  def read_all_lines(file_path):
    with file_path.open(newline='', encoding='utf-8') as csvfile:
      csvreader = csv.reader(csvfile)
      return list(csvreader)

  @staticmethod
  def get_path_from_file_name(file_name):
    return Path(__file__).parent / file_name