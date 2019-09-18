from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty, OptionProperty
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class Calculator(Widget):
    inp_height = ObjectProperty(None)
    inp_weight = ObjectProperty(None)
    inp_gender = ObjectProperty(None)
    inp_hours   = ObjectProperty(None)
    inp_rd = ObjectProperty(None)
    bac = StringProperty(None)
    drinks_amount = StringProperty(None)

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.bac = "Please enter your details"
        self.alcohol = 0
        self.drinks_amount = "0"

    def update(self):
        try:
            height = float(self.inp_height.text)
            weight = float(self.inp_weight.text)
            gender = str(self.inp_gender.text)
            hours = float(self.inp_hours.text)
            rd = float(self.inp_rd.text)
            if gender == "f":
                redfac = 0.31223 - 0.006446 * weight + 0.004466 * height
            else:
                 redfac = 0.31608 - 0.004821 * weight + 0.004432 * height
            if self.alcohol != 0:
                tBAK = (self.alcohol * 0.8) / (weight * redfac)
                tBAKrd = tBAK - (tBAK*rd/100)
                tBAKab = tBAKrd - (hours*0.15)
                if tBAKab < 0:
                    tBAKab = 0
                self.bac = "blood alcohol concentration: \n" + str(round(tBAKab, 2))
            else:
                self.bac = "Can not calculate \nblood alcohol concentration"
        except ValueError:
            self.bac = "Can not calculate \nblood alcohol concentration"

    def on_enter1(self,val):
        self.popupWindow1.dismiss()
        self.alcohol += float(self.ac.text)/100 * float(self.am.text)*1000
        self.update()

    def on_enter2(self,val):
        self.popupWindow2.dismiss()
        
    def add_drink(self):
        self.ac = DataInput(text='', multiline=False)
        self.ac.bind(on_text_validate=self.on_enter1)
        self.popupWindow1 = Popup(title="alcohol conzentration (in %)", content=self.ac, size_hint=(None, None), size=(400,400))
        self.popupWindow1.open()
        self.am = DataInput(text='', multiline=False)
        self.am.bind(on_text_validate=self.on_enter2)
        self.popupWindow2 = Popup(title="amount (in l)", content=self.am, size_hint=(None, None), size=(400,400))
        self.popupWindow2.open()
        self.drinks_amount = str(int(self.drinks_amount)+1)

    def remove_drink(self):
        self.alcohol = 0
        self.drinks_amount = "0"
        self.update()

class DataInput(TextInput):
	input_type = OptionProperty('number', options=('number', 'text'))

class DrinkApp(App):
    def build(self):
        self.load_kv('main.kv')
        return Calculator()

if __name__ == '__main__':
    DrinkApp().run()
