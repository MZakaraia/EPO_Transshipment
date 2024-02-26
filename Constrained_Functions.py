def RosenbrockConstrained(x):
    if ((x[0] -1)**3 - x[1] + 1) <= 0 and (x[0] + x[1]-2) <= 0:
        return (1-x[0])**2 + 100 * (x[1] - x[0]**2)**2
    else:
        return float('Inf')