from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([[85, 10], [60, 5], [78, 8]])  # [Feeling, Study Hours]
y = np.array([90, 65, 80])                 # Exam Scores

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction example
new_data = np.array([[75, 7]])
predicted_score = model.predict(new_data)
print(predicted_score)
