class node(object):
    def __init__(self, data):
        self.info = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def addbeg(self):
        x = int(input("Enter a number"))
        pnew = node(x)
        if self.head is None:
            self.head = pnew
            print(self.head)
        else:
            pnew.next = self.head
            self.head = pnew
            print(self.head)

    def displaylist(self):
        current_node = self.head
        while(current_node):
            print(current_node.info)
            current_node = current_node.next

l = linkedlist()
for x in range(2):
    l.addbeg()
    l.displaylist()