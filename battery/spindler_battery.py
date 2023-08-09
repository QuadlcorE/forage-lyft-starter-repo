from battery.battery import Battery
from utils import add_years_to_date

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        date_for_battery_service = add_years_to_date(self.last_service_date, 3)
        if date_for_battery_service < self.current_date:
            return True 
        else: 
            return False
        