q = []

def isEmpty():
    if q == []:
        print("Empty Queue")
    else:
        Display()

def Enqueue(item):
    q.append(item)
    print("Element Inserted: ", item)

def Dequeue():
    if q == []:
        print("Empty Queue")
    else:
        print("Element Popped: ", q.pop(0))

def Peek():

    if q == []:
        print("Empty Queue")
    else:
        print('Frontend:', q[0])

def Display():
    if q == []:
        print("Empty Queue")
    else:
        for x in range(0, len(q)):
            print(q[x])

while True:
    print("QUEUE IMPLEMENTATION")
    print('[1]: Enqueue')
    print('[2]: Dequeue')
    print('[3]: Peek')
    print('[4]: Display')
    print('[5]: Exit')

    ch = input("Enter Your Choice: ")
    
    if ch == '1':
        en_item = input("Enter The Element You Want To Enqueue: ")
        Enqueue(en_item)
    if ch == '2':
        Dequeue()
    if ch == '3':
        Peek()
    if ch == '4':
        Display()
    if ch == '5':
        break

