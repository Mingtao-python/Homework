from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def show_confusion_matrix_example():
    y_true = [1, 0, 1, 1, 0, 0, 1, 0]
    y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

    cm = confusion_matrix(y_true, y_pred)

    print("1. 模型评估")
    print(f"Accuracy={accuracy_score(y_true, y_pred):.2%}")
    print(f"Precision={precision_score(y_true, y_pred):.2%}")
    print(f"Recall={recall_score(y_true, y_pred):.2%}")
    print(f"F1={f1_score(y_true, y_pred):.2%}")
    print(f"Confusion Matrix=\n{cm}")
    print()


def imbalanced_data_experiment():
    print("2. 数据不平衡实验")
    true_labels = [0] * 90 + [1] * 10
    predict_labels = [0] * 95 + [1] * 5

    tp = sum(1 for t, p in zip(true_labels, predict_labels) if t == 1 and p == 1)
    tn = sum(1 for t, p in zip(true_labels, predict_labels) if t == 0 and p == 0)
    fp = sum(1 for t, p in zip(true_labels, predict_labels) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(true_labels, predict_labels) if t == 1 and p == 0)

    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0

    print(f"TP={tp}, TN={tn}, FP={fp}, FN={fn}")
    print(f"Accuracy={accuracy:.2%}")
    print(f"Precision={precision:.2%}")
    print(f"Recall={recall:.2%}")
    print()
