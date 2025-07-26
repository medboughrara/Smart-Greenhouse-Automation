# Dataset Description

This directory should contain the following data file:

- `IoTProcessed_Data.csv`: Contains processed IoT sensor data with the following columns:
  - `date`: Timestamp of the reading
  - `tempreature`: Temperature reading in Celsius
  - `humidity`: Humidity percentage
  - `water_level`: Water level percentage
  - `N`: Nitrogen level
  - `P`: Phosphorus level
  - `K`: Potassium level
  - `Fan_actuator_ON`: Binary indicator for fan status
  - `Fan_actuator_OFF`: Binary indicator for fan status
  - `Watering_plant_pump_ON`: Binary indicator for water pump status
  - `Watering_plant_pump_OFF`: Binary indicator for water pump status
  - `Water_pump_actuator_ON`: Binary indicator for water pump actuator status
  - `Water_pump_actuator_OFF`: Binary indicator for water pump actuator status

## Data Format

The data should be in CSV format with the following specifications:
- Comma-separated values
- UTF-8 encoding
- First row contains headers
- No missing values

## Sample Data Structure

```csv
date,tempreature,humidity,water_level,N,P,K,Fan_actuator_ON,Fan_actuator_OFF,Watering_plant_pump_ON,Watering_plant_pump_OFF,Water_pump_actuator_ON,Water_pump_actuator_OFF
2025-07-26 10:00:00,31,40,90,130,90,100,1,0,0,1,0,1
```

You can download the complete dataset from the project's releases page.
