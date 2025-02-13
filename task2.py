def typeBasedTransformer(**yoyo):
    transformed_dict = {}

    for key, value in yoyo.items():
        if isinstance(value, int):
            transformed_dict[key] = value ** 2
        elif isinstance(value, str):
            transformed_dict[key] = value[::-1]
        elif isinstance(value, float):
            transformed_dict[key] = value ** 2
        elif isinstance(value, bool):
            transformed_dict[key] = not value
        elif isinstance(value, list):
            transformed_dict[key] = type(value)(value[::-1])
        elif isinstance(value, tuple):
            transformed_dict[key] = type(value)(value[::-1])
        elif isinstance(value, dict):
            transformed_dict[key] = {v: k for k, v in value.items()}
        else:
            return None

    return transformed_dict
