INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

def task():
    with open(INPUT_FILE, 'r') as file1, open(OUTPUT_FILE, 'w') as file2:
        for line in file1:
            file2.write(line.upper())

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for current_line in file:
            print(current_line, end="")
