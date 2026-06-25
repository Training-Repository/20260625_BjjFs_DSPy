# Expression Conversion
# Infix to Posfix

def infix_to_postfix(tokens):
    prec = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    output, ops = [], []          # output list + operator stack
    for tok in tokens:
        if tok in prec:                                   # an operator
            while ops and ops[-1] != "(" and prec.get(ops[-1], 0) >= prec[tok]:
                output.append(ops.pop())                  # pop higher/equal precedence
            ops.append(tok)
        elif tok == "(":
            ops.append(tok)
        elif tok == ")":
            while ops and ops[-1] != "(":
                output.append(ops.pop())
            ops.pop()                                     # discard the "("
        else:                                             # an operand
            output.append(tok)
    while ops:
        output.append(ops.pop())
    return output

# "principal + rate * years"  ->  operands and operators as tokens
expr = ["principal", "+", "rate", "*", "years"]
print("infix  :", " ".join(expr))
print("postfix:", " ".join(infix_to_postfix(expr)))

expr2 = ["(", "principal", "+", "rate", ")", "*", "years"]
print("\ninfix  :", " ".join(expr2))
print("postfix:", " ".join(infix_to_postfix(expr2)))