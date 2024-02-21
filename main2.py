import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.screensize(600,600)
designer = trtl.Turtle()
stockWriter = trtl.Turtle()
moneyWriter= trtl.Turtle()
otherWriter = trtl.Turtle()
dayWriter = trtl.Turtle()
dayEnd = ""
bought = ""
money = 50
stocks = []#10
stockMaxes=[]#10
stockGet=[]
realEstates=[]#3
posstates = ["E1", "E2", "E3"]
estateValues = [0,0,0]
estateMaxes = [0,0,0]
estateBought = [False, False, False]
customers = [0,0.01,0.02,0.03,0.04,0.05]
eSold = [False, False, False, False, False]
increasePercent = [0,0,0]
posStocks = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
posLoans = ["L1", "L2", "L3", "L4"]
cryptocurrency=0
crMax=rand.randint(40,400)
crCount=0
crDirect=True
bonds=[]#5
posBonds = ["B1", "B2", "B3", "B4", "B5"]
bondB = [False, False, False, False, False]
bondMaxes = [30, 60, 85, 115, 145]
bondPay = [0,0,0,0,0]
randComps=[]#5
posComps = ["C1", "C2", "C3", "C4", "C5"]
compMaxes = [0,0,0,0,0]
incrementList=[0.08, 0.07,0.06,0.05,0.04,0.02]
loans = []#4
loanBought=[False, False, False, False]
debt = 0
lChoice=''
owned = []
debtShow = False
designer.speed(0)
# this sets start random values, raise, and drop/resets for the stocks
def setValues():   
    x=0
    while x < 10:
        if len(stocks) < 10:
            stocks.append(rand.randint(5,20))
            stockGet.append(False)
            stockMaxes.append(rand.randint(40,300))
        elif stockMaxes[x] < stocks[x]:
            stocks[x]=rand.randint(10,35)
            stockMaxes[x]=rand.randint(40,300)
            #print(stocks[x],stockMaxes[x])
        elif stockMaxes > stocks[x]:
            stocks[x]+=rand.randint(5,30)
            #print(stocks[x], stockMaxes[x])
        x+=1
#this writes the money, real estates, and cryptocurrency values onto the screen
def writeMoneyValues():
    moneyWriter.clear()
    moneyWriter.penup()
    moneyWriter.goto(-290,250)
    moneyWriter.pendown()
    moneyWriter.write("Money:" + str(money), False, font=("Arial", 25, "bold"))
    moneyWriter.penup()
    moneyWriter.goto(-290,200)
    moneyWriter.pendown()
    moneyWriter.write("(CR) Crypto: " + str(int(cryptocurrency)), False, font=("Arial", 25, "bold"))
    for x in range(3):
        if len(realEstates) < 3:
            realEstates.append(50)
        moneyWriter.penup()
        moneyWriter.goto(-290,150 - (x*50))
        moneyWriter.pendown()
        moneyWriter.write("(E" + str(x+1) + ") Estate: "  + str(int(realEstates[x])) , False, font=("Arial", 25, "bold"))

  #this writes the stock values on the screen  
def writeStockValues():
    stockWriter.clear()
    x = 0
    while x < 10:
        if x < 5:
            l = -90
            w = (x * -50)+250
            stockWriter.penup()
            stockWriter.goto(l,w)
            stockWriter.pendown()
            stockWriter.write("(S" + str(x+1) + ")Stock:"+ str(stocks[x]), False, font=("Arial", 25, "bold"))
        else:
            l = 110
            w = ((x-5) * -50)+250
            stockWriter.penup()
            stockWriter.goto(l,w)
            stockWriter.pendown()
            stockWriter.write("(S" + str(x+1) + ")Stock:"+ str(stocks[x]), False, font=("Arial", 25, "bold"))
        x+=1
#this writes the bonds, loans and random companies on the screen
def writeOtherValues():
    otherWriter.clear()
    for x in range(14):
        if x < 5:
            l = -290
            w = (x * -50) 
            if len(bonds) < 5:
                bonds.append((x+1)*25)
            otherWriter.penup()
            otherWriter.goto(l,w)
            otherWriter.pendown()
            otherWriter.write("(B" + str(x+1) + ") Bond: " + str(bonds[x]), False, font=("Arial", 25, "bold"))
        elif x < 10:
            l = -90
            w = ((x-5) * -50) 
            if len(randComps) < 5:
                randComps.append(0)
            otherWriter.penup()
            otherWriter.goto(l,w)
            otherWriter.pendown()
            otherWriter.write("(C" + str(x-4) + ") Comp: " + str(randComps[x-6]), False, font=("Arial", 25, "bold"))
        else:
            l = 110
            w = ((x-10) * -50)
            if len(loans) < 5: 
                loans.append(x*5)
            otherWriter.penup()
            otherWriter.goto(l,w)
            otherWriter.pendown()
            otherWriter.write("(L" + str(x-9) + ") Loan: " + str(loans[x-11]), False, font=("Arial", 25, "bold"))
