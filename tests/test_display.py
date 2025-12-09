import unittest
from src.display import Display
from src.car_park import CarPark


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display("display1", "Example message", True)
        self.car_park = CarPark("123 Example Street", 100)

        self.car_park.register(self.display)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, "display1")
        self.assertEqual(self.display.message, "Example message")
        self.assertEqual(self.display.is_active, True)

    def test_update_display_message(self):
        data: dict[str, int | float] = {
            "available_spaces": 50,
            "temperature": 0,
        }

        self.display.update(data)
        expected_message = "Available spaces: 50\nTemperature: 0\n"
        self.assertEqual(self.display.message, expected_message)

    def test_update_display_on_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.add_car("FAKE-002")

        expected_message = "Available spaces: 98\nTemperature: 0\n"
        self.assertEqual(self.display.message, expected_message)

if __name__ == "__main__":
    unittest.main()
