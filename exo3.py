a  = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []

c = input("type the highest number")

for i in a:

    if i < int(c):
        b.append(i)
       
print(b)


