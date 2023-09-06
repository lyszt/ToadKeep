import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
import pyperclip
import pyautogui
import pynput
from pynput import keyboard
from pynput.keyboard import Key, Controller

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '300')

kivy.require('2.1.0')

keyboard = Controller()
class VirtualKeyboard(FloatLayout):
    pass

class ToodKeppApp(App):
    def build(self):
        return VirtualKeyboard()
    def callback(self, instance):
        KeyCode = instance.text
        try:
            pyperclip.copy(KeyCode)
            print(f"{KeyCode} has been copied.")
        except Exception as e:
            print(e)



# Press the green Button in the gutter to run the script.
if __name__ == '__main__':
    ToodKeppApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
