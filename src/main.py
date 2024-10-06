from src.csv.csv_service import CSVService
from src.exel_util import ExcelUtil
from src.probability_calculation import ProbabilityCalculationService


def main():
    keys_probabilities = CSVService.get_keys_probabilities()
    print("Keys Probabilities:")
    print(keys_probabilities)

    open_text_probabilities = CSVService.get_open_texts_probabilities()
    print("Open Text Probabilities:")
    print(open_text_probabilities)

    cypher_table = CSVService.get_cypher_table()
    print("Cypher Table:")
    for row in cypher_table:
        print(row)

    cypher_text_probabilities = (
        ProbabilityCalculationService.calculate_cypher_text_probabilities(
            open_text_probabilities, keys_probabilities, cypher_table
        )
    )
    # print("##################### P(C):\n")
    # for cypher_text, probability in cypher_text_probabilities.items():
    #   print(f"Cypher Text: {cypher_text}, Probability: {probability}")

    open_text_encrypted_to_cypher_text_probabilities = ProbabilityCalculationService.calculate_open_text_encrypted_to_cypher_text_probabilities(
        open_text_probabilities, keys_probabilities, cypher_table
    )
    # print("##################### P(M, C):\n")
    # for (open_text,
    #      cypher_text), probability in open_text_encrypted_to_cypher_text_probabilities.items():
    #   print(
    #     f"Open Text: {open_text}, Cypher Text: {cypher_text}, Probability: {probability}")

    open_text_dependent_on_cypher_text_probabilities = ProbabilityCalculationService.calculate_open_text_dependent_on_cypher_text_probability(
        cypher_text_probabilities, open_text_encrypted_to_cypher_text_probabilities
    )
    # print("##################### P(M|C):\n")
    # for (open_text,
    #      cypher_text), probability in open_text_dependent_on_cypher_text_probabilities.items():
    #   print(
    #     f"Open Text: {open_text}, Cypher Text: {cypher_text}, Probability: {probability}")

    ExcelUtil.write_stochastic_matrix_to_excel(
        open_text_dependent_on_cypher_text_probabilities
    )

    deterministic_loss = (
        ProbabilityCalculationService.calculate_average_deterministic_loss(
            open_text_dependent_on_cypher_text_probabilities,
            open_text_encrypted_to_cypher_text_probabilities,
            list(range(20)),
            list(range(20)),
        )
    )
    print(f"Deterministic loss:{deterministic_loss}")

    stochastic_loss = ProbabilityCalculationService.calculate_average_stochastic_loss(
        open_text_dependent_on_cypher_text_probabilities,
        open_text_encrypted_to_cypher_text_probabilities,
        list(range(20)),
        list(range(20)),
    )
    print(f"Stochastic loss:{stochastic_loss}")


if __name__ == "__main__":
    main()
