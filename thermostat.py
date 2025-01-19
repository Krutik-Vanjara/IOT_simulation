class Thermostat:
    def __init__(self, temperature=22):
        self.temperature = temperature  # Default is 22°C

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Temperature set to {self.temperature}°C.")
