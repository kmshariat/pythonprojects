#LIFO = Last In First Out
nodes =[]
n = int(input("How many nodes? "))
for i in range(n):
    nodes.append(float(input("Enter a node ")))
for j in range(n):
    print(nodes)
    del nodes[n-j-1]
