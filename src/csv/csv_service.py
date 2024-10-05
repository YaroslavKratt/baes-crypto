from src.csv.csv_util import CSVReaderUtil


class CSVService:

  @staticmethod
  def get_open_texts_probabilities():
    data = CSVReaderUtil.read_all_probabilities()
    if data:
      try:
        return [float(x) for x in data[0]]
      except ValueError as e:
        raise RuntimeError(f"Failed to parse probabilities as floats: {e}")
    else:
      raise RuntimeError("Failed to read texts probabilities from CSV file")

  @staticmethod
  def get_keys_probabilities():
    data = CSVReaderUtil.read_all_probabilities()
    if data:
      try:
        return [float(x) for x in data[-1]]
      except ValueError as e:
        raise RuntimeError(f"Failed to parse probabilities as floats: {e}")
    else:
      raise RuntimeError("Failed to read keys probabilities from CSV file")

  @staticmethod
  def get_cypher_table():
    data = CSVReaderUtil.read_all_table()
    if data:
      try:
        return [[int(x) for x in row] for row in
                data]
      except ValueError as e:
        raise RuntimeError(f"Failed to parse table as integers: {e}")
    else:
      raise RuntimeError("Failed to read cipher table from CSV file")