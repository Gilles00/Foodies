from Employee import Manager, Cook, Delivery, Salesperson
from Food import Food
from User import Member, VIP, Guest
from Supplies import Supplies

# Employee
def addDeliveryPerson(employee):
    DeliveryPeople.append(employee)
    print("Added " + employee.getFirst() + " to DeliveryPeople")

def addCook(employee):
    Cooks.append(employee)
    print("Added " + employee.getFirst() + " to Cooks")

def addSalesperson(employee):
    Sales.append(employee)
    print("Added " + employee.getFirst() + " to Sales")

def findCook(name):
    for i in range(len(Cooks)):
        if(Cooks[i].getFirst() == name):
            print('Cook ' + Cooks[i].getFirst() + ' has been found')
            return Cooks[i]

def printCooks():
    print("Printing list of Cooks...")
    if(len(Cooks) == 0):
        print("\tCooks is empty")
    else:
        print('\tCooks: ', end='')
        for i in range(len(Cooks)):
            print(Cooks[i].getFirst(), end=' ')
        print('')

# Food
def addMenuItem(food):
    Menu.append(food)
    print("Added " + food.getName() + " to Foods")
    
def printMenu():
    print("Printing list of Foods...")
    if(len(Menu) == 0):
        print("\tFoods is empty")
    else:
        for i in range(len(Menu)):
            print('\t' + Menu[i].getCate(), Menu[i].getFood_name(), Menu[i].getSpice())

# User

def getUserSize():
    return len(User)

def removeMember(user):
    User.remove(user)
    print("Removed " + user.getFirst() + " from VIP")

def findUser(name):
    for i in range(len(User)):
        if(User[i].getFirst() == name):
            print('Member ' + user[i].getFirst() + ' has been found')
            return User[i]

def promoteVIP(name):
    for i in range(len(User)):
        if(User[i].getFirst() == name):
            print(User[i].getFirst() + " found, promoting to VIP")
            para1 = User[i].getFirst()
            para2 = User[i].getLast()
            para3 = User[i].getUser()
            para4 = User[i].getEmail()
            para5 = User[i].getPass()
            removeMember(User[i])
            new = VIP(para1, para2, para3, para4, para5)
            addUser(new)
            break

    self.order.append(Food)
    self.order.append(Price)

def addCurrentUser(name):
    CurrentUser.append(name)
    
def addCurrentCart(name):
    CurrentCart.append(name)

def currentCartSize():
    return len(CurrentCart)*2

def addEmployee(name):
    Employee.append(name)
    
def addUser(user):
    User.append(user)

def sortMenu(): #Bubble sort algorithm for most relevant items, May change for only top 3 
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(Menu)-1):
            if(Menu[i].getSold() < Menu[i+1].getSold()):
                Menu[i], Menu[i+1] = Menu[i+1], Menu[i]

def printMenu():
    for i in range(len(Menu)):
        print(Menu[i].getName())

# Salesperson
# For each supplier they will have an array of different supplies in them.
def addSupplies1(Supplies):
    SuppliesList1.append(Supplies)
    print(f"Added {Supplies.getName()} to Supplies List for Supplier 1")

def addSupplies2(Supplies):
    SuppliesList2.append(Supplies)
    print(f"Added {Supplies.getName()} to Supplies List for Supplier 2")

def addSupplies3(Supplies):
    SuppliesList3.append(Supplies)
    print(f"Added {Supplies.getName()} to Supplies List for Supplier 3")

def addCurrentCart_SalesPerson(Supplies):
    CurrentCart_SalesPerson.append(Supplies)

 #====For_Storage====#   
DeliveryPeople = []
Cooks = []
Sales = []
Menu = []
IngredientList = []
User = []
Employee = []
CurrentUser = []
CurrentCart = []
SuppliesList1 = []
SuppliesList2 = []
SuppliesList3 = []
CurrentCart_SalesPerson=[]
#====For_Storage====#

# Foods
Chicken = Food('Chicken', 12.99, 'Entree', True, 100, 2, 4)
Fish = Food('Fish', 10.99, 'Entree', True, 500, 3, 5)
Duck = Food('Duck', 9.49, 'Entree', True, 122, 5, 6)
Dog = Food('Dog', 20.99, 'Entree', True, 5, 5, 7)

