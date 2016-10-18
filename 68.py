from constraint import *

class Gon:
    def __init__(self, solution):
        self.solution = solution

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
s = solutions[0]

a = [int(str(s['a'])+str(s['f'])+str(s['j'])),
int(str(s['b'])+str(s['g'])+str(s['f'])),
int(str(s['c'])+str(s['h'])+str(s['g'])),
int(str(s['d'])+str(s['i'])+str(s['h'])),
int(str(s['e'])+str(s['j'])+str(s['i']))]

print a,  a[a.index(max(a)):]+ a[:a.index(max(a))]