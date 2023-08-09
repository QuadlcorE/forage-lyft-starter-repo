from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors
    
    def needs_service(self):
        tire_wear_array_sum = 0
        for entry in self.wear_sensors:
            tire_wear_array_sum += entry 
            if tire_wear_array_sum >= 3:
                return True 
        return False