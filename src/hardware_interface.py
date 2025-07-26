import os
from typing import Optional

class SensorInterface:
    """
    Abstract base class for sensor interfaces.
    Implement this class for your specific sensor hardware.
    """
    def read_temperature(self) -> Optional[float]:
        """Read temperature sensor."""
        raise NotImplementedError
    
    def read_humidity(self) -> Optional[float]:
        """Read humidity sensor."""
        raise NotImplementedError
    
    def read_water_level(self) -> Optional[float]:
        """Read water level sensor."""
        raise NotImplementedError
    
    def read_npk(self) -> tuple[Optional[float], Optional[float], Optional[float]]:
        """Read NPK (Nitrogen, Phosphorus, Potassium) sensors."""
        raise NotImplementedError

class ActuatorInterface:
    """
    Abstract base class for actuator interfaces.
    Implement this class for your specific actuator hardware.
    """
    def set_fan(self, state: bool) -> bool:
        """Control fan actuator."""
        raise NotImplementedError
    
    def set_water_pump(self, state: bool) -> bool:
        """Control water pump actuator."""
        raise NotImplementedError

# Example implementation for simulation
class SimulatedSensorInterface(SensorInterface):
    def read_temperature(self) -> float:
        return 31.0
    
    def read_humidity(self) -> float:
        return 40.0
    
    def read_water_level(self) -> float:
        return 90.0
    
    def read_npk(self) -> tuple[float, float, float]:
        return 130.0, 90.0, 100.0

class SimulatedActuatorInterface(ActuatorInterface):
    def __init__(self):
        self.fan_state = False
        self.pump_state = False
    
    def set_fan(self, state: bool) -> bool:
        self.fan_state = state
        print(f"Fan turned {'ON' if state else 'OFF'}")
        return True
    
    def set_water_pump(self, state: bool) -> bool:
        self.pump_state = state
        print(f"Water pump turned {'ON' if state else 'OFF'}")
        return True
