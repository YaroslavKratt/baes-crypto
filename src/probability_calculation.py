from collections import defaultdict
from src.csv.csv_service import CSVService


class ProbabilityCalculationService:

  # P(C)
  @staticmethod
  def calculate_cypher_text_probabilities(open_texts_probabilities, keys_probabilities, cypher_table):
    cypher_text_to_probability = defaultdict(float)

    for i, key_prob in enumerate(keys_probabilities):
      for j, open_prob in enumerate(open_texts_probabilities):
        cypher_text = cypher_table[i][j]
        cypher_text_to_probability[cypher_text] += open_prob * key_prob

    return dict(cypher_text_to_probability)

  # P(M, C)
  @staticmethod
  def calculate_open_text_encrypted_to_cypher_text_probabilities(open_texts_probabilities, keys_probabilities, cypher_table):
    cypher_text_to_open_texts_and_keys = ProbabilityCalculationService.get_cypher_text_to_open_texts_and_keys(cypher_table)

    open_text_encrypted_to_cypher_text_probabilities = {}

    for open_text_index in range(len(open_texts_probabilities)):
      for cypher_text, key_open_text_pairs in cypher_text_to_open_texts_and_keys.items():
        probability = sum(
          keys_probabilities[key_index] * open_texts_probabilities[open_text_index]
          for key_index, open_text_idx in key_open_text_pairs
          if open_text_idx == open_text_index
        )
        open_text_encrypted_to_cypher_text_probabilities[(open_text_index, cypher_text)] = probability

    return open_text_encrypted_to_cypher_text_probabilities

  # P(M/C)
  @staticmethod
  def calculate_open_text_dependent_on_cypher_text_probability(cypher_text_probabilities, open_text_encrypted_to_cypher_text_probabilities):
    open_text_dependent_on_cypher_text_probabilities = {}

    for (open_text, cypher_text), mc_prob in open_text_encrypted_to_cypher_text_probabilities.items():
      probability = mc_prob / cypher_text_probabilities.get(cypher_text, 1)
      open_text_dependent_on_cypher_text_probabilities[(open_text, cypher_text)] = probability

    return open_text_dependent_on_cypher_text_probabilities

  @staticmethod
  def get_cypher_text_to_open_texts_and_keys(cypher_table):
    cypher_text_to_open_texts_and_keys = defaultdict(list)

    for i, row in enumerate(cypher_table):
      for j, cypher_text in enumerate(row):
        cypher_text_to_open_texts_and_keys[cypher_text].append((i, j))

    return cypher_text_to_open_texts_and_keys