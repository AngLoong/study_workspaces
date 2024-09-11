def conflict(num, state):
        for tem in state:
            if num == tem:
                return True
        for tem in range(len(state)):
            if abs(state[tem] - num) == len(state) - tem:
                return True
        return False

def queens(num, state):
    print('in')
    for pos in range(num):
        if not conflict(pos,state):
            if len(state) == num -1:
                yield (pos, )
            else:
                for result in queens(num, state + (pos, )):
                    yield (pos, ) + result

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
            

if __name__ == '__main__':
    """
    print('this is a test for 8 queens')
    st = (2,4)
    aa = queens(4,st)
    bb = list(aa)
    print(bb)
    """
    aa = [[1,3],[2,4],[9]]
    bb = flatten(aa)
    for i in range(2):
        print(next(bb))
    cc = flatten(aa)
    print(next(bb))
    dd = list(flatten(aa))
    print(dd)

