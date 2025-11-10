def add_numbers(a, b):
    return a + b

def main():
    result = add_numbers(100, 200)
    result = add_numbers("10", 20)  # wrong type
    print("The result is:", result)
    print("This is a new update")
    print("Updated by Rohit for testing CodeRabbit")


if __name__ == "__main__":
    main()
