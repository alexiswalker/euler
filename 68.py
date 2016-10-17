from constraint import *

for i in range(1,50):
    problem = Problem()

    for variable in range(ord('a'), ord('j')+1):
        problem.addVariables(chr(variable), range(1, 11))
    problem.addConstraint(AllDifferentConstraint())

    problem.addConstraint(AllDifferentConstraint())

    constraint = lambda a, b, c: a+b+c == i

    problem.addConstraint(constraint, ('a','f','j'))
    problem.addConstraint(constraint, ('f','g','b'))
    problem.addConstraint(constraint, ('g','h','c'))
    problem.addConstraint(constraint, ('h','i','d'))
    problem.addConstraint(constraint, ('e','j','i'))

    if problem.getSolutions():
        print i