algebraic_expression = input()

opening_stack = []

for x in range(len(algebraic_expression)):
    if algebraic_expression[x] == '(':
        opening_stack.append(x)
    elif algebraic_expression[x] == ')':
        print(algebraic_expression[opening_stack.pop():x + 1])
