import numpy as np

def neville(x_points, y_points, x_val):
    n = len(x_points)
    P = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        P[i][0] = y_points[i]
    for j in range(1, n):
        for i in range(j, n):
            P[i][j] = ((x_val - x_points[i - j]) * P[i][j - 1] - (x_val - x_points[i]) * P[i - 1][j - 1]) / (x_points[i] - x_points[i - j])
    return P[n - 1][n - 1]

def newton_divided_differences(x, y):
    n = len(x)
    table = [y.copy()]
    for j in range(1, n):
        col = []
        for i in range(n - j):
            diff = (table[j - 1][i + 1] - table[j - 1][i]) / (x[i + j] - x[i])
            col.append(diff)
        table.append(col)

    coeff = [table[i][0] for i in range(n)]
    return coeff, table

def newton_polynomial(x_val, x_points, coeff, degree):
    result = 0.0
    product = 1.0
    for i in range(degree + 1):
        if i > 0:
            product *= (x_val - x_points[i - 1])
        result += coeff[i] * product
    return result

def hermite_divided_differences(x, f, fp):
    n = len(x)
    m = 2 * n
    z = [0.0] * m
    Q = [[0.0 for _ in range(m)] for _ in range(m)]
    for i in range(n):
        z[2 * i] = x[i]
        z[2 * i + 1] = x[i]
        Q[2 * i][0] = f[i]
        Q[2 * i + 1][0] = f[i]
        Q[2 * i + 1][1] = fp[i]
        if i != 0:
            Q[2 * i][1] = (Q[2 * i][0] - Q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])
    for i in range(2, m):
        for j in range(2, i + 1):
            Q[i][j] = (Q[i][j - 1] - Q[i - 1][j - 1]) / (z[i] - z[i - j])
    return z, Q

def cubic_spline_system(x, f):
    n = len(x)
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    A[0, 0] = 1.0
    A[n-1, n-1] = 1.0
    b[0] = 0.0
    b[n-1] = 0.0
    
    h = [x[i+1] - x[i] for i in range(n-1)]
    
    for i in range(1, n-1):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        b[i] = 6 * ((f[i+1] - f[i]) / h[i] - (f[i] - f[i-1]) / h[i-1])
    
    return A, b

def main():
    print("Question 1")
    x1 = [3.6, 3.8, 3.9]
    y1 = [1.675, 1.436, 1.318]
    x_val_neville = 3.7
    result_neville = neville(x1, y1, x_val_neville)
    print(result_neville)
    
    print("Question 2")
    x2 = [7.2, 7.4, 7.5, 7.6]
    y2 = [23.5492, 25.3913, 26.8224, 27.4589]
    x2_3 = x2[:3]
    y2_3 = y2[:3]
    coeff_2nd, _ = newton_divided_differences(x2_3, y2_3)
    for i, c in enumerate(coeff_2nd):
        print(c)
        print('\n')
    
    print("Question 3")
    coeff_full, _ = newton_divided_differences(x2, y2)
    x_eval = 7.3
    approx_val = newton_polynomial(x_eval, x2, coeff_full, 3)
    print(approx_val)
    
    print("Question 4")
    x4 = [3.6, 3.8, 3.9]
    f4 = [1.675, 1.436, 1.318]
    fp4 = [-1.195, -1.188, -1.182]
    z, Q = hermite_divided_differences(x4, f4, fp4)
    for i in range(6):
        row_items = []
        for j in range(5):
            if j <= i:
                row_items.append(f"{Q[i][j]:.6f}")
            else:
                row_items.append("0.000000")
        print("\t".join(row_items))
    
    print("Question 5")
    x5 = [2, 5, 8, 10]
    f5 = [3, 5, 7, 9]
    A, b = cubic_spline_system(x5, f5)
    print("Matrix A:")
    print(A)
    print("\nVector b:")
    print(b)
    x = np.linalg.solve(A, b)
    print("\nSolution vector (second derivatives at nodes):")
    print(x)
if __name__ == "__main__":
    main()