username="1234567890"
password="1"
name=raw_input("please enter your username:")
if name==username:
    word=raw_input("please enter your password:")
    if word==password:
        print"you have $1000000."
    else:
        print"please come here next time."
else:
    name=raw_input("please enter your username again:")
    if name==username:
        word=raw_input("please enter your password:")
        if word==password:
            print"you have $1000000."
        else:
            print"please come here next time."
    else:
        print"please come here next time."
    
    
