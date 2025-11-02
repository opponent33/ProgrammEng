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

    def get_status(self):
        base_status = "Turn on"
        return f"{base_status}"

class SmartLamp(SmartDevice):
    def __init__(self, name, brightness):
        super().__init__(name)
        self._is_on = False
        self._brightness = brightness
    def change_brightness(self, brightness):
        self._is_on = brightness > 100
        self._brightness = brightness
        print(f"{self._name} brightness changed to {brightness}")

    def get_status(self):
        base_status = super().get_status()
        return f"{base_status}, Яркость: {self._brightness}%"

class SmartTV(SmartDevice):
    def __init__(self, name, channel=1, volume=10):
        super().__init__(name)
        self._channel = channel
        self._volume = 0
        self.set_volume(volume)  #

    def set_channel(self, channel):
        if channel > 0:
            self._channel = channel
            print(f"{self._name} переключен на канал {channel}.")

    def set_volume(self, level):
        if 0 <= level <= 100:
            self._volume = level
            print(f"Громкость {self._name} установлена на {level}.")
        else:
            print("Ошибка: Громкость должна быть от 0 до 100.")

    def get_status(self):
        base_status = super().get_status()
        return f"{base_status}, Канал: {self._channel}, Громкость: {self._volume}"
my_devices = [
    SmartLamp("Прихожая лампа", 100),
    SmartTV("Гостиная TV", channel=5, volume=25)
]
for device in my_devices:
    device.turn_on()
    print(device.get_status())
    print("---")