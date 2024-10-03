from pytest import mark


@mark.usefixtures('driver', 'appium_service')
class TestOnboarding:
    def test_first_action(self):
        pass