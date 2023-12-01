Advent of Code: Day 01

This is a Python script designed to read a file named "inputDay1.txt" and perform two different operations on the data within the file. The code is organized into functions to handle distinct tasks, and the main function orchestrates the execution of these tasks.
Functions
readFile(filename)

This function takes a filename as input, reads the content of the file, and returns a list of lines.
part1(lines)

This function calculates the sum of specific numbers found in each line of the input file. It uses regular expressions to extract numeric characters and then combines the first and last digits to form a two-digit number, which is added to the running sum.
part2(lines)

This function calculates the sum of numbers represented by the first and last occurrences of specific words (digits) in each line of the input file. It iterates through each character in the line, identifies the words representing digits, and forms a two-digit number using the index of the first and last occurrences of these words.
main()

The main function is responsible for executing the script. It reads the lines from the input file, prints the result of part1(lines) and part2(lines).
How to Use

	- Ensure that the input file "inputDay1.txt" is present in the same directory as the script.
	- Run the script, and it will display the results of both Part 1 and Part 2.


```python script_name.py```

Example Output

```part 1: 12345
part 2: 67890```

Replace script_name.py with the actual name of your Python script.

Note: The provided example output is for illustrative purposes and may not reflect the actual results of running the script with your input file.