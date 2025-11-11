def process_numbers(numbers):
    total = 0
    for i in range(0, len(numbers)):
        total = total + numbers[i]
    avg = total / len(numbers)
    return avg

result = process_numbers([10, 20, 30, 40])
print("Average is:", result)
