import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf 


def alan(data_text_file):

    #fitting func
    def amissDublin(ex, a, b, c):
        return a*ex**2 + b*ex + c  #b + c*np.exp(a*ex)    #b + c*ex**a #b + a*np.log(c*ex)


    nl = sum(1 for _ in open(data_text_file))
    #print(nl)

    D = np.loadtxt(fname = data_text_file ,skiprows = 3, max_rows = nl-4 ,  delimiter = ',')
    t, x, v = D.T


    fit, covar = cf(amissDublin, x, v)#p0=[-293.57, 665.91, 67.181])
    print("\nFit params", fit)
    print("\n\nCovar", covar)

    #plt.figure()
    plt.plot(x, v, '.', label = data_text_file)
    plt.plot(x, amissDublin(x, fit[0], fit[1], fit[2]), 'g')
    plt.xlabel('x, m')
    plt.ylabel('Velocity, m/s')
    plt.title('Velocity vs Position')
    plt.grid()
    #plt.savefig(data_text_file + '.png')
    #plt.show()
    print(data_text_file + '.png')

#txt = 'Vx3.txt'

plt.figure()
for n in range (1, 5): 
    txt = 'Vx' + str(n) + '.txt'
    alan(txt)
    
plt.legend()
plt.grid()
plt.show()