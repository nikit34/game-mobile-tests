from configs.environment_config import EnvironmentConfig


class EnvironmentManager:
    @staticmethod
    def execute_platform_specific_callback(android_callback, ios_callback):
        if EnvironmentConfig.get_platform() == "android":
            return android_callback()
        else:
            return ios_callback()

    @staticmethod
    def execute_android_callback(android_callback):
        if EnvironmentConfig.get_platform() == "android":
            return android_callback()

    @staticmethod
    def execute_ios_callback(ios_callback):
        if EnvironmentConfig.get_platform() == "ios":
            return ios_callback()
