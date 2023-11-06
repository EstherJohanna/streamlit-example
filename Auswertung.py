import streamlit as st
import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression

# Database setup
conn = sqlite3.connect('survey_results.db')
c = conn.cursor()

# Streamlit app to display the linear regression results
st.title("Linear Regression on Survey Data")

# Step 1: Retrieve Data
c.execute("SELECT answer1, answer2, answer3, answer4 FROM responses")
data = c.fetchall()

# Convert data to a pandas DataFrame
df = pd.DataFrame(data, columns=['answer1', 'answer2', 'answer3', 'answer4'])

# Close the connection to the database
conn.close()

# Step 2: Prepare Data for Regression
# Let's say 'answer4' is our dependent variable (y) and the rest are independent variables (X)
X = df[['answer1', 'answer2', 'answer3']]
y = df['answer4']

# Step 3: Perform Linear Regression
model = LinearRegression()
model.fit(X, y)

# Step 4: Analyze Results
# Display the coefficients
st.write("Coefficients:", model.coef_)

# Display the intercept
st.write("Intercept:", model.intercept_)

# You might also want to display R^2 to see how well your model performs
st.write("R^2:", model.score(X, y))

# Optionally, make predictions
# predictions = model.predict(X)
# st.write("Predictions:", predictions)
