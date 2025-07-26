# Trained Models

This directory contains the trained machine learning models for the Smart Greenhouse Automation system.

## Model Files

### Random Forest Models
- `rf_greenhouse_model.pkl`: Main Random Forest multi-output classifier
- `rf_fan_model.onnx`: ONNX-converted Random Forest model for fan control

### XGBoost Models
- `xgb_greenhouse_model.pkl`: Main XGBoost multi-output classifier
- `xgb_fan_model.onnx`: ONNX-converted XGBoost model for fan control

## Model Details

### Random Forest Model
- Type: Multi-output Random Forest Classifier
- Features: temperature, humidity, water_level, N, P, K
- Outputs: Fan control, Water pump control
- Parameters:
  - n_estimators: 100
  - random_state: 42

### XGBoost Model
- Type: Multi-output XGBoost Classifier
- Features: temperature, humidity, water_level, N, P, K
- Outputs: Fan control, Water pump control
- Parameters:
  - n_estimators: 100
  - max_depth: 5
  - learning_rate: 0.1

## Downloading Models

You can download the trained models from the project's releases page. After downloading:

1. Place the `.pkl` and `.onnx` files in this directory
2. Ensure the filenames match exactly as listed above
3. The system will automatically use these models for predictions

Note: Models are periodically retrained with new data. Check the releases page for the latest versions.
