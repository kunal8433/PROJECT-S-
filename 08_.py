# Student Marks Prediction
# Linear Regression WITHOUT scikit-learn

import numpy as np
import matplotlib.pyplot as plt

# 1. Dataset
hours = np.array([1,2,3,4,5,6,7,8,9,10])
marks = np.array([20,30,35,40,50,55,65,70,85,95])

# 2. Mean
x_mean = np.mean(hours)
y_mean = np.mean(marks)

# 3. Calculate slope (m)
numerator = 0
denominator = 0

for i in range(len(hours)):
    numerator += (hours[i] - x_mean) * (marks[i] - y_mean)
    denominator += (hours[i] - x_mean) ** 2

m = numerator / denominator

# 4. Calculate intercept (c)
c = y_mean - m * x_mean

print("Slope (m):", m)
print("Intercept (c):", c)

# 5. Prediction function
def predict(x):
    return m * x + c

# 6. User input
study_hours = float(input("Enter study hours: "))
predicted_marks = predict(study_hours)

print("Predicted Marks:", predicted_marks)

# 7. Visualization
plt.scatter(hours, marks)
plt.plot(hours, predict(hours), linestyle='--')
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Marks Prediction (No scikit-learn)")
plt.show()
