class Note:
    def __init__(self,width, height,key_to_press):
        self.width = width
        self.height = height
        self.key_to_press = key_to_press
    
    def getKey(self):
        return self.key_to_press
