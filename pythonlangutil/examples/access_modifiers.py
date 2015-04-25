from pythonlangutil.access_modifiers import private_variable, private_function


class PrivateVariableTest(object):
    def __init__(self):
        self.id = "123"
        
    @private_variable('id')
    def __setattr__(self, *args, **kwargs):
        return object.__setattr__(self, *args, **kwargs)
    
    def insider(self):
        self.id = "321"
    
class PrivateFunctionTest(object):
    def __init__(self):
        pass
    
    @private_function
    def private_method(self):
        return 'called from inside my own class'
    
    def insider(self):
        return self.private_method()
        
class PrivateConstructorTest(object):
    @private_function
    def __init__(self):
        pass
