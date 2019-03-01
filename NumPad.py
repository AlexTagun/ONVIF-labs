from Key import Key

class NumPad:
    def __init__(self):
        self.keys = [Key('1'), Key('2'), Key('3'), Key('4'), Key('5'), Key('6'), Key('7'), Key('8'), Key('9')]
    
    def update(self):
        for key in self.keys:
            key.update()
    
    def getPressedKey(self):
        for key in self.keys:
            if(key.isPressed):
                return key
        return None

        