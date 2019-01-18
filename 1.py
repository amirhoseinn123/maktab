language=["mhgjhf","jkgjhf","khvb","ghfjhg"]
m=map(len,language)
def is_even(num):
    if num%2==0:
        return True
    else:
        return False

def is_digit(num):
    if not(ord("0")<=ord(num)<=ord("9")):
        return False
    else:
        return True

l=[1,2,3,4,5,6,3,4,4,4,4,3,2,56,6,7,8,8,5]
filter(is_even,l)

l=["5","4","h"]
l2=filter(is_digit,l)
#print(list(l2))


def is_Prime(num):
    for i in range (2,num):
        if num%i==0:
            return False
    if num==1:
        return False
    else:
        return True
l=[1,2,3,4,5,6,3,4,4,4,4,3,2,56,6,7,8,8,5]

f=filter(is_Prime,l)



l=[[-3,11,12],[-11]]
m=map(sum,l)


l=[1,True,[1,2]]
#print(m)
m=map(":".join,str(l))
print(list(m))



def has_odd_index(m):
    a,b=m
    if a%2==0:
        return False
    else :
        return True
    
def get_value(m) :
    a,b=m
    return b


l=["A","B"]
m=list(enumerate(l))
print(m)
s=filter(has_odd_index,m)
a=map(get_value,s)
b=list(a)
print(b)


# second commit
print("hi")




















