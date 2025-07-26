from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import joblib
import pandas as pd

def convert_to_onnx(model_path: str, output_path: str, input_shape: int):
    """Convert a trained sklearn model to ONNX format."""
    # Load the model
    model = joblib.load(model_path)
    
    # Get the first target model (fan)
    single_model = model.estimators_[0]
    
    # Define input type
    initial_type = [('float_input', FloatTensorType([None, input_shape]))]
    
    # Convert to ONNX
    onnx_model = convert_sklearn(single_model, initial_types=initial_type)
    
    # Save the model
    with open(output_path, "wb") as f:
        f.write(onnx_model.SerializeToString())

def main():
    # Load sample data to get input shape
    df = pd.read_csv('data/IoTProcessed_Data.csv')
    df = df.drop(columns=['date', 'Fan_actuator_OFF', 'Watering_plant_pump_OFF', 
                         'Water_pump_actuator_OFF', 'Water_pump_actuator_ON',
                         'Fan_actuator_ON', 'Watering_plant_pump_ON'])
    input_shape = df.shape[1]
    
    # Convert Random Forest model
    print("Converting Random Forest model to ONNX format...")
    convert_to_onnx('models/rf_greenhouse_model.pkl', 'models/rf_fan_model.onnx', input_shape)
    
    # Convert XGBoost model
    print("Converting XGBoost model to ONNX format...")
    convert_to_onnx('models/xgb_greenhouse_model.pkl', 'models/xgb_fan_model.onnx', input_shape)
    
    print("✅ Models converted to ONNX format successfully")

if __name__ == "__main__":
    main()