#this raises the money, or drops tha amount of money in crypto
def cryptoRaise():
    global crDirect
    global crMax
    global cryptocurrency
    if crDirect == True:
        if crMax < cryptocurrency:
            crMax = rand.randint(40,400)
            crDirect=False
            if cryptocurrency<100:
                cryptocurrency-=35
            else:
                cryptocurrency == rand.randint(40,100)
        if cryptocurrency > 0:
            cryptocurrency *= (rand.choice(customers) + 1)
            cryptocurrency = round(cryptocurrency)
    elif crDirect == False:
        if crMax < (cryptocurrency + 35):
            cryptocurrency * (1-rand.choice(customers))
        else:
            crDirect=True
#this allows you to buy or sell cryptocurrency
def cryptoAction():
    global money
    global cryptocurrency
    crChoice = ""
    if bought.upper() == "CR":
        crChoice = input("\nWould you like to buy(B) or sell(S)?  ")
        if crChoice.upper() == "B":
            crCount = input("\nHow much do you want to buy?  ")
            try:
                crCount = int(crCount)
            except ValueError:
                print("\nPlease enter a number.")
                return
            if crCount <= money and crCount > 0:
                cryptocurrency += crCount
                money-=crCount
                print("\nYou bought " + str(crCount) + " dollars in crypto.")
            elif crChoice > money:
                print("\nYou don't have that much money")
            else:
                print("\nAn error occured. Please enter a valid option next time.")
    if crChoice.upper() == "S":
            crCount = int(input("\nHow much do you want to sell?  "))
            if crCount <= cryptocurrency and crCount == int and crCount > 0:
                cryptocurrency -= crCount
                money+=crCount
            elif crCount > cryptocurrency:
                print("\nYou don't have that much money.")
            else:
                print("\nPlease enter a number greater than 0.")
#this allows you to buy or sell stocks
def buyStocks():
    for x in range(len(posStocks)):
        if bought.upper() == posStocks[x]:
            global money
            if stockGet[x] == False and money > stocks[x]:
                stockGet[x]= True
                owned.append(posStocks[x])
                money = money - stocks[x]
                print("\nYou bought a Stock.")
            elif stockGet[x] == True:
                money += stocks[x]
                stockGet[x] = False
                owned.remove(posStocks[x])
                print("\nYou Sold a stock.")
            else:
                print("\nYou are unable to buy this.")   
#this allows you to buy a loan, and pay it off
def buyLoans():
    for x in range(len(posLoans)):
        global money
        global bought
        global debt
        if bought.upper() == posLoans[x]: 
            if loanBought[x]== False and debt == 0:
                debtShow = True
                money+=loans[x]
                debt+=loans[x]+25
                print("\nYou bought a loan!")
                owned.append(posLoans[x])
                loanBought[x] = True
            elif loanBought[x] == True and debt > 0:
                lChoice = input("\nHow much debt would you like to payoff?  ")
                try:
                    lChoice = int(lChoice)
                except ValueError:
                    print("\nPlease enter a number.")
                if int(lChoice) > 0 and int(lChoice) <= debt:
                    debt -= int(lChoice)
                    money -= int(lChoice)
                else:
                    print("\nPlease choose a viable number.")

            elif loanBought[x]== False and debt != 0:
                print("\nPlease pay off all debt before buying another loan.") 
#This allows you to buy an estate and raise the amount of money invested into it
def buyEstates(wants):
    
    for x in range(len(posstates)):
        global money
        global bought
        global eChoice
        if wants > 0 and estateBought[x] == True:
            increasePercent[x] += (wants)
            print("\nYour open house went well! You have " + str(wants * 100) + " people interested in the estate, therefore we raised the price by " + str(wants) + "." )
        if bought.upper() == posstates[x]:
            if wants==0 and estateBought[x] == True:
                print("\nIf you own an estate, Your open houses are every five days.")
            if estateBought[x] == True and eSold[x] == False:
                eChoice = input("\nWould you like to (S)sell or (R)renovate?  ")
                if eChoice.upper() == "S":
                    money +=realEstates[x]
                    owned.remove(posstates[x])
                    eSold[x] = True
                elif eChoice.upper() == "R":
                    eChoice=input("\nHow much would you like to pay to renovate?  ")
                    try:
                        int(eChoice)
                    except ValueError:
                        print("Please enter an integer.")
                        return 
                    if int(eChoice) <= money and int(eChoice) >0:
                        money -= int(eChoice)
                        estateValues[x] += int(eChoice)
                        increasePercent[x] = estateValues[x] * 0.02
                    else:
                        print("\nPlease choose when you have enough money.")
                else:
                    print("\nPlease choose one of the two options.")
            elif estateBought[x] == False and money >= realEstates[x]:
                money -= realEstates[x]
                estateBought[x] = True
                owned.append(posstates[x])
                print("\nEstate bought")
            else:
                print("\nPlease buy when you have enough money.")

