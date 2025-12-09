import unittest
from src.sensor import TempSensor, EntrySensor, ExitSensor
from src.car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self) -> None:
        self.car_park = CarPark("123 Example Street", 100)

        self.temp_sensor = TempSensor("temp_sensor1", True, self.car_park)
        self.entry_sensor = EntrySensor("entry_sensor1", True, self.car_park)
        self.exit_sensor = ExitSensor("exit_sensor1", True, self.car_park)

    def test_sensors_initialized_with_all_attributes(self) -> None:
        # test our entry sensor
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, "entry_sensor1")
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)

        # test our exit sensor
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, "exit_sensor1")
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)

        # test our temp sensor
        self.assertIsInstance(self.temp_sensor, TempSensor)
        self.assertEqual(self.temp_sensor.id, "temp_sensor1")
        self.assertEqual(self.temp_sensor.is_active, True)
        self.assertEqual(self.temp_sensor.car_park, self.car_park)

    def test_parking_sensor_update_car_park(self) -> None:
        # entry sensor
        self.entry_sensor.update_car_park("FAKE-001")
        self.assertIn("FAKE-001", self.car_park.plates)
        self.assertEqual(self.car_park.available_spaces, 99)
        
        # exit sensor
        self.exit_sensor.update_car_park("FAKE-001")
        self.assertNotIn("FAKE-001", self.car_park.plates)
        self.assertEqual(self.car_park.available_spaces, 100)

    def test_temp_sensor_update_car_park(self) -> None:
        self.temp_sensor.update_car_park(25.0)
        self.assertEqual(self.car_park.ambient_temp, 25.0)

    def test_parking_sensor_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.assertIn("FAKE", self.car_park.plates[0])

if __name__ == "__main__":
    unittest.main()