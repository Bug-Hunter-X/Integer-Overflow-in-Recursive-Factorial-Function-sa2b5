def function(x):
    if x == 0:
        return 0
    elif x > 0:
        return x * function(x - 1)
    else:
        return -x * function(-x - 1)