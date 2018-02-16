class person:
    def __init__(self,id):
        self.id=id
        print("Our calss is created")
    def __del__(self):
        print(self.id,"Our calss object is destroyed")
    
    def setFullName(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    
    def printFullName(self):
        print(self.firstName," ",self.lastName)
personName=person(101)
personName.setFullName("Rajat", "Jain")
personName.printFullName()
personName.__del__()
