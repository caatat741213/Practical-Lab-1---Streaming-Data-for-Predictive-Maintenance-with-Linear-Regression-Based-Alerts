
## This file is specifically used for calculating scores and drawing diagrams.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(y_true, y_pred, label="Model"):

    # Evaluate and print metrics

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    
    print(f"[{label}] RMSE: {rmse:.4f}")
    print(f"[{label}] R2 Score: {r2:.4f}")
    return {"rmse": rmse, "r2": r2}

def plot_regression_results(X_scaled, y_true, y_pred, title="Regression Result"):

    #Plot regression fitting

    plt.figure(figsize=(10, 6))
    plt.scatter(X_scaled, y_true, color='blue', alpha=0.1, label='Actual Data')
    plt.plot(X_scaled, y_pred, color='red', linewidth=3, label='Regression Line')
    plt.title(title)
    plt.legend()
    plt.show()