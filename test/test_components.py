import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date, today)

        self.assertTrue(battery.needs_service())
    
    def test_does_not_need_service(self):
        today = datetime.today().date()

        battery = NubbinBattery(today, today)

        self.assertFalse(battery.needs_service())
    
class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year -5)

        battery = SpindlerBattery(last_service_date, today)

        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year -3)

        battery = SpindlerBattery(last_service_date, today)

        self.assertFalse(battery.needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 30001
        last_service_mileage = 0 

        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.engine_should_be_serviced())

    def test_does_not_need_service(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.engine_should_be_serviced())

class TestStermanEngine(unittest.TestCase):
    def test_needs_service(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)

        self.assertTrue(engine.engine_should_be_serviced())
    
    def test_does_not_need_service(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)

        self.assertFalse(engine.engine_should_be_serviced())

class TestWillougbyEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0 

        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.engine_should_be_serviced())

    def test_does_not_need_service(self):
        current_mileage = 60000
        last_service_mileage = 0 
        
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.engine_should_be_serviced())

class TestCariganTire(unittest.TestCase):
    def test_need_service(self):
        wear_sensors = [0.9, 0.8, 0.6, 1]

        tire = CarriganTire(wear_sensors)

        self.assertTrue(tire.needs_service())
    
    def test_does_not_need_service(self):
        wear_sensors = [0.5, 0.8, 0.2, 0.3]

        tire = CarriganTire(wear_sensors)

        self.assertFalse(tire.needs_service())
    
class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service(self):
        wear_sensors = [0.9, 0.8, 0.6, 1]

        tire = OctoprimeTire(wear_sensors)

        self.assertTrue(tire.needs_service())

    def test_does_not_need_service(self):
        wear_sensors = [0.5, 0.8, 0.2, 0.3]

        tire = OctoprimeTire(wear_sensors)

        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()