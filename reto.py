class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, he):
        self.he = he
    def length(self):
        current = self.he
        if current is not None:
            count = 1
            while current.next is not None:
                count += 1
                current = current.next
            return count
        else:
            return 0
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = head.he
            head.he = new_node
        else:
            current = head.he
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node

    def Rotar(self,k):
        if k >= self.length():
            k=k%self.length()

        j = 1
        while j <= k:
            current = self.he
            while current.next.next is not None:
                current = current.next
            current.next.next = self.he
            self.he = current.next
            current.next = None
            j+=1

    def Lista(self):
        current = head.he
        while current is not None:
            print(current.data, end = '')
            current = current.next
            print()
head = SinglyLinkedList(Node(1))
for j in range (2,6):
    head.insert(j,j-1)

print('Lista inicial: ')
head.Lista()
head.Rotar(27)            #---> Número de veces a rotar
print("Lista después de ser rotada: ")
head.Lista()