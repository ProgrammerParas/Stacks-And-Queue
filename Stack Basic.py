stk = []
top = None
Dtop = None
def isEmpty(stk):
  if (len(stk) <= 0):
    print("Stack Is Empty")
  else:
    return False

def Push():
  item = int(input("Enter Item You Want To Push: "))
  stk.append(item)
  print("Pushed Successfully")

def Pop():
  if(isEmpty(stk)):
        return ("Underflow!")
  else:
    i = stk.pop()
def Display():
  if(isEmpty(stk)):
        print("Stack Is Empty")
  else:
    Dtop = len(stk)-1
    print(stk[Dtop], '<<<top')
    for i in range(len(stk)-1,-1,-1):
      print(stk[i])
def Peek():
  if (isEmpty(stk)):
        return ("Underflow!")
  else:
    top=len(stk)-1
    print(stk[top])

while True:
  print("STACK IMPLEMENTATION")
  print('[1]: PUSH')
  print('[2]: POP')
  print('[3]: PEEK')
  print('[4]: DISPLAY')
  print('[5]: EXIT')

  ch = input('Enter Your Choice: ')

  if ch == '1':
    Push()
  elif ch == '2':
    Pop()
  elif ch == '3':
    Peek()
  elif ch == '4':
    Display()
  else:
    print("Invalid Choice")
  
  