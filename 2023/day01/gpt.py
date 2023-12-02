import re

def sum_calibration_values_part2(lines):
    word_to_digit = {
        'nine': '9', 'eight': '8', 'seven': '7', 'six': '6',
        'five': '5', 'four': '4', 'three': '3', 'two': '2', 'one': '1'
    }
    total_sum = 0

    for line in lines:
        # Find all spelled-out numbers with their start and end indices
        spelled_numbers = [(match.start(), match.end(), word_to_digit[match.group()])
                           for match in re.finditer('|'.join(word_to_digit.keys()), line)]

        processed_line = ''
        last_index = 0
        for start, end, digit in spelled_numbers:
            # Add unprocessed part of the line and the digit
            processed_line += line[last_index:start] + digit
            last_index = end

        # Add the remaining part of the line
        processed_line += line[last_index:]

        print(processed_line)

        # Extract first and last digit
        digits = [char for char in processed_line if char.isdigit()]
        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            total_sum += int(first_digit + last_digit)

    return total_sum

# Example usage
lines_part2 = [
    "two1nine", "eightwothree", "abcone2threexyz",
    "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"
]
print(sum_calibration_values_part2(lines_part2))
