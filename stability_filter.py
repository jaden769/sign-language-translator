def filter_stable_predictions(predictions, required_matches=3):
    accepted = []
    candidate = None
    match_count = 0
    last_accepted = None

    for prediction in predictions:
        if prediction is None:
            candidate = None
            match_count = 0
            last_accepted = None
        elif prediction == candidate:
            match_count += 1
        else:
            candidate = prediction
            match_count = 1
        if match_count == required_matches and candidate != last_accepted:
            accepted.append(candidate)
            last_accepted = candidate

    return accepted

if __name__ == "__main__":
    predictions = [
        "A", "A", "A", "B", "A", "A", "A"
    ]

    result = filter_stable_predictions(predictions)

    print(result)