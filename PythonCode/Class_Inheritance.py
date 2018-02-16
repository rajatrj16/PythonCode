class parent:
    value1 = "This is value 1"
    value2 = "This is value 2"

class child (parent):
    pass

parentInstance = parent()
print(parentInstance.value1)
print(parentInstance.value2)
childInstance = child()
print(childInstance.value1)
print(childInstance.value2)
