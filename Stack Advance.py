s = []
top = None

def isEmpty(stk):
    if(stk==[]):
        return True
    
    else:
        return False

def push(stk, item):
    stk.append(item)
    top = len(stk) - 1

def spop(stk):
    if(isEmpty(stk)):
        return ("Underflow!")
    else:
        i = stk.pop()
        print("Item Popped")
    return i
def peek(stk):
    if (isEmpty(stk)):
        return ("Underflow!")
    else:
        top=len(stk)-1
        return stk[top]
def display(stk):
    if(isEmpty(stk)):
        print("Stack Is Empty")
    else:
        top = len(stk)-1
        print(stk[top], '<<<top')
        for i in range(top-1,-1,-1):
            print(stk[i])


while True:
    print("STACK IMPLEMENTATION")
    print('[1]: PUSH')
    print('[2]: POP')
    print('[3]: PEEK')
    print('[4]: DISPLAY')
    print('[5]: QUIT')
    ch = input("Enter Your Choice>>> ")

    if ch == '1':
        item = int(input("Enter Item You Want To Push: "))
        push(s, item)
        print('%d, added succesfully')
    elif ch == '2':
        item = spop(s)
        if(item=="Underflow!"):
            print("Underflow Stack Is Empty")
        else:
            print('%d Item Popped'%item)
    elif ch == '3':
        item=peek(s)
        if(item=="Underflow!"):
            print("Underflow Stack Is Empty")
        else:
            print('%d Is At The Top'%item)
    elif ch == '4':
        display(s)
    elif ch == '5':
        break
    else:
        print("Invalid Choice")