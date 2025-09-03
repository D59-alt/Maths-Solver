from sympy import symbols, Eq, solve, sympify, pi, E, sqrt

def read_problems(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def solve_equation(eq_str):
    try:
        # Define symbols: x and e (variable), pi and E (constants)
        x, e = symbols('x e')  # lowercase 'e' is variable, uppercase 'E' is Euler's number
        if '=' in eq_str:
            lhs, rhs = eq_str.split('=')
            equation = Eq(sympify(lhs), sympify(rhs))
            solution = solve(equation)
            return f"{eq_str} -> Solution: {solution}"
        else:
            result = sympify(eq_str)
            return f"{eq_str} -> Result: {result}"
    except Exception as err:
        return f"{eq_str} -> Error: {err}"

def txt_math_solver(file_path):
    problems = read_problems(file_path)
    for eq in problems:
        print(solve_equation(eq))

# Run the engine
if __name__ == "__main__":
    txt_math_solver(r"C:\Users\divra\Onedrive\School Sabotage\math\equations.txt")  # Replace with your actual file path
