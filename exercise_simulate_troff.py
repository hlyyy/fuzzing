import string

def check_1(inp):
    i = inp.find("\\D")
    if i >= 0 and i < len(inp):
        assert inp[i+2] in string.printable
           

def check_2(inp):
    for i in range(len(inp)-1):
        if ord(inp[i]) > 127:
            assert inp[i+1] != "\n"
        
    
def check_3(inp):
    assert inp != ".\n"
    

def f(s):
    check_1(s)
    check_2(s)
    check_3(s)
    return

#check_1("abcd\D\0")
#check_2("&%$ù\n")
#check_3(".\n")

#f("abcd\D\0")
#f("&%$ù\n")
#f(".\n")