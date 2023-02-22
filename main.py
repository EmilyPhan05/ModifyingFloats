import random

arr = []

for i in range(17):
    num = random.randint(0, 100)
    decimal = random.randint(0, 10) / 10
    holdFloat = num + decimal
    arr.append(holdFloat)


def mean(arr):
    total = 0.0
    for i in range(len(arr)):
        added = arr[i]
        total += added

    answer = total / len(arr)
    return(answer)

def median(arr):
    arr2 = arr.copy()
    answer = 0

    if len(arr) % 2 != 0:
        i = 0
        while len(arr2) != 1:
            arr2.remove(max(arr2))
            arr2.remove(min(arr2))
            i += 1
        answer = arr2[0]

    else:
        i = 0
        while len(arr2) != 2:
            arr2.remove(max(arr2))
            arr2.remove(min(arr2))
            i += 1
        answer = (arr[0] + arr[1]) / 2


    return(answer)


def mode(arr):
    largestCount = arr.count(arr[0])
    largest = arr[0]

    for i in range(len(arr)):
        temp = arr.count(arr[i])
        if temp > largestCount:
            largestCount = temp
            largest = arr[i]

    if largestCount > 1:
        return largest
    else:
        return None


print(arr)
print(mean(arr))
print(median(arr))
print(mode(arr))
