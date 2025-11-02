class SmartDevice:
    def __init__(self, name):
        self._name = name
        self._is_on = False

    def turn_off(self):
        self._is_on = False
        print(f"{self._name} turned off")
    def turn_on(self):
        self._is_on = True
        print(f"{self._name} turned on")

smart_lamp = SmartDevice('Smart Lamp')
print(smart_lamp._name)