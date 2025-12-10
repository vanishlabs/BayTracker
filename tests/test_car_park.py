import unittest
import json
import os
from pathlib import Path
from src.car_park import CarPark


class TestCarPark(unittest.TestCase):
    def setUp(self):
        with Path("config.json").open("w") as file:
            config = {
                "capacity": 100,
                "location": "123 Example Street",
                "plates": ["FAKE-001"],
            }

            json.dump(config, file)

        self.car_park_with_config = CarPark.from_config(Path("config.json"))
        self.car_park = CarPark("123 Example Street", 100)

    def test_car_park_from_config(self):
        # test if initialised correctly from config
        self.assertIsInstance(self.car_park_with_config, CarPark)
        self.assertEqual(self.car_park_with_config.location, "123 Example Street")
        self.assertEqual(self.car_park_with_config.capacity, 100)
        self.assertEqual(self.car_park_with_config.plates, ["FAKE-001"])
        self.assertEqual(self.car_park_with_config.displays, [])
        self.assertEqual(self.car_park_with_config.available_spaces, 99)

    def test_car_park_write_config_file(self):
        # tests if writes file.
        self.car_park.config_path = Path("test-config.json")
        path = Path(self.car_park.config_path)
        if os.path.exists(path):
            os.remove(path)

        self.car_park.add_car("FAKE-001")

        self.car_park.write_config()

        self.assertEqual(os.path.exists(path), True)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_spaces, 100)

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_spaces, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_spaces, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")

        self.assertEqual(self.car_park.available_spaces, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_spaces, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_spaces, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")


if __name__ == "__main__":
    unittest.main()
