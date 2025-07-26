import pandas as pd
import joblib
import time
import os
from typing import Dict, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GreenhousePredictor:
    def __init__(self, model_path: str):
        """Initialize the predictor with a trained model."""
        self.model = self._load_model(model_path)
        logging.info(f"Loaded model from {model_path}")

    @staticmethod
    def _load_model(model_path: str):
        """Load the trained model from disk."""
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        return joblib.load(model_path)

    def predict(self, sensor_data: Dict[str, float]) -> Tuple[bool, bool]:
        """Make predictions based on sensor data."""
        try:
            # Convert to DataFrame for prediction
            df_input = pd.DataFrame([sensor_data])
            
            # Make prediction
            prediction = self.model.predict(df_input)
            
            # Extract predictions
            fan_on = bool(prediction[0][0])
            watering_on = bool(prediction[0][1])
            
            return fan_on, watering_on
            
        except Exception as e:
            logging.error(f"Error making prediction: {str(e)}")
            return False, False

def simulate_sensor_reading() -> Dict[str, float]:
    """Simulate reading from sensors. Replace with actual sensor interface."""
    return {
        'tempreature': 31,  # Corrected column name to match training data
        'humidity': 40,
        'water_level': 90,
        'N': 130,
        'P': 90,
        'K': 100
    }

def main():
    # Initialize predictor with Random Forest model (or XGBoost)
    predictor = GreenhousePredictor('models/rf_greenhouse_model.pkl')
    
    try:
        while True:
            # Get sensor data (simulated)
            sensor_data = simulate_sensor_reading()
            
            # Make prediction
            fan_on, watering_on = predictor.predict(sensor_data)
            
            # Log predictions
            logging.info(
                f"Sensors: {sensor_data}\n"
                f"Actions: Fan: {'ON' if fan_on else 'OFF'} | "
                f"Watering: {'ON' if watering_on else 'OFF'}"
            )
            
            # TODO: Add your actuation code here
            # Example:
            # if fan_on:
            #     activate_fan()
            # if watering_on:
            #     activate_watering()
            
            # Wait before next reading
            time.sleep(5)
            
    except KeyboardInterrupt:
        logging.info("Stopping greenhouse automation...")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
