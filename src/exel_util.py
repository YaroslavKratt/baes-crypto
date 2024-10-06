from datetime import datetime

import pandas as pd


class ExcelUtil:
  @staticmethod
  def write_stochastic_matrix_to_excel(probabilities_dict):
    cypher_texts = sorted(
      set(cypher_text for _, cypher_text in probabilities_dict.keys()))
    open_texts = sorted(
      set(open_text for open_text, _ in probabilities_dict.keys()))

    df = pd.DataFrame(index=cypher_texts, columns=open_texts)

    for (open_text, cypher_text), probability in probabilities_dict.items():
      df.loc[cypher_text, open_text] = probability

    df.to_excel("stochastic_matrix" + datetime.now().strftime(
      "%Y-%m-%d %H:%M:%S") + ".xlsx",
                index_label="Cypher Text")