def filter_predictions(predictions):
    accepted = []
    last_prediction = None

    for prediction in predictions:
        if prediction is None:
            last_prediction = None
        elif prediction != last_prediction:
            accepted.append(prediction)
            last_prediction = prediction
    
    return accepted

if __name__ == "__main__":
    predictions = ["C", "C", None, "A", "A"]
    result = filter_predictions(predictions)

    print(result)