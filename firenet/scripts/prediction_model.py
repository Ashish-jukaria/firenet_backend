import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load your dataset
# Replace 'your_data.csv' with the actual path to your CSV file
data = pd.read_csv('your_data.csv')

# Prepare features and target variable
X = data[['temperature', 'humidity']]  # Adjust column names if needed
y = data['fire']  # Assuming 'fire' is your target variable indicating fire status

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the decision tree classifier
clf = DecisionTreeClassifier()

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model to a .pkl file
model_path = '/home/ashish/FInal_Year_Project_Backend/Firenet_backend/firenet/scripts/trained_model3.pkl'
joblib.dump(clf, model_path)
print(f"Model saved to {model_path}")
