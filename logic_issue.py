def divide(a, b):
    return a / b

def calculate():
    value = divide(10, 0)  # ❌ Bug: division by zero
    print("Result:", value)

calculate()
