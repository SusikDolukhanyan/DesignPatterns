
class Subject:
    def __init__(self):
        self._observers = []  

    def attach(self, observer):
        """Add an observer."""
        self._observers.append(observer)

    def detach(self, observer):
        """Remove an observer."""
        self._observers.remove(observer)

    def notify(self):
        """Notify all observers about the change."""
        for observer in self._observers:
            observer.update(self)


class TemperatureSensor(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()  


class Observer:
    def update(self, subject):
        pass


class TemperatureDisplay(Observer):
    def update(self, subject):
        print(f"TemperatureDisplay: Current temperature is {subject.temperature}°C.")

class TemperatureLogger(Observer):
    def update(self, subject):
        print(f"TemperatureLogger: Logged temperature: {subject.temperature}°C.")

if __name__ == "__main__":
    sensor = TemperatureSensor()

 
    display = TemperatureDisplay()
    logger = TemperatureLogger()

    
    sensor.attach(display)
    sensor.attach(logger)

    
    print("Setting temperature to 25°C:")
    sensor.temperature = 25

    print("\nSetting temperature to 30°C:")
    sensor.temperature = 30

    
    print("\nDetaching the display observer and setting temperature to 20°C:")
    sensor.detach(display)
    sensor.temperature = 20
