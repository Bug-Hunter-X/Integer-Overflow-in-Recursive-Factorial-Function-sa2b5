def function(x):
    if x == 0:
        return 1
    elif x > 0:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
    else:
        result = 1
        for i in range(-1, x -1 , -1):
            result *= i
        return result