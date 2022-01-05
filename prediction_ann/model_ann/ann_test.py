import torch
import matplotlib as plt
from sklearn.metrics import accuracy_score

def test_predictions(model, X_test):
    predictions=[]
    with torch.no_grad():
        for i,data in enumerate(X_test):
            y_pred=model(data)
            predictions.append(y_pred.argmax().item())
    return predictions

# Confusion Matrix
def con_matrix(y_test, predictions):
    cm = confusion_matrix(y_test,predictions)
    plt.pyplot.figure(figsize=(10,6))
    sns.heatmap(cm,annot=True)
    plt.pyplot.xlabel('Actual Values')
    plt.pyplot.ylabel('Predicted Values')
    plt.pyplot.show()

def acc_score(y_test, predictions):
    return accuracy_score(y_test,predictions)
