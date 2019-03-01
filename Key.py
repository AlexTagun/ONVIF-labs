import keyboard

class Key:
    def __init__(self, value):
        self.value = value
        self.isPressed = False
    
    def update(self):
        if keyboard.is_pressed(self.value):
            self.isPressed = True
        else:
            self.isPressed = False
