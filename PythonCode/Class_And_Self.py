class person:
    def setFullName(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    
    def printFullName(self):
        print(self.firstName," ",self.lastName)
personName=person()
personName.setFullName("Rajat", "Jain")
personName.printFullName()
