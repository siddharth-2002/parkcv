import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import json

# Dummy data for demonstration
data = {
    'hour': np.arange(24),
    'spaces': np.random.randint(10, 50, size=24)
}

df = pd.DataFrame(data)
X = df[['hour']]
y = df['spaces']

# Train linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict for the next 24 hours
future_hours = np.arange(24, 48).reshape(-1, 1)
forecast = model.predict(future_hours)

result = {'forecast': list(forecast)}
print(json.dumps(result))
