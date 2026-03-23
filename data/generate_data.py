import numpy as np
import pandas as pd
import os

def generate_data(n_safe=1000, n_hotspot=100):

    safe = np.random.normal([50, 50, 0, 0], [5, 5, 10, 10], (n_safe, 4))
    hotspot = np.random.normal([30, 20, 0, 0], [5, 5, 10, 10], (n_hotspot, 4))

    X = np.vstack([safe, hotspot])
    y = np.hstack([np.zeros(n_safe), np.ones(n_hotspot)])

    df = pd.DataFrame(X, columns=["width", "spacing", "x_coord", "y_coord"])
    df["label"] = y

    return df

if __name__ == "__main__":
    df = generate_data()
    df.to_csv("data/dataset.csv", index=False)
    print("Dataset saved")