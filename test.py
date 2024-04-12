i = 1
list = set()
list_1 = set()
for n in range(0, 4):
    
    i += 1
    print(n)
    list_1.add(n)
    while True:
        list.add(n)
        if i >= 3:
            print("i")
        break
    
print("hhhhh", len(list))
print("hhhhh", len(list_1))