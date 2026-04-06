import pandas as pd

# Load once (like DB)
df = pd.read_csv("data/raw/fraud_users_dataset.csv")


def get_user_features(user_id: str):
    user = df[df["user_id"] == user_id]

    if user.empty:
        return None

    return user.iloc[0].to_dict()