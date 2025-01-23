import time
print('Welcome to Chissoe Casino')
time.sleep(1)
print('We have a large selections of games here')
time.sleep(1)
print('Slots, Blackjack, Roulette, Higher or Lower, and Craps')
activity = input('Would you like to play a game? Check your balance? or Earn some money 1/2/3')
if activity = '1' :
    gamechoice = input('Would you like to play Slots, Blackjack, Roulette, Higher or Lower, or Craps? 1/2/3/4/5')
    if gamechoice = '4'
        higherlower()
elif activity = '2' :
    print('You have $' + str(MoneyFunc())


def MoneyFunc() :
    f = open('Money.txt', 'r')
    var = f.read().strip()
    return int(float(var))
    f.close

def changeMoney(money) :
    f = open('Money.txt', 'r')
    previousbalance = f.read().strip()
    newbalance = int(float(previousbalance)) + money
    f.close
    f = open('Money.txt', 'w')
    f.write(str(newbalance))
    f.close

def higherlower() :
    import time
    global money, won
    money = MoneyFunc()
    def game() :
        from random import randint
        global money, won
        number = randint(0,100)
        amountbet = int(input('How much do you want to bet? '))
        time.sleep(1)
        while amountbet > money :
            print('You cannot bet more then you have')
            time.sleep(1)
            amountbet = int(input('How much do you want to bet? '))
            time.sleep(1)
        highlow = input('Do you think the number is higher or lower then 50? higher/lower ')
        if highlow == 'higher' and number > 50 :
            won = amountbet * 1.25
            print('Nice guess you won $' + str(amountbet * 1.25))
            changeMoney(won)
        elif highlow == 'lower' and number < 50 :
            won = amountbet * 1.25
            print('Nice guess you won $' + str(amountbet * 1.25))
            changeMoney(won)
        else :
            print('Unlucky... You lost ')
            lost = amountbet * -1
            changeMoney(lost)
            time.sleep(1)
            print('You should try your luck again. ')

    print('Welcome to Higher or Lower. ')
    time.sleep(1)
    print("It's a simple game")
    time.sleep(1)
    print('All you have to do is guess if the number is higher or lower then the current number.')
    time.sleep(2)
    ready = input('Ready to play? yes or no ')
    while ready == 'yes' :
        game()
        ready = input('Want to play again? yes or no ')
    time.sleep(1)
    print('Come again soon ')

#SLOTS
from random import randint
import time
money = 5000

def FullSlot():
    global money
    print('Hello player, lets test your luck!')
    time.sleep(.5)
    slotgame()
def slotgame():
    global money
    time.sleep(.4)
    print('You have $' + str(money))
    Slots()

def Slots():
    global money
    time.sleep(.4)
    print('You spin the slot machine')
    time.sleep(.4)
    dice1 = randint(0, 7)
    slot1 = dice1
    dice2 = randint(0, 7)
    slot2 = dice2
    dice3 = randint(0, 7)
    slot3 = dice3

    if slot1 == 0:
        slot1 = '🍒'
    elif slot1 == 1:
        slot1 = '🔔'
    elif slot1 == 2:
        slot1 = '💰'
    elif slot1 == 3:
        slot1 = '🍓'
    elif slot1 == 4:
        slot1 = '7'
    elif slot1 == 5:
        slot1 = '❤'
    elif slot1 == 6:
        slot1 = '👅'
    elif slot1 == 7:
        slot1 = '🥝'

    if slot3 == 0:
        slot3 = '🍒'
    elif slot3 == 1:
        slot3 = '🔔'
    elif slot3 == 2:
        slot3 = '💰'
    elif slot3 == 3:
        slot3 = '🍓'
    elif slot3 == 4:
        slot3 = '7'
    elif slot3 == 5:
        slot3 = '❤'
    elif slot3 == 6:
        slot3 = '👅'
    elif slot3 == 7:
        slot3 = '🥝'

    if slot2 == 0:
        slot2 = '🍒'
    elif slot2 == 1:
        slot2 = '🔔'
    elif slot2 == 2:
        slot2 = '💰'
    elif slot2 == 3:
        slot2 = '🍓'
    elif slot2 == 4:
        slot2 = '7'
    elif slot2 == 5:
        slot2 = '❤'
    elif slot2 == 6:
        slot2 = '👅'
    elif slot2 == 7:
        slot2 = '🥝'
    time.sleep(.3)
    print(slot1, slot2, slot3)
    time.sleep(.4)

    if dice1 == dice2 == dice3 :
        again = input('You hit a MEGA JACKPOT! Want to try again?(y/n)')
        money += 500
        if again == 'y' :
            slotgame()
    elif dice1 == dice2 or dice2 == dice3 or dice1 == dice3 :
        again = input('You WON! Want to try again?(y/n)')
        money += 25
        if again == 'y' :
            slotgame()
    else :
        again = input('You lost... Want to try again?(y/n)')
        money -= 10
        if again == 'y' :
            slotgame()
#FullSlot()
