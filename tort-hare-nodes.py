class Node(object):
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

class LinkedList:
    def __init__(self):
        self.cur_node = None
        self.head = None

    def add_node(self, data):
        new_node = Node() # create a new node
        new_node.data = data
        if self.head == None: 
            self.head = new_node
            self.cur_node = self.head
        else:
            self.cur_node.next = new_node
            self.cur_node = new_node

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print (node.data)
            node = node.next



ll = LinkedList()
for i in range(0,18):
    ll.add_node(i)

ll.cur_node.next = ll.head

# Set up the Race
hare = ll.head
meet_count = 0
tortoise = ll.head

def t_step(tortoise):
    for i in [0,1]:
        tortoise = tortoise.next
    print('T:' + str(tortoise.data))
    return tortoise

def h_step(hare):
    for i in range(0,9): 
        hare = hare.next
        if hare.data == tortoise.data:
            print('Met at' + str(hare.data))
            global meet_count 
            meet_count = meet_count + 1
    print('H:' + str(hare.data))
    return hare

flag = False
for i in range(1,19):
    tortoise = t_step(tortoise)
    if tortoise.data > 12: 
        flag = True
    if flag:
        hare = h_step(hare)
    print('Time: ' + str(i*5)) 
    print('=================')
    
print (meet_count)
