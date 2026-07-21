import joblib
import pandas as pd


class DriverRiskModel:

    def __init__(
        self,
        model_path="src/ml/models/driver_risk_model.pkl"
    ):

        self.model = joblib.load(
            model_path
        )

    # =======================================

    def predict(self, result):

        features = pd.DataFrame([{

            "ear": result.ear,

            "mar": result.mar,

            "pitch": result.pitch,

            "yaw": result.yaw,

            "roll": result.roll,

            "blink_count": result.blink_count,

            "yawn_count": result.yawn_count

        }])

        prediction = self.model.predict(
            features
        )[0]

        probabilities = self.model.predict_proba(
            features
        )[0]

        confidence = max(
            probabilities
        )

        return prediction, confidence