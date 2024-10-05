## e2e автотесты на игру Township
в [Google Play](https://play.google.com/store/apps/details?id=com.playrix.township)

### Структура проекта
1. Тесты сложены в папке `tests/` у корня репозитория
   1. На втором уровне находится разделение по видам тестов (`smoke/`, `uat/`, `regress/`, `analytics/` и т.д.)
   2. Названия файлов с тестами следуют шаблону `test_<цель_тестирования>.py`
2. Экраны приложения расположены в папке `src/screens/` у корня репозитория
   1. Каждый экран помещается в свою папку, даже если он там один, по принципу `src/screens/<название_экрана>/*.py|.png`
   2. Название экрана пишется по шаблону `<название_экрана_screen>.py|.png`
3. Компоненты приложения могут быть размещены в двух разных местах, в зависимости от их использования:
   1. Если компонент принадлежит только одному экрану, он будет помещён в папку `src/screens/<название_экрана>/components/*.py|.png`
   2. Если компонент встречается на разных экранах, он будет находиться в папке `src/components/` у корня репозитория, по принципу `src/components/*.py|.png`
   3. Название компонента пишется по шаблону `<название_компонента_component>.py|.png`
4. Элементы приложения расположены в папке `src/elements/` у корня репозитория
   1. Название элемента пишется по шаблону `<название_элемента_element>.py|.png`
5. Конфигурация автотестов хранится в папке `configs/` у корня репозитория


### Конфигурация для подключения к приложению через Appium
#### Android
```commandline
{
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.playrix.township",
  "appium:appActivity": "com.playrix.township.Launcher"
}
```
#### iOS
```commandline
{
  "platformName": "iOS",
  "appium:udid": "00008030-000E65521444202E",
  "appium:fullReset": true,
  "appium:automationName": "XCUITest",
  "appium:bundleId": "com.playrix.township-ios",
  "appium:app": "Downloads/township.ipa"
}
```