def sphere(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total
    
if __name__ == "pso.sphere":
    sphere()
