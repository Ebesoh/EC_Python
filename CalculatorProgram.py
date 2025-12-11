def calculator (a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "%":
        return a % b
    if operator == "/":
        if b == 0:
            raise  ValueError("Cannot divide by zero")
        return a/b
    raise  ValueError(f"Unknow operator: {operator}")

print(calculator(5, 3, "+"))  # 8
print(calculator(10, 2, "/")) # 5.0
print(calculator(7, 4, "*"))  # 28