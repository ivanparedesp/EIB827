import numpy as np
from scipy.optimize import linprog
from numpy.linalg import solve

#Aqui escribes el codigo a ejecutar
def miFuncion():

#aca se escribe el codigo a ejecutar
    A_eq = np.array([[1,1,1]])
    b_eq = np.array([999])

    A_ub = np.array([
    [1, 4, 8],
    [40,30,20],
    [3,2,4]])

    b_ub = np.array([4500, 36000,2700])

    c = np.array([70, 80, 85])

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub,
    bounds=(0, None))
    print('Optimal value:', res.fun, '\nX:', res.x)

# Aqui se ejecuta el codigo
if __name__ == "__main__":
    miFuncion()