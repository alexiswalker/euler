def letters():
    return { chr(i) : i-64 for i in range(65, 91)}

def names():
    f = open('C:\Users\Alexis\Desktop\p022_names.txt', 'r')
    names = f.read().replace('"', '')
    f.close()
    return sorted(names.split(','))

def position():
    n = names()
    return
     { n[i] : i+1 for i in range(len(n))}



l = letters()
p = position()

print sum([p[name] * sum([l[c] for c in name]) for name in names()])
    
       