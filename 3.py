username="123456789"
password="12345"
word1=raw_input("please enter your username:")
if word1==username:
    word2=raw_input("please enter your password:")
else:
    word1=raw_input("please enter your username again:")
    if word1==username:
        word2=raw_input("please enter your password:")
    else:
        print "your username is wrong ,please come here at next time!"
if word2==password:
    print "you have $10000."
else:
    print "it is wrong."
