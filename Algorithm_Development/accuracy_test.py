actual_mapping = {"a": "k", "b": "x", "c": "v", "d": "m", "e": "c", "f": "y", "g": "o", "h": "p", "i": "h", "j": "q",
                            "k": "r", "l": "s", "m": "z", "n": "f", "o": "i", "p": "j", "q": "a", "r": "d", "s": "l", "t": "e",
                            "u": "g", "v": "w", "w": "b", "x": "u", "y": "n", "z": "t"}

def test_accuracy_with_custom_mapping(calculated_mapping, actual_mapping):
    total_correct = 0
    for key, value in calculated_mapping.items():
        print(f"Calculated Mapping Letter: {calculated_mapping[value]}. Actual Mapping Letter: {actual_mapping[value]}")
        if calculated_mapping[value] == actual_mapping[value]:
            total_correct += 1
    return total_correct


def test_accuracy(calculated_mapping):
    total_correct = 0
    for key, value in calculated_mapping.items():
        print(f"Calculated Mapping Letter: {calculated_mapping[value]}. Actual Mapping Letter: {actual_mapping[value]}")
        if calculated_mapping[value] == actual_mapping[value]:
            total_correct += 1
    return total_correct