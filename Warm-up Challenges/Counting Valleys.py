def countingValleys(steps, path):
    # Write your code here
    count = 0
    res = 0
    for i in path:
        if i == 'U':
            count += 1
        else:
            count -= 1
        if count == 0 and i == 'U':
            res += 1
    return res 
