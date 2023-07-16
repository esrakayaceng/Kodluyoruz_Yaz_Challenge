import random
def generate_random_numbers(size, min, max):
    array_index = random.sample(range(min, max + 1), size)
    return array_index

def find_combinations(numbers, target):
    combinations = []
    backtrack(numbers, target, 0, [], combinations)
    return combinations

def backtrack(numbers, target, start, path, combinations):
    if target == 0:
        combinations.append(path[:])
        return
    if target < 0:
        return
    for i in range(start, len(numbers)):
        path.append(numbers[i])
        backtrack(numbers, target - numbers[i], i, path, combinations)
        path.pop()

# Example usage
size = int(input("Enter the size of the array: "))
min = int(input("Enter the min value: "))
max = int(input("Enter the max value: "))


numbers = generate_random_numbers(size, min, max)
print("Random sequence:", numbers)

target_number = int(input("Enter target number:"))

target = target_number

result = find_combinations(numbers, target)
print(f"Combinations to reach {target}:")
for combination in result:
    print(combination)