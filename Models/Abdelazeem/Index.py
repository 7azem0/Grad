import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Tire_Life": [5, 15, None, 22, 7, 18, 12, 25],
    "Tire_Temperature": [85, 105, 95, 110, 90, 108, 98, 115],
    "Pit_Stop": ["No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes"]
}

data_frame = pd.DataFrame(data)


data_frame.info()
print(data_frame.head())
print(data_frame.isnull().sum())


data_frame = data_frame.dropna()


x = data_frame["Tire_Life"]
y = data_frame["Tire_Temperature"]

beta_1, beta_0 = np.polyfit(x, y, 1)

print("Beta 0:", beta_0)
print("Beta 1:", beta_1)

y_pred = beta_0 + beta_1 * x

residuals = y - y_pred

rss = np.sum(residuals ** 2)
mse = np.mean(residuals ** 2)
rmse = np.sqrt(mse)

print("RSS:", rss)
print("MSE:", mse)
print("RMSE:", rmse)

plt.scatter(x, y)
plt.plot(x, y_pred)

plt.xlabel("Tire Life")
plt.ylabel("Tire Temperature")
plt.title("Linear Regression")


plt.savefig("tire_life_regression.png")
