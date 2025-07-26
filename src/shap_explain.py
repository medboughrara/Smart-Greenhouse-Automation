import shap
import matplotlib.pyplot as plt
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    """Load and preprocess the dataset."""
    df = pd.read_csv('data/IoTProcessed_Data.csv')
    
    # Preprocess
    df = df.drop(columns=['date', 'Fan_actuator_OFF', 'Watering_plant_pump_OFF', 
                         'Water_pump_actuator_OFF', 'Water_pump_actuator_ON'])
    
    # Features (X) and labels (y)
    X = df.drop(columns=['Fan_actuator_ON', 'Watering_plant_pump_ON'])
    y = df[['Fan_actuator_ON', 'Watering_plant_pump_ON']]
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

def explain_model(model_path, X_test, output_path):
    """Generate SHAP explanations for the model."""
    # Load model
    model = joblib.load(model_path)
    
    # Use the first classifier from MultiOutput (Fan_actuator_ON)
    explainer = shap.Explainer(model.estimators_[0])
    shap_values = explainer(X_test)
    
    # Create summary plot
    plt.figure(figsize=(10, 6))
    shap.summary_plot(shap_values, X_test)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    
    return shap_values

def main():
    # Load test data
    X_train, X_test, y_train, y_test = load_data()
    
    # Generate explanations for XGBoost model
    print("Generating SHAP explanations for XGBoost model...")
    xgb_shap = explain_model('models/xgb_greenhouse_model.pkl', X_test, 'models/xgb_shap_summary.png')
    
    # Generate explanations for Random Forest model
    print("Generating SHAP explanations for Random Forest model...")
    rf_shap = explain_model('models/rf_greenhouse_model.pkl', X_test, 'models/rf_shap_summary.png')
    
    print("\n✅ SHAP explanations generated and saved as PNG files")

if __name__ == "__main__":
    main()
