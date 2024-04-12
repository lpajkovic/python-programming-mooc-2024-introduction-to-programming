# Write your solution here
def remove_smallest(numbers:list)->None:
    smallest=numbers[0]
    for num in numbers:
        if num<smallest:
            smallest=num
    numbers.remove(smallest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)