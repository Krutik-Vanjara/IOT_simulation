class SmartLight:
    def __init__(self, status=False, brightness=0):
        self.status = status  # True for ON, False for OFF
        self.brightness = brightness  # Value between 0-100

    def toggle(self):
        self.status = not self.status
        print(f"Smart Light is now {'ON' if self.status else 'OFF'}.")

    def set_brightness(self, brightness):
        if 0 <= brightness <= 100:
            self.brightness = brightness
            print(f"Brightness set to {self.brightness}%.")
        else:
            print("Invalid brightness level! Please set a value between 0 and 100.")
