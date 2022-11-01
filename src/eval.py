"""
Check Score procedure
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import load
import src.ml.data
import src.ml.model
import logging


def eval_score():
    """
    Execute score checking
    """
    df = pd.read_csv("data/prepared/census.csv")
    _, test = train_test_split(df, test_size=0.20)

    trained_model = load("data/model_data/model.joblib")
    encoder = load("data/model_data/encoder.joblib")
    lb = load("data/model_data/lb.joblib")

    sliced_values = []

    for cat in src.ml.data.get_cat_features():
        for cls in test[cat].unique():
            df_temp = test[test[cat] == cls]

            X_test, y_test, _, _ = src.ml.data.process_data(
                df_temp,
                categorical_features=src.ml.data.get_cat_features(),
                label="salary", encoder=encoder, lb=lb, training=False)

            y_preds = trained_model.predict(X_test)

            prc, rcl, fb = src.ml.model.compute_model_metrics(y_test,
                                                                      y_preds)

            line = "[%s->%s] Precision: %s " \
                   "Recall: %s FBeta: %s" % (cat, cls, prc, rcl, fb)
            logging.info(line)
            sliced_values.append(line)

    with open('data/model_data/slicedoutput.txt', 'w') as out:
        for value in sliced_values:
            out.write(value + '\n')
    
    X_test, y_test, _, _ = src.ml.data.process_data(
    test,categorical_features=src.ml.data.get_cat_features(),label="salary", encoder=encoder, lb=lb, training=False)
    y_preds = trained_model.predict(X_test)
    acracy=src.ml.model.classification_metrics(y_test,y_preds)
    print(f"Accuracy of whole test model is:{acracy}")