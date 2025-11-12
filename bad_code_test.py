# bad_code_test.py

# TODO: Remove hardcoded values and fix naming
import os
import math

# This function violates multiple rules:
# - No docstring
# - Uses print() (should be disallowed)
# - Too long (>50 lines)
# - Bad naming convention (camelCase)
def CalculateArea(radius):
    print("Calculating area...")  # Violates disallow_print_statements
    if radius < 0:
        print("Invalid radius!")  # Violates again
        return None
    area = math.pi * radius * radius
    for i in range(60):  # Just to exceed line length rule
        area += 0  # Doing nothing useful
    return area


# Another function with no docstring
def logicIssue():
    result = eval("2+2")  # Violates disallow_eval_usage
    print(result)          # Violates disallow_print_statements
    return result


# JS-like debug call for violation testing (should be flagged conceptually)
def fakeConsole():
    console_log = "This mimics console.log"
    print(console_log)  # Violates print usage again


# Improper naming (camelCase instead of snake_case)
def doStuff():
    for i in range(5):
        print("Doing stuff...")  # Violates print again


# Large function to exceed max_function_length
def veryLargeFunction():
    value = 0
    for i in range(55):
        value += i
        print("Iteration:", i)  # Violates print rule
    return value


# debugger-like placeholder for violation testing
def debugFunction():
    # debugger statement simulation
    print("Debugger active")  # Violates print rule
    return "debug"

# Top-level code execution (should not exist)
print("This should not be here!")  # Violates print rule
result = CalculateArea(10)
print("Area result:", result)      # Violates print rule
