try:
    with open('sample.txt', 'r') as file1:
        reading_sample = file1.read()
        print(reading_sample)
except FileNotFoundError:
    print("Error: This file 'sample.txt' was not found. ")


# Take user input and write to output.txt
user_input = input("Enter some text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')
    print("Data successfully written to output.txt. ")

# Append additional data
additional_input = input("Enter more text to append to the file: ")
with open('output.txt', 'a') as file:
    file.write(additional_input + '\n')
    print("Data successfully appended. ")

# Read and display final content
print("\nFinal content of output.txt:")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
