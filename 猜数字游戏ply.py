import random
secret=random.randint(1, 100)
guess=0
tries=0
print "AHOY!   I am the Dread pirate Pirate Roberts,and I have a secret!"
print"It is a number from 1 to 100. I will give you 6tryes."
while guess!=secret and tries<6:
    guess=input("what is yer guess?")
    if guess<secret:
        print "too low,ye scurvy dog!"
    elif guess>secret:
        print "too high, landlubber!"


    tries=tries+1
if guess==secret:
    print "Avast!Ye got it!Found my secret,ye did!"
else:
    print "No more guesses!Better Luck next time,matey!"
    print "the secret number was",secret
