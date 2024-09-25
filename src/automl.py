import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Load the dataset
data = pd.read_csv('D:/traffic_monitoring_system/data/traffic_data.csv')  # Adjust the path as necessary

# Check the columns in the DataFrame
print("Columns in the dataset:", data.columns)

# Define features and target variable
X = data[['average_speed', 'location', 'time_of_day']]  # Features
y = data['vehicle_count']  # Target variable

# Convert categorical features to numeric (using one-hot encoding for 'location' and 'time_of_day')
X = pd.get_dummies(X, columns=['location', 'time_of_day'], drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'Decision Tree': DecisionTreeRegressor(),
    'Random Forest': RandomForestRegressor(),
    'XGBoost': XGBRegressor()
}

# Train models and evaluate performance
for model_name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    
    # Calculate MSE and RMSE
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    
    print(f"{model_name} MSE: {mse:.2f}")
    print(f"{model_name} RMSE: {rmse:.2f}")
