from UtilLib.overload import Overload, signature


class OverloadTest():
    def __init__(self):
        self.male_pref = "Mr. %s"
        self.female_pref = "Ms. %s"
        self.general_pref = "Dear %s"
    
    @Overload
    @signature("str", "bool")
    def my_method(self, name, male):
        if male:
            return self.male_pref % name 
        return self.female_pref % name

    @my_method.overload
    @signature("str")
    def my_method(self, name):
        return self.general_pref % name
    
    @my_method.overload
    @signature("int", "str")
    def my_method(self, times, name):
        return "\n".join([self.general_pref % name for i in range(times)])

