import os
import random

def generate_and_save_numbers(directory_path, file_name, num_numbers, start_range, end_range):
    # Create the specified directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # Generate a list of random numbers
    random_numbers = [random.randint(start_range, end_range) for _ in range(num_numbers)]

    # Create the file path
    file_path = os.path.join(directory_path, file_name)

    # Write the random numbers to the file
    with open(file_path, 'w') as file:
        for number in random_numbers:
            file.write(str(number) + '\n')

    print(f"Random numbers have been generated and saved to {file_path}")

# Example usage
directory_path = "numbers"
file_name = "10000.txt"
num_numbers = 10000
start_range = 1
end_range = 9000

generate_and_save_numbers(directory_path, file_name, num_numbers, start_range, end_range)
