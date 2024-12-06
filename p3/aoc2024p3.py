


def is_safe(numbers):
    increasing = False
    decreasing = False

    for i in range(1, len(numbers)):
        diff = abs(numbers[i] - numbers[i - 1])

        # Check for invalid differences
        if diff < 1 or diff > 3:
            return False

        # Update increasing and decreasing trends
        if numbers[i] > numbers[i - 1]:
            increasing = True
        elif numbers[i] < numbers[i - 1]:
            decreasing = True

        # Check for conflicting trends
        if (numbers[i] > numbers[i - 1] and decreasing) or (numbers[i] < numbers[i - 1] and increasing):
            return False

    return True



with open('p3/data.txt', 'r') as file:
    safe_reports = 0

    for line in file:
        numbers = list(map(int, line.split()))
        if is_safe(numbers):
            safe_reports += 1

print(safe_reports)