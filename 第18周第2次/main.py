from src.model import train_and_get_model, ablation_scores, classify, predict_difficulty


def main():
    model, baseline, X, y = train_and_get_model()
    print("Baseline Accuracy:", baseline)
    print(model.coef_)
    scores = ablation_scores(X, y)
    for name, score in scores.items():
        print(f"Without {name}:", score)

    print(classify("add 5 and 9", model))
    print(classify("python loop example", model))
    print(predict_difficulty("explain python class"))

main()