#this increases the amount of money an estate is worth
def estatesIncrease():
    for x in range(len(estateMaxes)):
        addV = 4 * realEstates[x]
        if estateValues[x] == 0:
            estateMaxes[x] = addV
        if estateMaxes[x] > realEstates[x]:
            realEstates[x] *= (1 + increasePercent[x]) 
            realEstates[x] = round(realEstates[x])
            
#this allows you to buy a bond
def buyBond():
    global bought
    global money
    for x in range(len(posBonds)):
        if bought.upper() == posBonds[x]:
            if money >= bonds[x] and bondB[x] == False:
                money -= bonds[x]
                bondB[x] = True
            else:
                print("You can not buy this bond")
#this pays you over time for the bond that you bought
def payBonds():
    global money
    for x in range(len(bondB)):
        if bondB[x] == True:
            if bondPay[x] < bondMaxes[x]:
                bondAdd = bondMaxes[x]/5
                bondPay[x] += bondAdd
                money += bondAdd

#this allows you to pick how much money you want to invest into a company
def buyComp():
    global money
    global bought
    compChoice = ""
    for x in range(len(posComps)):
        if compMaxes[x] == 0:
            compMaxes[x] == rand.randint(50,250)
        if bought.upper() == posComps[x]:
            if randComps[x] == 0:
                compChoice = input("\nHow much do you want to input?  ")
                try:
                    compChoice = int(compChoice)
                except ValueError:
                    print("Please enter an integer.")
                    return
                if compChoice <= money and compChoice > 0:
                    money -= compChoice
                    owned.append(posComps[x])
                    randComps[x]+= compChoice
            elif randComps[x] > 0:
                money+=randComps[x]
                owned.remove(posComps[x])
                randComps[x] = 0
                
#this causes your investment companies money to raise
def compRaise():
    for x in range(len(randComps)):
        if randComps[x] < compMaxes[x]:
            randComps[x] += round(randComps[x]*rand.choice(incrementList))
            #print("Raise")
        elif randComps[x] > compMaxes[x]:
            compMaxes[x] = rand.randint(50,250)
            randComps[x] = 40
            #print("Reset")



##########User InterFace#########
designer.penup()
designer.goto(-300,300)
designer.pendown()
z=0
while z < 6:
    if z == 0:
        y=50
        x=200
    elif z == 1:
        x=200
        y=100
    elif z == 2:
        x=200
        y=250
    elif z == 3:
        x=200
        y=500
    elif z == 4:
        x=600
        y=250
    elif z == 5:
        x=400
        y=500
    designer.forward(x)
    designer.right(90)
    designer.forward(y)
    designer.right(90)
    designer.forward(x)
    designer.right(90)
    designer.forward(y)
    designer.right(90)
    z+=1

designer.forward(600)
designer.right(90)
designer.forward(450)
designer.right(90)
designer.forward(200)
designer.left(90)
designer.forward(50)
designer.left(90)
designer.forward(200)
designer.left(90)
designer.forward(600)
days=1
designer.penup()
designer.goto(-290,-280)
designer.pendown()
designer.write("Hello Player. You must use the money that you start off with to invest and become rich in as few days as possible. \n If you type the combo before the option, You can transfer money into cryptocurrency with hopes that it will gain \n more value for it to be pulled out. You can also buy and sell stocks in a gamble to earn more. You can take a loan \n with about an 8% interest rate, or use a bond that will give you about 15% back over 5 days. Give any amount of money \n that you want to a investment manager (comp) so they can 'invest' your money for you, or spend money to raise the \n value of owned real estates. If you select a already bought choice again then you will be able to use different\n options. Type y to move on to the next day. Try to win $3000 in as few days as possible." , False, font=("Arial", 10, "bold"))
y = 0
done = False
# this is the loop that calls the functions when needed
while y < 1:
    dayEnd=False
    if done == True:
        break
    while dayEnd == False:  
        print("\nDay: " + str(days) + "\n")
        bought="n"
        days+=1
        dayWriter.clear()
        dayWriter.penup()
        dayWriter.goto(110,-200)
        dayWriter.pendown()
        dayWriter.write("Days :" + str(days), False, font=("Arial", 25, "bold"))
        writeMoneyValues()
        writeOtherValues()
        setValues()
        writeStockValues()
        cryptoRaise()
        payBonds()
        estatesIncrease()
        compRaise()
        while bought.lower() != "y":
            print("------------------------------------------")
            for x in owned:
                print(str(x) + "   ")
            print("\nMoney: $" +  str(int(money)))
            print("\nCryptoCurrency: $" + str(int(cryptocurrency)))
            print("\nDebt: $" + str(debt))
            bought = input("\nWhat would you like to buy?  ")
            buyLoans()
            buyStocks()
            cryptoAction()
            if days % 5 == 0:
                buyEstates(rand.choice(customers))
            else:
                buyEstates(0)
            buyBond()
            buyComp()
            if bought.lower() == "y":
                print("------------------------------------------")
                dayEnd==True
                if money >=3000 and debt == 0:
                    print("done")
                    done = True
                    break
        if done == True:
            break
    

print("Congrats on getting 3000 dollars!\nIt only took you " + str(days) + " days." )