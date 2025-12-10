from pathlib import Path

from car_park import CarPark
from display import Display
from sensor import TempSensor, EntrySensor, ExitSensor



car_park = CarPark("123 Example Location", 100)

# create our display and register it with our carpark
display = Display("display1", "", True)
car_park.register(display)

# create our entry and exit sensors and inject our carpark
entry_sensor = EntrySensor("entry_sensor1", True, car_park)
exit_sensor = ExitSensor("exit_sensor1", True, car_park)

# create our temp sensor (ambient temp returns 0 in uncontrolled lots)
temp_sensor = TempSensor("temp_sensor1", True, car_park)

# detect mock temp change
temp_sensor.detect_temp()

# detect car entry
entry_sensor.detect_vehicle("FAKE-001")

# detect car exit
exit_sensor.detect_vehicle("FAKE-001")

# make sure this exists before running! (check readme.md for template)
car_park = CarPark.from_config(Path("test-config.json"))