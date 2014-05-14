import random

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

def dropEveryN(l, N, original):
    if l == []:
        return []
    if N == 1:
        return dropEveryN(l[1:], original, original)
    else:
        car = l[0]
        rest = dropEveryN(l[1:], N - 1, original)
        return [car] + rest

def splitParts(l, length):
    if l == []:
        return []

    if length == 1:
        return [[l[0]], l[1:]]
    else:
        car = l[0]
        rest = splitParts(l[1:], length - 1)
        rest[0] = [car] + rest[0]
        return rest


def slice(l, start, end):
    if l == []:
        return []
    if end == 1:
        return [l[0]]
    else:
        if start > 1:
            return slice(l[1:], start - 1, end - 1)
        elif start <= 1:
            car = l[0]
            rest = slice(l[1:], start - 1, end - 1)
            return [car] + rest


def rotateLeft(l, N):
    return flatten(reverse(splitParts(l, N)))

def removeKth(l, k):
    if l == []:
        return []
    if k == 1:
        return l[1:]
    else:
        car = l[0]
        return [car] + removeKth(l[1:], k - 1)

def insertAt(l, k, item):
    if l == []:
        return []
    if k == 1:
        return [item] + l
    else:
        car = l[0]
        return [car] + insertAt(l[1:], k - 1, item)

def inclusiveRange(start, end):
    if start >= end:
        return [start]
    else:
        return [start] + inclusiveRange(start + 1, end)

def selectNRandom(l, N):
    if l == []:
        return []

    index = random.randint(1, len(l))
    if N == 1:
        return [ l[index - 1] ]
    else:
        elem = l[index - 1]
        return [elem] + selectNRandom(removeKth(l, index), N - 1)

def lottoSelect(N, M):
    return selectNRandom(inclusiveRange(1, M), N)

def randomPermutation(l):
    return selectNRandom(l, len(l))

def combinations(l, n):
    if l == []:
        return []
    if n == 1:
        return [[x] for x in l]
    else:
        car = l[0]
        withoutcar = combinations(l[1:], n)
        withcar = combinations(l[1:], n - 1)

        return withoutcar + [[car] + x for x in withcar]





if __name__ == '__main__':
    print combinations([1, 2, 3], 2)
    # print lottoSelect(6, 500)

