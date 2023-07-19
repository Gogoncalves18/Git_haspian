import kivy 
  
from kivy.app import App 
  
from kivy.uix.button import Button 
  
from kivy.uix.relativelayout import RelativeLayout 
  
from kivy.config import Config 
      
Config.set('graphics', 'resizable', True) 
  
class Pos_Size_App(App): 
      
    def build(self): 
  
        
        rl = RelativeLayout(size =(300, 300)) 
          
        
        
        
        b1 = Button(size_hint =(.2, .2), 
                    pos_hint ={'center_x':.7, 'center_y':.5}, 
                    text ="pos_hint") 
  
        
        
        b2 = Button(size_hint =(.5, .2),  
                    text ="size_hint") 
  
                
        
        
        b3 = Button( size_hint =(.2, .2),
                    pos =(200, 200), 
                    text ="pos") 
          
          
  
        
        rl.add_widget(b1) 
        rl.add_widget(b2) 
        rl.add_widget(b3) 
      
          
        
        return rl 
  
if __name__ == "__main__": 
    Pos_Size_App().run() 