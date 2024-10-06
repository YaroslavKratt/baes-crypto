from collections import defaultdict


class ProbabilityCalculationService:

    # P(C)
    @staticmethod
    def calculate_cypher_text_probabilities(
        open_texts_probabilities, keys_probabilities, cypher_table
    ):
        cypher_text_to_probability = defaultdict(float)

        for i, key_prob in enumerate(keys_probabilities):
            for j, open_prob in enumerate(open_texts_probabilities):
                cypher_text = cypher_table[i][j]
                cypher_text_to_probability[cypher_text] += open_prob * key_prob

        return dict(cypher_text_to_probability)

    # P(M,C)
    @staticmethod
    def calculate_open_text_encrypted_to_cypher_text_probabilities(
        open_texts_probabilities, keys_probabilities, cypher_table
    ):
        cypher_text_to_open_texts_and_keys = (
            ProbabilityCalculationService.get_cypher_text_to_open_texts_and_keys(
                cypher_table
            )
        )

        open_text_encrypted_to_cypher_text_probabilities = {}

        for open_text_index in range(len(open_texts_probabilities)):
            for (
                cypher_text,
                key_open_text_pairs,
            ) in cypher_text_to_open_texts_and_keys.items():
                probability = sum(
                    keys_probabilities[key_index]
                    * open_texts_probabilities[open_text_index]
                    for key_index, open_text_idx in key_open_text_pairs
                    if open_text_idx == open_text_index
                )
                open_text_encrypted_to_cypher_text_probabilities[
                    (open_text_index, cypher_text)
                ] = probability

        return open_text_encrypted_to_cypher_text_probabilities

    @staticmethod
    def get_cypher_text_to_open_texts_and_keys(cypher_table):
        cypher_text_to_open_texts_and_keys = defaultdict(list)

        for i, row in enumerate(cypher_table):
            for j, cypher_text in enumerate(row):
                cypher_text_to_open_texts_and_keys[cypher_text].append((i, j))

        return cypher_text_to_open_texts_and_keys

    # P(M/C)
    @staticmethod
    def calculate_open_text_dependent_on_cypher_text_probability(
        cypher_text_probabilities, open_text_encrypted_to_cypher_text_probabilities
    ):
        open_text_dependent_on_cypher_text_probabilities = {}

        for (
            open_text,
            cypher_text,
        ), m_to_c_probability in (
            open_text_encrypted_to_cypher_text_probabilities.items()
        ):
            probability = m_to_c_probability / cypher_text_probabilities.get(
                cypher_text
            )
            open_text_dependent_on_cypher_text_probabilities[
                (open_text, cypher_text)
            ] = probability

        return open_text_dependent_on_cypher_text_probabilities

    @staticmethod
    def calculate_average_deterministic_loss(
        open_text_dependent_on_cypher_text_probabilities,
        open_text_encrypted_to_cypher_text_probabilities,
        open_texts,
        cypher_texts,
    ):
        total_loss = 0

        for cypher_text in cypher_texts:
            # Find the open text with the maximum P(M|C) for deterministic function
            max_prob_open_text = max(
                open_texts,
                key=lambda M: open_text_dependent_on_cypher_text_probabilities.get(
                    (M, cypher_text)
                ),
            )

            for open_text in open_texts:
                prob_m_c = open_text_encrypted_to_cypher_text_probabilities.get(
                    (open_text, cypher_text)
                )
                if open_text != max_prob_open_text:
                    total_loss += prob_m_c

        return total_loss

    @staticmethod
    def calculate_average_stochastic_loss(
        open_text_dependent_on_cypher_text_probabilities,
        open_text_encrypted_to_cypher_text_probabilities,
        open_texts,
        cypher_texts,
    ):
        total_loss = 0

        for cypher_text in cypher_texts:
            for open_text in open_texts:
                prob_m_c = open_text_encrypted_to_cypher_text_probabilities.get(
                    (open_text, cypher_text)
                )

                loss_for_m = 0
                for other_open_text in open_texts:
                    if other_open_text != open_text:
                        # L(M,C) = sum (P(M'|C))
                        loss_for_m += (
                            open_text_dependent_on_cypher_text_probabilities.get(
                                (other_open_text, cypher_text)
                            )
                        )
                # P(M,C) * L(M,C)
                total_loss += prob_m_c * loss_for_m

        return total_loss
