__author__ = 'cook'


inputstring = "Please enter a SS# number in the format SSS-SS-SSSS"
def validatessnumber(s):
    ssnum = input(s)
    return ssnum


def getssnumber(s):
    ss = validatessnumber(s)
    while ss is None:
        ss = validatessnumber(s)
    return ss

print(getssnumber(inputstring))
