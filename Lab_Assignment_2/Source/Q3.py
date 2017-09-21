#class representing person details name, address, email
class Person_Details:
    #declares constructr for class Person_Details
    def __init__(self, p_na, p_ag):
        #use of self keyword
        self.p_name = p_na
        self.p_age = p_ag


    def person_Details(self):
        print("Person_Name:", self.p_name + " Person_Age ", self.p_age )
#inherits person_details class to addexpense class
class Addexpense(Person_Details):
    a = 0

    def __init__(self, p_na, p_ag, s, p):
        self.expense = p
        Person_Details.__init__(self, p_na, p_ag)
#calculates total expenses
    def addexpen(self):
        self.__class__.a = self.__class__.a + self.expense
        super().person_Details()
        print("Total exp. of", self.__class__.a)
        #calling previous class function with super keyword


class Income(Person_Details):
    incom = 0
    def __init__(self,p_na,p_ag,s):
        self.a = int(input("enter salary"))
        super(Income, self).__init__(p_na,p_ag)

    def salary(self):
        self.__class__.incom = self.__class__.incom + self.a
        print("total income: ", self.__class__.incom)

#multiple inheritence where addexpense and income class are inherited by balance class
class Balance(Addexpense, Income):
    balanc = 0

    def balan(self):
        self.__class__.balanc = Income.incom - Addexpense.a
        print("Remaining balance:",self.__class__.balanc)
class Tracking(Balance):
    tr = input("Enter balance limit")
    def __init__(self,a):
        self.__class__.tr = a
        if(Balance.balanc < self.__class__.tr):
            print(Balance.balanc)
            print("Limit exceeded")
#instance a is created for person_details class
a = Person_Details ("Ramu",21)
a.person_Details()
#expenses added for a person created using person details class
b = Addexpense("Ramu", 21, 100, 5)
d = Addexpense("Raju", 23, 100, 10)
b.addexpen()
d.addexpen()

e = Income("A", 1, 100)
#salary function of income class invoked
e.salary()
c = Balance("A", 1, 100, 1)
#balan function class balance invoked
c.balan()
f=Tracking(100)