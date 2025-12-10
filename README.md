# BayTracker
Lachlan Hutchings-Richards
20035488

#### Example Usage
Uncontrolled CarPark (don't register sensors/displays etc.)
```python
    car_park = CarPark("123 Example Location", 100)
    car_park_from_config = CarPark.from_config(Path("test-config.json")) # from config
```
Controlled CarPark
```python
    car_park = CarPark("123 Example Location", 100)

    # create our display and register it with our carpark
    display = Display("display1", "Example Message", True)
    car_park.register(display)

    # create our entry and exit sensors and inject our carpark
    entry_sensor = EntrySensor("entry_sensor1", True, car_park)
    exit_sensor = ExitSensor("exit_sensor1", True, car_park)

    # create our temp sensor (ambient temp returns 0 in uncontrolled lots)
    temp_sensor = TempSensor("temp_sensor1", True, car_park)
```

#### Example Configuration File
```json
{ 
    "location": "123 Example location",
    "capacity": 100,
    "plates": ["FAKE-001", "FAKE-002"]
}
```

#### Test Coverage
- CarPark
  - Initialised correctly 
  - Initialised correctly from config 
  - Write config to disk 
  - Add car
  - Remove car
  - Overfill carpark
  - Remove car that doesn't exist
- Display
  - Initialised correctly
  - Display correct message
  - Update on add car
- Sensors
  - Temp and Parking sensors initialised correctly
  - Temp sensor update carpark
  - Parking sensor update carpark
  - Parking sensor detect vehicle  