# Cook
John = Cook('John','Username', 'test')

# Manager
manager = Manager('y','y','y')

# Salesperson
Anderson = Salesperson('Anderson','anderson1','password',1000.00,'restaurantname','☆☆☆☆☆') #sales person example

# Users
deli = Delivery('z','z','z','z')
void = Guest('void1','void2')
eric = Member('eric','test2','t','t','t','t')
chue = VIP('chue','bloo','blee','blee','blop','t')

# Define some supplies
#### reminder to maybe add randomnized quality
# Supplier 1 - 10 sample supplies
freshChicken = Supplies('Chicken', 'Good',15.99)
Broccoli = Supplies('Broccoli', 'Bad', 5.99 )
freshDuck = Supplies('Duck', 'Best',25.99)
Lettuce = Supplies('Lettuce', 'Bad', 4.99)
Asparagus = Supplies('Asparagus', 'Bad', 6.99)
Rice = Supplies('Rice', 'Good,', 1.99)
Pasta = Supplies('Pasta', 'Good', 1.99 )
Tomato = Supplies('Tomato','Good', 2.99)
Onion = Supplies('Onion', ' Best', 3.99)
Pepper = Supplies('Pepper', 'Good', 2.99)

# Supplier 2 - 10 sample supplies
freshDog = Supplies('Dog', 'Best', 299.99) #????????
Mushroom = Supplies('Mushroom', 'Best', 9.99 )
whiteWine = Supplies('White Wine','Good', 13.99)
redWine = Supplies('Red Wine', 'Bad', 29.99 )
Truffle = Supplies('Truffle', 'Best', 199.99)
kingCrab = Supplies('King Crab', 'Good', 44.99)
Lobster = Supplies('Lobster', 'Bad', 19.99)
Salmon = Supplies('Salmon', 'Best', 39.99)
Tuna = Supplies('Tuna', 'Good', 39.99)
blueCrab = Supplies('Blue Crab', 'Good', 12.99)


# Supplier 3 - 10 sample supplies
freshDuck1 = Supplies('Duck', 'Good', 25.99)
freshChicken1 = Supplies('Chicken', 'Bad', 15.99)
honeyHam = Supplies('Honey Ham', 'Good', 7.99 )
forestHam = Supplies('Forest Ham', 'Bad', 10.99)
porkBelly = Supplies('Pork Belly', 'Bad', 15.99)
porkChops = Supplies('Pork Chop', 'Good', 10.99)
tenderloin = Supplies('Beef Tenderloin', 'Good', 44.99)
chuckSteak = Supplies('Chuck Steak', 'Best', 13.99)
ribeyeSteak = Supplies('Ribeye Steak', 'Good', 55.99)
kobeBeef = Supplies('Kobe Beef', 'Best', 119.99)


addUser(void)
addUser(chue)
addUser(eric)
addUser(John)
addUser(manager)
addUser(Anderson)
addUser(deli)
addMenuItem(Duck)
addMenuItem(Dog)
addMenuItem(Fish)
addMenuItem(Chicken)

# Add to supplies list 1
addSupplies1(freshChicken)
addSupplies1(Broccoli)
addSupplies1(freshDuck)
addSupplies1(Lettuce)
addSupplies1(Asparagus)
addSupplies1(Rice)
addSupplies1(Pasta)
addSupplies1(Tomato)
addSupplies1(Onion)
addSupplies1(Pepper)

# Add to supplies list 2
addSupplies2(freshDog)
addSupplies2(Mushroom)
addSupplies2(whiteWine)
addSupplies2(redWine)
addSupplies2(Truffle)
addSupplies2(kingCrab)
addSupplies2(Lobster)
addSupplies2(Salmon)
addSupplies2(Tuna)
addSupplies2(blueCrab)

# Add to supplies list 3
addSupplies3(freshDuck1)
addSupplies3(freshChicken1)
addSupplies3(honeyHam)
addSupplies3(forestHam)
addSupplies3(porkBelly)
addSupplies3(porkChops)
addSupplies3(tenderloin)
addSupplies3(chuckSteak)
addSupplies3(ribeyeSteak)
addSupplies3(kobeBeef)




