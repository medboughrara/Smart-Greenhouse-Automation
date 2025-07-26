# Smart Greenhouse Automation 🌱

An intelligent greenhouse automation system that uses machine learning to optimize environmental conditions for plant growth. The system combines sensor data analysis, machine learning predictions, and automated control mechanisms to maintain optimal growing conditions.

## 🌟 Features

### Machine Learning & Analytics
- **Dual Model Approach**: Random Forest and XGBoost models for robust predictions
- **Real-time Predictions**: Continuous monitoring and automated control decisions
- **Model Explainability**: SHAP value analysis for understanding model decisions
- **Edge Deployment**: ONNX model conversion for efficient edge computing

### Monitoring & Control
- **Interactive Dashboard**: Real-time visualization of all greenhouse parameters
- **Sensor Integration**: Modular interface for temperature, humidity, water level, and NPK sensors
- **Automated Control**: Smart actuation of fans and water pumps
- **Data Logging**: Comprehensive data collection and storage

### Technical Architecture
- **Abstract Hardware Interface**: Easy integration with different sensor/actuator setups
- **Modular Design**: Separate modules for training, prediction, and visualization
- **Extensible Framework**: Easy to add new sensors or control mechanisms

## 🗂️ Project Structure

```
Smart-Greenhouse-Automation/
│
├── data/
│   └── IoTProcessed_Data.csv          # Training and historical data
│
├── models/
│   ├── rf_greenhouse_model.pkl        # Random Forest model
│   ├── xgb_greenhouse_model.pkl       # XGBoost model
│   ├── rf_fan_model.onnx             # ONNX model for fan control
│   └── xgb_fan_model.onnx            # ONNX model for fan control
│
├── src/
│   ├── train_models.py               # Model training pipeline
│   ├── shap_explain.py              # Model explanation generation
│   ├── real_time_predict.py         # Real-time prediction system
│   ├── convert_models.py            # ONNX model conversion
│   ├── hardware_interface.py        # Sensor/actuator interfaces
│   └── dashboard.py                 # Streamlit visualization dashboard
│
├── requirements.txt                  # Project dependencies
└── README.md                        # Documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/medboughrara/Smart-Greenhouse-Automation.git
cd Smart-Greenhouse-Automation
```

2. Create and activate a virtual environment (optional but recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📋 Usage Guide

### 1. Data Preparation
- Place your sensor data in `data/IoTProcessed_Data.csv`
- Ensure the data includes: temperature, humidity, water_level, N, P, K readings

### 2. Model Training and Setup
```bash
# Train both Random Forest and XGBoost models
python src/train_models.py

# Generate model explanations with SHAP
python src/shap_explain.py

# Convert models to ONNX format for edge deployment
python src/convert_models.py
```

### 3. Real-time System
```bash
# Start the prediction system
python src/real_time_predict.py
```

### 4. Dashboard Visualization
```bash
# Launch the Streamlit dashboard
streamlit run src/dashboard.py
```

The dashboard provides:
- Real-time sensor readings
- Environmental trends
- Actuator status
- System performance metrics

## 🔧 Hardware Integration

### Implementing Custom Hardware

1. Create a new sensor interface:
```python
from src.hardware_interface import SensorInterface

class MyCustomSensor(SensorInterface):
    def read_temperature(self) -> float:
        # Implement your sensor reading logic
        return temperature_value
    
    # Implement other required methods...
```

2. Create a new actuator interface:
```python
from src.hardware_interface import ActuatorInterface

class MyCustomActuator(ActuatorInterface):
    def set_fan(self, state: bool) -> bool:
        # Implement your fan control logic
        return success_status
    
    # Implement other required methods...
```

3. Update the real-time prediction system to use your implementations:
```python
sensor = MyCustomSensor()
actuator = MyCustomActuator()
# Update real_time_predict.py accordingly
```

## 🤖 Models

### Random Forest Model
- General-purpose classifier
- Excellent interpretability
- Robust to outliers
- Used for baseline predictions

### XGBoost Model
- High-performance gradient boosting
- Better handling of complex patterns
- Optimized for production use
- Used for critical control decisions

### ONNX Deployment
- Optimized for edge computing
- Reduced model size
- Faster inference
- Cross-platform compatibility

## 📊 Dashboard Features

### Real-time Monitoring
- Current sensor readings
- Historical trends
- Actuator status

### Analysis Tools
- Temperature-humidity relationships
- NPK level tracking
- Water level monitoring
- System performance metrics

### Interactive Features
- Date range selection
- Custom visualization options
- Data export capabilities
- Real-time updates

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow Python PEP 8 style guide
- Add unit tests for new features
- Update documentation as needed
- Maintain type hints and docstrings

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Med Boughrara - [@medboughrara](https://github.com/medboughrara)

Project Link: [https://github.com/medboughrara/Smart-Greenhouse-Automation](https://github.com/medboughrara/Smart-Greenhouse-Automation)
