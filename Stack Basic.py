s = []
def isEmpty():
    if s == []:
        print("Stack Is Empty")
    else:
        Display()
def Push(item):
    s.append(item)
    print("Element Pushed: ", item)
def Pop():
    if s == []:
        print("Underflow!")
    else:
        print("Element Popped Out: ", s.pop())
def Peek():
    if s == []:
        print("Empty Stack")
    else:
        print("Top Is:", s[len(s)-1])
def Display():
    if s == []:
        print("Stack Is Empty")
    else:
        for x in range(len(s)-1,-1,-1):
            print(s[x])

while True:
    print('STACK IMPLEMENTATION')
    print('[1]: PUSH')
    print('[2]: POP')
    print('[3]: PEEK')
    print('[4]: DISPLAY')
    print('[5]: EXIT')

    ch = input("Enter Your Choice: ")
    if ch == '1':
        push_element = input("Enter Element: ")
        Push(push_element)
    elif ch == '2':
        Pop()
    elif ch == '3':
        Peek()
    elif ch == '4':
        Display()
    elif ch == '5':
        break
    else:
        print("Invalid Choice")
