from constraint import *



problem = Problem()
constraint = lambda a, b, c: a+b+c == 14

for variable in range(ord('a'), ord('j')+1):
    problem.addVariables(chr(variable), range(1, 11))

problem.addConstraint(AllDifferentConstraint())
problem.addConstraint(constraint, ('a','f','j'))
problem.addConstraint(constraint, ('f','g','b'))
problem.addConstraint(constraint, ('g','h','c'))
problem.addConstraint(constraint, ('h','i','d'))
problem.addConstraint(constraint, ('e','j','i'))

solutions = problem.getSolutions()

l = []
for s in solutions:
    a = [int(str(s['a'])+str(s['f'])+str(s['j'])),
    int(str(s['b'])+str(s['g'])+str(s['f'])),
    int(str(s['c'])+str(s['h'])+str(s['g'])),
    int(str(s['d'])+str(s['i'])+str(s['h'])),
    int(str(s['e'])+str(s['j'])+str(s['i']))]

    #l.append(''.join([str(x) for x in a[a.index(max(a)):]+ a[:a.index(max(a))]]))
    l.append(''.join([str(x) for x in a]))

print l#max([int(x) for x in l])
#6531031914842725