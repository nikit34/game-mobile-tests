from configs._config import Config


class DeviceAppiumConfig(Config):
    CONFIG = 'json/device_appium.json'

    def __init__(self, device):
        self.device = self.choice_device(device)

    def choice_device(self, device):
        config = self.load_config(self.CONFIG)
        if device not in config:
            raise KeyError("The device '" + device + "' was not found in the config")
        return config[device]

    def get_height(self):
        return self.device.get("height")

    def get_width(self):
        return self.device.get("width")
