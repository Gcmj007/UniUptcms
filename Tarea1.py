class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def top(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)

def my_stack_function(arreglo):
    pilaA = Stack()
    pilaB = Stack()
    for num in arreglo:
        if pilaA.isEmpty() == True:
            pilaA.push(num)
        elif num > pilaA.top():
            pilaA.push(num)
        else:
            while pilaA.isEmpty() == False and num < pilaA.top():
                pilaB.push(pilaA.pop())
            pilaA.push(num)
            while pilaB.isEmpty() == False:
                pilaA.push(pilaB.pop())
				
    return pilaA.items

numeros = [15, 92, -15, 6, 10, -7, 1, 12, 56, -40]
print("Arreglo =", numeros)
print("Pila Ordenada =", my_stack_function(numeros))