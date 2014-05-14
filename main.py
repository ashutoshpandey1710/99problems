__author__ = 'ashutosh_pandey'

def lastOfAList(l):
    if len(l) == 1:
        return l[0]
    else:
        return lastOfAList(l[1:])

def lastButOne(l):
    if len(l) <= 1:
        return None
    if len(l) <= 2:
        return  l[0]
    else:
        return lastButOne(l[1:])

def findKthElement(l, k):
    if k == 1:
        return l[0]
    else:
        return findKthElement(l[1:], k - 1)

def getLength(l):
    if l == []:
        return 0
    else:
        return 1 + getLength(l[1:])

def reverse(l):
    if len(l) <= 1:
        return l
    else:
        car = l[0]
        cdr = l[1:]
        return (reverse(cdr) + [car])

# (a, a, a, b, b, b, b, c, c, c, c)
def palindrome(l):
    start = 0
    end = len(l) - 1
    while start < end:
        if l[start] != l[end]:
            return False
        start += 1
        end -= 1
    return True

def flatten(l):
    result = []
    for item in l:
        if type(item) is list:
            result += flatten(item)
        else:
            result.append(item)
    return result

def eliminateConsecutive(l):
    if len(l) <= 1:
        return l
    else:
        # print l
        car = l[0]
        cdr = l[1:]

        rest = eliminateConsecutive(cdr)
        if car == rest[0]:
            return rest
        else:
            return ([car] + rest)

def packConsecutives(l):
    if len(l) == 1:
        return [l]
    else:
        print l
        first = l[0]
        rest = packConsecutives(l[1:])

        if first == rest[0][0]:
            rest[0].append(first)
            return rest
        else:
            return [[first]] + rest

def runLength(l):
    if len(l) == 1:
        return [[l[0], 1]]
    else:
        car = l[0]
        cdr = l[1:]

        rest = runLength(cdr)
        if car == rest[0][0]:
            rest[0][1] += 1
            return rest
        else:
            return [[car, 1]] + rest

def expand(ch, count):
    if count <= 1:
        return [ch]
    else:
        return [ch] + expand(ch, count - 1)

def decode(l):
    return map(lambda x: expand(x[0], x[1]), l)

def replicate(l, n, original):
    print l
    if l == []:
        return []

    car = l[0]
    rest = None
    if n == 1:
        rest = replicate(l[1:], original, original)
    else:
        rest = replicate(l, n - 1, original)
    return ([car] + rest)

def dropEveryN(l, N):
    pass




if __name__ == '__main__':
    print dropEveryN([1, 2, 3, 4, 5], 3)

