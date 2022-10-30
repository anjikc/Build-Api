# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
import pandas as pd
from joblib import dump
import src.ml.data
import src.ml.model

# Add code to load in the data.

# Optional enhancement, use K-fold cross validation instead of a train-test split.

# Proces the test data with the process_data function.

# Train and save a model.




def train_test_model():
    """
    Execute model training
    """
    df = pd.read_csv("data/prepared/census.csv")
    train, _ = train_test_split(df, test_size=0.20)

    X_train, y_train, encoder, lb = src.ml.data.process_data(
        train, categorical_features=src.ml.data.get_cat_features(),
        label="salary", training=True
    )
    trained_model = src.ml.model.train_model(X_train, y_train)

    dump(trained_model, "data/model_data/model.joblib")
    dump(encoder, "data/model_data/encoder.joblib")
    dump(lb, "data/model_data/lb.joblib")
