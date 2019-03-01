from Key import Key

class NumPad:
    def __init__(self):
        self.keys = [Key('1'), Key('2'), Key('3'), Key('4'), Key('5'), Key('6'), Key('7'), Key('8'), Key('9'), Key('-'), Key('+')]
        self.dictionary = {
            '1' : {'x' : -1, 'y' : -1, 'z' :  0},
            '2' : {'x' :  0, 'y' : -1, 'z' :  0},
            '3' : {'x' :  1, 'y' : -1, 'z' :  0},
            '4' : {'x' : -1, 'y' :  0, 'z' :  0},
            '6' : {'x' :  1, 'y' :  0, 'z' :  0},
            '7' : {'x' : -1, 'y' :  1, 'z' :  0},
            '8' : {'x' :  0, 'y' :  1, 'z' :  0},
            '9' : {'x' :  1, 'y' :  1, 'z' :  0},
            '-' : {'x' :  0, 'y' :  0, 'z' : -1},
            '+' : {'x' :  0, 'y' :  0, 'z' :  1},
        }
    def update(self):
        for key in self.keys:
            key.update()
    
    def getPressedKey(self):
        for key in self.keys:
            if(key.isPressed):
                return key
        return None
    
    # Get Velocity for continuous moving, whitch depends on pressed key
    def getVelocity(self, key):
        value = key.value
        Velocity = self.dictionary.get(value, '1')
        # Velocity.x = Velocity.get('x', 0)
        # Velocity.y = Velocity.get('y', 0)
        # Velocity.z = Velocity.get('z', 0)
        return self.dictionary.get(value, '1')

        