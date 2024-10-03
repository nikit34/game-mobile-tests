from pytest import mark


@mark.usefixtures('driver')
class TestOnboarding:
    def test_first_action(self):
        pass