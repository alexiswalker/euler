from constraint import *

problem = Problem()
constraint = lambda a, b, c: a+b+c == 14

for variable in range(ord('a'), ord('j')+1):
    problem.addVariables(chr(variable), range(1, 11))

problem.addConstraint(AllDifferentConstraint())
problem.addConstraint(AllDifferentConstraint())
problem.addConstraint(constraint, ('a','f','j'))
problem.addConstraint(constraint, ('f','g','b'))
problem.addConstraint(constraint, ('g','h','c'))
problem.addConstraint(constraint, ('h','i','d'))
problem.addConstraint(constraint, ('e','j','i'))

solution = problem.getSolutions()
for s in solution:
    print str(s['a'])+str(s['f'])+str(s['j'])
    print str(s['b'])+str(s['g'])+str(s['f'])
    print str(s['c'])+str(s['h'])+str(s['g'])
    print str(s['d'])+str(s['i'])+str(s['h'])
    print str(s['e'])+str(s['j'])+str(s['i'])
