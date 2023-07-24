def generate_equations(equation):
    if len(equation) == 1:
        return [equation]
    equations = []
    for i in range(1, len(equation), 2):
        left = generate_equations(equation[:i])
        right = generate_equations(equation[i+1:])
        for l in left:
            for r in right:
                equations.append('{}{}{}'.format(l, equation[i], r))
    return equations

equation = '5*3/7-3'
equations = generate_equations(equation)
print(equations)
