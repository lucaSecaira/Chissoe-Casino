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
