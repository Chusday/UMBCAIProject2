import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

#Dylan Chu
#3/19/16
#CMSC 471
#Hill Climbing, Hill Climbing with restarts, and Simulated annealing

#the function to optimize
def z(x,y):
    r = np.sqrt(np.add(np.square(x),np.square(y)))
    z1 = np.divide(np.sin(np.square(x)+ 3 * np.square(y)),np.add(0.1,np.square(r)))
    z2 = np.add(np.square(x),5 * np.square(y)) * np.divide(np.exp(1-np.square(r)),2)
    z = z1 + z2
    return z

#optimize function f with hill climbing
def hill_climb(f,step_size, xmin, xmax, ymin, ymax):
    best = 999999
    best_coords= []
    pathX = []
    pathY = []
    pathZ = []
    xrange = np.arange(xmin,xmax+step_size,step_size)
    yrange = np.arange(ymin,ymax+step_size,step_size)
       
    for x in xrange:
        for y in yrange:
            z = f(x,y)
            if (z< best):
                best = z
                best_coords = [x,y]
                pathX.append(x)
                pathY.append(y)
                pathZ.append(z)
    
    return best, best_coords, pathX, pathY, pathZ

#optimize function f with hill climbing with random restarts
def hill_climb_random_restart(f,step_size, num_restarts, xmin, xmax, ymin, ymax): 
    best = 9999999
    best_coords= []
    pathX = []
    pathY = []
    pathZ = []
    restart_counter = 0
    r = 0
    x = xmin
    y = ymin
    #break out of the loops if we've maximized the amount of restarts
    while x <= xmax:
        while y <= ymax:
            z = f(x,y)
            if (z< best):
                best = z
                best_coords = [x,y]
                pathX.append(x)
                pathY.append(y)
                pathZ.append(z)
            #random generator to determine if we restart
            r = random.randint(1,200)
            if (r==1) and restart_counter<num_restarts:
                x = best_coords[0]
                y = best_coords[1]
                restart_counter += 1
            elif restart_counter == num_restarts:
                break
            else:
                y = y+ step_size
                
        if (r==1) and restart_counter<num_restarts:
            x = best_coords[0]
            y = best_coords[1]
            restart_counter += 1
        elif restart_counter == num_restarts:
            break
        else:
            x = x + step_size
            y = ymin
                                
    return best, best_coords, restart_counter, pathX, pathY, pathZ

#temperature function for simulated annealing
def temp(new, old, t):
    num = 1 + (np.exp((new-old)/t))
    num = 1/num
    return num

#optimize function f with simulated annealing
def simulated_annealing(f, step_size, max_temp, xmin, xmax, ymin, ymax):
    best = 999999
    best_coords= []
    pathX = []
    pathY = []
    pathZ = []
    prev = f(xmin,ymin)
    t = max_temp
    x = xmin
    y = ymin+step_size

    #loop while temperature is above 0
    while max_temp > 0.0001:
        z = f(x,y)
        if (z < best):
            best = z
            best_coords = [x,y]
            pathX.append(x)
            pathY.append(y)
            pathZ.append(z)
        #use the temperature to see if we accept a bad move
        elif (temp(z, best, max_temp) >= random.uniform(0.0,2.0)):
            pathX.append(x)
            pathY.append(y)
            pathZ.append(z)

        #cool the temperature
        max_temp = max_temp * 0.999
        prev = z
        y += step_size
        if y >= ymax:
            y = ymin
            x += step_size
        

    return best, best_coords, pathX, pathY, pathZ
    
    
    

def main():
    #do all three optimizations
    h, hc, pathX, pathY, pathZ = hill_climb(z, 0.05,-2.5,2.5,-2.5,2.5)
    h2, hc2, r2, pathX2, pathY2, pathZ2 = hill_climb_random_restart(z, 0.05,200, -2.5,2.5,-2.5,2.5)
    h3, hc3, pathX3, pathY3, pathZ3 = simulated_annealing(z,0.05, 10,-2.5,2.5,-2.5,2.5)

    #graph hill climbing
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = y = np.arange(-2.5, 2.5, 0.05)
    X, Y = np.meshgrid(x, y)
    zs = np.array([z(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)
    ax.plot_surface(X, Y, Z, color = 'w', linewidth = 0)
    ax.plot(pathX,pathY,pathZ, 'r')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    #graph hill climbing with random restarts
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111, projection='3d')
    ax2.plot_surface(X, Y, Z, color = 'w', linewidth = 0)
    ax2.plot(pathX2,pathY2,pathZ2,'g')
    ax2.set_xlabel('X Axis')
    ax2.set_ylabel('Y Axis')
    ax2.set_zlabel('Z Axis')


    #graph simulated annealing
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111, projection='3d')
    ax3.plot_surface(X, Y, Z, color = 'w', linewidth = 0)
    ax3.plot(pathX3,pathY3,pathZ3,'b')
    ax3.set_xlabel('X Axis')
    ax3.set_ylabel('Y Axis')
    ax3.set_zlabel('Z Axis')
    plt.show()
    
    #print the findings
    print("Hill climbing found the min to be: ", h, " at coordinates: ", hc)
    print("Hill climbing with random restarts found the min to be: ", h2, " at coordinates: ", hc2)
    print("Simulated annealing found the min to be: ", h3, " at coordinates: ", hc3)
    return 0

main()
