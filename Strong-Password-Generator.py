SYM = list("!/#$%&/'()*+,-./:;<=>?@[\]^_`{|}~")
LL = list("qwertyuiopasdfghjklzxcvbnm")
UP = list("QWERTYUIOPASDFGHJKLZXCVBNM")
NUM = list("0123456789")
characters = SYM + LL + UP + NUM

def rdmps(user_choice):
    import random
    password = random.sample(characters, user_choice)
    a = set(password) & set(SYM)
    b = set(password) & set(LL)
    c = set(password) & set(UP)
    d = set(password) & set(NUM)
    if (len(a) >= 2 and len(b) >= 2 and len(c) >= 2 and len(d) >= 2):
        print("Here is your random password: ",*password,sep="")
    else:
        return rdmps(user_choice)

def choice_checker(user_choice):
    if (user_choice >= 8):
        rdmps(user_choice)
    else:
        print("ERROR: Password too short - minimum length is 8 characters")

user_choice = int(input ("Please enter a password with at least 8 characters"))
choice_checker(user_choice)