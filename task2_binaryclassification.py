import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score, average_precision_score
from sklearn.preprocessing import LabelEncoder

# Load the data from both CSV files
df1= pd.read_csv(r"C:\Users\Dell\Desktop\bmw-tasks\table_1.csv", encoding= "utf-8", delimiter= ";")
df2= pd.read_csv(r"C:\Users\Dell\Desktop\bmw-tasks\table_2.csv", encoding= "utf-8", delimiter= ";")

# Merge the two tables on 'ID'
merged_data = pd.merge(df1, df2, on='ID')

# Handle missing values
merged_data = merged_data.apply(lambda x: x.fillna(x.mean()) if x.dtype in ['float64', 'int64'] else x.fillna(x.mode()[0]))

# Encode the categorical columns 
label_encoder = LabelEncoder()

for col in merged_data.columns:
    merged_data[col] = label_encoder.fit_transform(merged_data[col].astype(str))

# Encode 'Type' column as binary: 'y' = 1, 'n' = 0
merged_data['Type'] = merged_data['Type'].replace({'y': 1, 'n': 0})
merged_data = merged_data[merged_data['Type'].isin([0, 1])]
merged_data = merged_data.dropna(subset=['Type'])

# Select features (X) and target (y)
X = merged_data.drop(columns=['ID', 'Type'])  
y = merged_data['Type']

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nPrecision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))