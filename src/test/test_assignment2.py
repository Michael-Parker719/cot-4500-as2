import sys
import os

# Get the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import assignment2 using its package path
from main import assignment_2

class TestAssignment2():

    def test_neville(self):
        x_vals = [3.6, 3.8, 3.9]
        f_vals = [1.675, 1.436, 1.318]
        result = assignment_2.neville_interpolation(x_vals, f_vals, 3.7)
        print(result)
    def test_newton(self):
        x_vals = [7.2, 7.4, 7.5, 7.6]
        f_vals = [23.5492, 25.3913, 26.8224, 27.4589]
        table = assignment_2.divided_diff_table(x_vals, f_vals)
        result = assignment_2.newton_poly(x_vals, table, 7.3, 3)
        print(result)

    def test_hermite(self):
        x_vals = [3.6, 3.8, 3.9]
        f_vals = [1.675, 1.436, 1.318]
        df_vals = [-1.195, -1.188, -1.182]
        table = assignment_2.hermite_interpolation(x_vals, f_vals, df_vals)
        print(table)

    def test_cubic_spline(self):
        x_vals = [2, 5, 8, 10]
        f_vals = [3, 5, 7, 9]
        A, b, M = assignment_2.cubic_spline(x_vals, f_vals)
        print(A)
        print(b)
        print(M)

if __name__ == '__main__':
    test = TestAssignment2()
    test.test_neville()
    test.test_newton()
    test.test_hermite()
    test.test_cubic_spline()
