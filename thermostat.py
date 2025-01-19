class Thermostat:
    def _init_(self):
        self.status = "OFF"
        self.current_temperature = 20
        self.target_temperature = None

    def toggle_status(self):
        if self.status == "OFF":
            self.status = "ON"
        else:
            self.status = "OFF"
        print(f"Thermostat is now {self.status}")

    def set_temperature(self, target):
        if 16 <= target <= 30:
            self.target_temperature = target
            print(f"Target temperature set to {target}°C")
        else:
            print("Error: Temperature must be between 16°C and 30°C.")
