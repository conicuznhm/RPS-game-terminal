# 1
def option1():
    return "rock"

def option2():
    return "paper"

def option3():
    return "scissors"

def default():
    return "Error"

def switchCase(arg):
    cases = {
        1: option1(),
        2: option2(),
        3: option3()
    }
    return cases.get(arg, default())

print(switchCase(1))

# 2
class Switch:
    @classmethod
    def switch(cls,arg):
        return getattr(cls, "option"+str(arg), cls.default)()
    
    @staticmethod
    def option1():
        return "rock"
    @staticmethod
    def option2():
        return "paper"
    @classmethod
    def option3(cls):
        return "scissors"
    @classmethod
    def default(cls):
        return "Error"

print(Switch.switch(1))

# 3
def switch(arg):
    match arg:
        case 1:
            return "rock"
        case 2:
            return "paper"
        case 3:
            return "scissors"
        case default:
            return "Error"

print(switch(1))





# # 2 instance method
# class Switch:
#     def switch(self,arg):
#         return getattr(self, "option"+str(arg), self.default)()
    
#     def option1(self):
#         return "rock"
#     def option2(self):
#         return "paper"
#     def option3(self):
#         return "scissors"
#     def default(self):
#         return "Error"

# switch = Switch()
# print(switch.switch(1))


# class MyClass:
#     def __init__(self, instance_attr):
#         self.instance_attr = instance_attr

#     @classmethod
#     def class_method(cls):
#         instance = cls("Example")  # Creating an instance of the class
#         print(instance.instance_attr)  # Accessing instance attribute


# MyClass.class_method()  # Output: Example