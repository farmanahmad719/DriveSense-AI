import os

import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import joblib


# ============================================
# PATHS
# ============================================

DATA_PATH = "data/ml_features.csv"

MODEL_PATH = "src/ml/models/driver_risk_model.pkl"


# ============================================
# LOAD DATA
# ============================================

print("Loading dataset...")

data = pd.read_csv(
    DATA_PATH
)


# ============================================
# ORIGINAL DISTRIBUTION
# ============================================

print(
    "\nOriginal Driver State Distribution:"
)

print(
    data["driver_state"].value_counts()
)


print(
    "\nOriginal Dataset Shape:",
    data.shape
)


## ============================================
# BALANCE DATASET
# ============================================

print(
    "\nBalancing dataset..."
)


min_count = (
    data["driver_state"]
    .value_counts()
    .min()
)


balanced_groups = []


for state in data["driver_state"].unique():

    state_data = data[
        data["driver_state"] == state
    ]

    sampled_data = state_data.sample(
        n=min_count,
        random_state=42
    )

    balanced_groups.append(
        sampled_data
    )


balanced_data = pd.concat(
    balanced_groups
)


balanced_data = balanced_data.sample(
    frac=1,
    random_state=42
).reset_index(
    drop=True
)


print(
    "\nBalanced Driver State Distribution:"
)

print(
    balanced_data[
        "driver_state"
    ].value_counts()
)


print(
    "\nBalanced Dataset Shape:",
    balanced_data.shape
)


# ============================================
# FEATURES
# ============================================

features = [

    "ear",

    "mar",

    "pitch",

    "yaw",

    "roll",

    "blink_count",

    "yawn_count"

]


X = balanced_data[features]


y = balanced_data["driver_state"]


# ============================================
# SPLIT DATA
# ============================================

X_train, X_test, y_train, y_test = (

    train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42,

        stratify=y

    )

)


# ============================================
# CREATE MODEL
# ============================================

model = RandomForestClassifier(

    n_estimators=100,

    random_state=42,

    class_weight="balanced"

)


# ============================================
# TRAIN
# ============================================

print(
    "\nTraining model..."
)


model.fit(

    X_train,

    y_train

)


# ============================================
# TEST
# ============================================

predictions = model.predict(

    X_test

)


accuracy = accuracy_score(

    y_test,

    predictions

)


print(

    f"\nAccuracy: {accuracy:.2f}"

)


print(

    "\nClassification Report:\n"

)


print(

    classification_report(

        y_test,

        predictions

    )

)


print(

    "\nConfusion Matrix:\n"

)


print(

    confusion_matrix(

        y_test,

        predictions

    )

)


# ============================================
# SAVE MODEL
# ============================================

os.makedirs(

    os.path.dirname(

        MODEL_PATH

    ),

    exist_ok=True

)


joblib.dump(

    model,

    MODEL_PATH

)


print(

    "\nModel saved to:",

    MODEL_PATH

)