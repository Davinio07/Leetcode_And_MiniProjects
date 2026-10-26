def FindingMaxLoop():
    scores = [45, 82, 19, 93, 71, 88]
    currentMax: int = 0
    for num in scores:
        if num > currentMax:
            currentMax = num
    return currentMax

print(FindingMaxLoop())