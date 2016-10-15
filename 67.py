
f = open('p067_triangle.txt', 'r')
file = f.readlines()
f.close()
data = [i.split(' ') for i in file]

position = data.__len__() - 1

while position != 0:
    position -=1
    for i, n in enumerate(data[position]):
        data[position][i] = max(int(n) + int(data[position+1][i]),int(n) + int(data[position+1][i+1]))


print data[position]
