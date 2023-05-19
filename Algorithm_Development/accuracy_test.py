
actual_mapping = {"a": "q", "b": "w", "c": "e", "d": "r", "e": "t", "f": "y", "g": "u", "h": "i", "i": "o",
                      "j": "p",
                      "k": "a", "l": "s", "m": "d", "n": "f", "o": "g", "p": "h", "q": "j", "r": "k", "s": "l",
                      "t": "z",
                      "u": "x", "v": "c", "w": "v", "x": "b", "y": "n", "z": "m"}
actual_mapping = {v: k for k, v in actual_mapping.items()}


def test_accuracy_with_custom_mapping(calculated_mapping, actual_mapping, show_output=False):
    total_correct = 0
    for key, value in calculated_mapping.items():
        if show_output:
            print(f"Calculated Mapping Letter: {calculated_mapping[value]}. "
                  f"Actual Mapping Letter: {actual_mapping[value]}")
        if calculated_mapping[value] == actual_mapping[value]:
            total_correct += 1
    return total_correct


def test_accuracy(calculated_mapping, show_output=False):
    total_correct = 0
    for key, value in calculated_mapping.items():
        if show_output:
            print(f"Calculated Mapping Letter: {calculated_mapping[value]}. Actual Mapping Letter: {actual_mapping[value]}")
        if calculated_mapping[value] == actual_mapping[value]:
            total_correct += 1
    return total_correct