#Liam Houghton x500
def left(e):
    return e[0]

def op(e):
    return e[1]

def right(e):
    return e[2]



def isInside(v, e):
    if v == e:
        return True
    else:
        if len(e) == 1:
            return False
        elif(isInside(v, left(e))):
            return True
        elif(isInside(v, right(e))):
            return True
        else:
            return False

def solve(v, e):
    if isInside(v, left(e)):
        return solving(v, e)
    elif isInside(v, right(e)):
        q = (right(e),) + (op(e),) + (left(e),)
        return solving(v, q)
    else:
        raise ValueError


def solving(v, e):
    if v == left(e):
        return e
    elif type(e) == tuple:
        if op(left(e)) == '+':
            return solvingAdd(v, e)
        elif op(left(e)) == '-':
            return solvingSub(v, e)
        elif op(left(e)) == '*':
            return solvingMul(v, e)
        elif op(left(e)) == '/':
            return solvingDiv(v, e)
    else:
        raise ValueError
    




    
def solvingAdd(v, e):
    a = left(left(e))
    b = right(left(e))
    c = right(e)
    if isInside(v, left(left(e))):
        s = (c, '-', b)
        q = a , '=', s
        return solving(v, q)
    else:
        s = (c, '-', a)
        q = b, '=', s
        return solving(v, q)

def solvingSub(v, e):
    a = left(left(e))
    b = right(left(e))
    c = right(e)
    if isInside(v, left(left(e))):
        s = (c, '+', b)
        q = a , '=', s
        return solving(v, q)
    else:
        s = (a, '-', c)
        q = b, '=', s
        return solving(v, q)

def solvingMul(v, e):
    a = left(left(e))
    b = right(left(e))
    c = right(e)
    if isInside(v, left(left(e))):
        s = (c, '/', b)
        q = a , '=', s
        return solving(v, q)
    else:
        s = (c, '/', a)
        q = b, '=', s
        return solving(v, q)
def solvingDiv(v, e):
    a = left(left(e))
    b = right(left(e))
    c = right(e)
    if isInside(v, left(left(e))):
        s = (c, '*', b)
        q = a , '=', s
        return solving(v, q)
    else:
        s = (a, '/', c)
        q = b, '=', s
        return solving(v, q)

    



        


print(isInside('x', 'x'))
print(isInside('x', 'y'))
print(isInside('x', ('x', '+', 'y')))
print(isInside('x', ('a', '+', 'b')))
print(isInside('+', ('a', '+', 'b')))
print(isInside('x', (('m', '*', 'x'),'+', 'b')))

print(solve('x', (('a', '+','x'), '=', 'c')))

print(solve('x', (('x', '+', 'b'), '=', 'c')))

print(solve('x', (('a', '-', 'x'), '=', 'c')))

print(solve('x', (('x', '-', 'b'), '=', 'c')))

print(solve('x', (('a', '*', 'x'), '=', 'c')))

print(solve('x', (('x', '*', 'b'), '=', 'c')))

print(solve('x', (('a', '/', 'x'), '=', 'c')))

print(solve('x', (('x', '/', 'b'), '=', 'c')))

print(solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))))

print(solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))))

print(solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))))

"""
True
False
True
False
False
True
('x', '=', ('c', '-', 'a'))
('x', '=', ('c', '-', 'b'))
('x', '=', ('a', '-', 'c'))
('x', '=', ('c', '+', 'b'))
('x', '=', ('c', '/', 'a'))
('x', '=', ('c', '/', 'b'))
('x', '=', ('a', '/', 'c'))
('x', '=', ('c', '*', 'b'))
('y', '=', (('m', '*', 'x'), '+', 'b'))
('x', '=', (('y', '-', 'b'), '/', 'm'))
('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e'))
"""