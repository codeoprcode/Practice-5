
def diamond_plotter(n:int):
        
    shape= []

    for i in range(n):
        print((n-i-1)*" " + (2*i+1)*"✩")
        shape.append((n-i-1)*" " + (2*i+1)*"✩")

    for j in range(n-1,0,-1):
        print((n-j)*" " + (2*j-1)*"✩")

