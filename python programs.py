
#Program 1: Write a program to implement Abstract Data type(ADT)

def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print("pushed item: "+ item)

def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"

    return stack.pop()
stack=create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
print("popped item: "+pop(stack))
print("stack after popping an element:" + str(stack))


#Program 3: implement doubly linked list with insertion,deletion traversal opertations.

class Node:
    def __init__(self, data):  
        self.item = data
        self.next = None
        self.prev = None

class DoublyLinkedList:  # Corrected class name
    def __init__(self):  # Corrected __init__ method
        self.start_node = None

    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is not empty")

    def InsertToEnd(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def DeleteAtStart(self):
        if self.start_node is None:
            print("The linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    def DeleteAtEnd(self):
        if self.start_node is None:
            print("The linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
        n.prev = None

    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is:", n.item)
                n = n.next


NewDoublyLinkedList = DoublyLinkedList()
NewDoublyLinkedList.InsertToEmptyList(10)
NewDoublyLinkedList.InsertToEnd(20)
NewDoublyLinkedList.InsertToEnd(30)
NewDoublyLinkedList.InsertToEnd(40)
NewDoublyLinkedList.InsertToEnd(50)
NewDoublyLinkedList.InsertToEnd(60)

NewDoublyLinkedList.Display()


#program 4 :- Write a program to implement stack with intertion, deletion,travensal operation.

def create_stack():
    stack=[]
    return stack

def check_empty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print("pushed items:"+ item)

def pop(stack):
    if(check_empty(stack)):
        return"stack is empty"
    return stack.pop( )

stack=create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
print("popped item:" +pop(stack))
print ("stack after popped an elements: "+str(stack))


#Program 5:- Write a program to implement queue with insertion,deletion,traversal operations.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element:")

q.display()


#progrm 6:- write a program to implement priority queue with insertion, deletion, traversal operations.

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # Corrected '1' to 'l'
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]

    array.pop()  # Corrected the element removal

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array:", arr)

deleteNode(arr, 4)
print("After deleting an element:", arr)


#program 7: write a program to implement binary tree with insertion,deletion,traversal operations.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Preorder Traversal:", end=' ')
root.traversePreOrder()

print("\nInorder Traversal:", end=' ')
root.traverseInOrder()

print("\nPostorder Traversal:", end=' ')
root.traversePostOrder()


#program 8:- write a program to implement Huffman coding.

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def huffman_code_tree(node, left=True, binString=""):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

# Frequency calculation
string = 'BCAADDDCCACACAC'
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

# Sort frequency in ascending order
freq = sorted(freq.items(), key=lambda x: x[1], reverse=False)

# Build the Huffman Tree
nodes = freq
while len(nodes) > 1:
    (key1, c1) = nodes[0]
    (key2, c2) = nodes[1]
    node = NodeTree(key1, key2)
    nodes = nodes[2:]  # Remove the two lowest frequency nodes
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=False)

# Generate Huffman Codes
huffmanCode = huffman_code_tree(nodes[0][0])

# Display Results
print('Char | Huffman code')
print('------------------')
for (char, frequency) in freq:
    print('%-4r | %12s' % (char, huffmanCode[char]))


#program 9- write a program to implement graph with insertion, deletion, traversal operations
from collections import defaultdict

graph = defaultdict(list)

def addEdge(graph, u, v):
    graph[u].append(v)


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges  


addEdge(graph, 'a', 'c')
addEdge(graph, 'b', 'c')
addEdge(graph, 'b', 'e')
addEdge(graph, 'c', 'd')
addEdge(graph, 'c', 'e')
addEdge(graph, 'c', 'a')
addEdge(graph, 'c', 'b')
addEdge(graph, 'e', 'b')
addEdge(graph, 'd', 'c')
addEdge(graph, 'e', 'c')

print(generate_edges(graph))


#program 10- write a program to implement Travelling Salesman Problem
from sys import maxsize
from itertools import permutations
V = 4
def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_path_weight = 0
        k = s
        for j in i:
            current_path_weight += graph[k][j]
            k = j
        current_path_weight += graph[k][s]   
        min_path = min(min_path, current_path_weight)   
    return min_path
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

s = 0

result = travellingSalesmanProblem(graph, s)
print("The minimum cost of the Hamiltonian Cycle is:", result)


#pratical 11- write a program to create basic hash table for inserton, deletion, traversaal operations

hashTable = [[] for _ in range(10)]


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True


def getPrime(n):
    if n % 2 == 0:
        n += 1
    while not checkPrime(n):
        n += 2
    return n

def hashFunction(key):
    capacity = getPrime(10)  
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index].append([key, data])


def removeData(key):
    index = hashFunction(key)
    for i, pair in enumerate(hashTable[index]):
        if pair[0] == key:
            del hashTable[index][i]
            return
    print(f"Key {key} not found.")


insertData(123, "C")
insertData(432, "Python")
insertData(213, "JAVA")
insertData(654, "C++")

for i, bucket in enumerate(hashTable):
    print(f"Index {i}: {bucket}")


#pratical 12- write a program to create hash table to handle collisions using overflow chaining.

# Function to display the hash table
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(f"Index {i}:", end=" ")  # Label each index
        for j in hashTable[i]:
            print(f"--> {j}", end=" ")  # Print the values in the bucket
        print()  # New line for each index

# Creating a hash table as a nested list
HashTable = [[] for _ in range(10)]

# Hashing Function to return a key for every value
def Hashing(keyvalue):
    return keyvalue % len(HashTable)

# Insert Function to add values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)  # Get the hash key
    Hashtable[hash_key].append(value)  # Insert the value into the appropriate bucket

# Driver Code
insert(HashTable, 11, 'JAVA')  # Inserting 'JAVA'
insert(HashTable, 3, 'PYTHON')
insert(HashTable, 10, 'C')
insert(HashTable, 9, 'C++')
insert(HashTable, 21, 'JAVASCRIPT')
insert(HashTable, 20, 'HTML')
insert(HashTable, 4, 'PHP')

# Display the hash table
display_hash(HashTable)
