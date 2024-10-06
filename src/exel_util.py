import pandas as pd


class ExcelUtil:
  @staticmethod
  def write_stochastic_matrix_to_excel(probabilities_dict,
      file_name="stochastic_matrix.xlsx"):
    # Extract unique cypher_texts and open_texts from the probabilities dictionary
    cypher_texts = sorted(
      set(cypher_text for _, cypher_text in probabilities_dict.keys()))
    open_texts = sorted(
      set(open_text for open_text, _ in probabilities_dict.keys()))

    # Create an empty DataFrame with Cypher Texts as rows and Open Texts as columns
    df = pd.DataFrame(index=cypher_texts, columns=open_texts)

    # Fill DataFrame with probabilities P(M|C)
    for (open_text, cypher_text), probability in probabilities_dict.items():
      df.loc[cypher_text, open_text] = probability

    # Write DataFrame to Excel
    df.to_excel(file_name, index_label="Cypher Text")