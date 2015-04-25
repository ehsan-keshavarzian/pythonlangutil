from UtilLib.singleton import Singleton

@Singleton()
class SingletonTest():
    def __init__(self):
        self.id = "1"
    
    def set_id(self, value):
        self.id = value