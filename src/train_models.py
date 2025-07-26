import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import joblib
import os

def load_and_preprocess_data(data_path):
    """Load and preprocess the dataset."""
    df = pd.read_csv(data_path)
    
    # Preprocess
    df = df.drop(columns=['date', 'Fan_actuator_OFF', 'Watering_plant_pump_OFF', 
                         'Water_pump_actuator_OFF', 'Water_pump_actuator_ON'])
    
    # Features (X) and labels (y)
    X = df.drop(columns=['Fan_actuator_ON', 'Watering_plant_pump_ON'])
    y = df[['Fan_actuator_ON', 'Watering_plant_pump_ON']]
    
    return X, y

def train_random_forest(X_train, X_test, y_train, y_test, model_path):
    """Train and evaluate Random Forest model."""
    print("\n🌲 Training Random Forest...")
    rf_model = MultiOutputClassifier(RandomForestClassifier(n_estimators=100, random_state=42))
    rf_model.fit(X_train, y_train)
    rf_preds = rf_model.predict(X_test)
    
    print("\n📊 Random Forest Performance:")
    print(classification_report(y_test, rf_preds, 
          target_names=['Fan_actuator_ON', 'Watering_plant_pump_ON']))
    
    # Save model
    joblib.dump(rf_model, model_path)
    return rf_model

def train_xgboost(X_train, X_test, y_train, y_test, model_path):
    """Train and evaluate XGBoost model."""
    print("\n🚀 Training XGBoost...")
    xgb_base = XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1,
                            use_label_encoder=False, eval_metric='logloss')
    xgb_model = MultiOutputClassifier(xgb_base)
    xgb_model.fit(X_train, y_train)
    xgb_preds = xgb_model.predict(X_test)
    
    print("\n📊 XGBoost Performance:")
    print(classification_report(y_test, xgb_preds,
          target_names=['Fan_actuator_ON', 'Watering_plant_pump_ON']))
    
    # Save model
    joblib.dump(xgb_model, model_path)
    return xgb_model

def main():
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Load and preprocess data
    X, y = load_and_preprocess_data('data/IoTProcessed_Data.csv')
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train and save models
    rf_model = train_random_forest(X_train, X_test, y_train, y_test, 'models/rf_greenhouse_model.pkl')
    xgb_model = train_xgboost(X_train, X_test, y_train, y_test, 'models/xgb_greenhouse_model.pkl')
    
    print("\n✅ Models saved in the 'models' directory")

if __name__ == "__main__":
    main()
