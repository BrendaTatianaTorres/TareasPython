from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout

class tarea(App):
  def build(self):
    boxl = BoxLayout()
    def tex(instance,value):
      print('Se ha oprimido')
      etiqueta = Label(text = 'Hola', font_size = 30)
      barra = Slider(orientation='horizontal',min=-4,max=4, value=0,value_track=True,value_track_color=(1,0,0,1))
      bt = Button(text='Presiona')
      bt.bind(state=tex)
      boxl.add_widget(barra)
      boxl.add_widget(bt)
      boxl.add_widget(etiqueta)
    return boxl

if __name__ == "__main__":
  tarea().run()