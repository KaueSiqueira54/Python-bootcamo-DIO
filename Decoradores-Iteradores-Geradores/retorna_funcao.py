def calculadota(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mult(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mult
        case "/":
            return div

op = calculadota("+")(2, 2)
print(op)
op = calculadota("-")(6, 2)
print(op)
op = calculadota("*")(3, 5)
print(op)
op = calculadota("/")(10, 2)
print(op)
