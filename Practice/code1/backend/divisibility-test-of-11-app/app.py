# Take a valid number input from the user
# Split the number into individual digits and store the digits in a list
# Separate the list of digits into odd position list and even position list
# Computes the sum of each list
# Find the difference of the sum of odd position and even position
# Use appropriate logic to make conclusion whether a number is divisible by 11 or not

# 1. Taking the input number, validating it and splitting it to individual digits.
while True:
    try:
        raw_input = input("Enter an integer number to test : ")
        number_input = int(raw_input)
        number = abs(number_input)
        original_number = f"{number_input:,}"

        digits_list = []
        while number > 0:
            digit = number % 10
            digits_list.insert(0, digit)
            number = (number - number % 10) // 10
        print("List of digits making the number = ", digits_list)
        print()

# 2. Extracting even position and odd position digits of the number
        even_position_digits = []
        odd_position_digits = []

        for i in range(len(digits_list)):
            if i % 2 == 0:
                even_position_digits.append(digits_list[i])
            else:
                odd_position_digits.append(digits_list[i])

        print("Even positions digits = ", even_position_digits, "and", "Odd positions digits = ", odd_position_digits)

# 3. Computing the sum of even and odd position digits
        sum_even_position = 0
        for digit in even_position_digits:
            sum_even_position = sum_even_position + digit
        print()

        sum_odd_position = 0
        for digit in odd_position_digits:
            sum_odd_position = sum_odd_position + digit

        print("Sum of digits in even positions = ", sum_even_position, "and Sum of digits in odd positions = ",
              sum_odd_position)
        print()

# 4. Logic to determine the divisibility of 11
        if sum_even_position > sum_odd_position:
            difference = sum_even_position - sum_odd_position

            print("Difference :", sum_even_position, "-", sum_odd_position, "=", difference)
            print()

        else:
            difference = sum_odd_position - sum_even_position

            print("Difference :", sum_odd_position, "-", sum_even_position, "=", difference)
            print()

        if difference == 0:
            print("Hence, number (", original_number,
                  ") is visible by 11 because the difference of "
                  "sum of digits in odd positions and even positions = ", difference)
            print()

        elif difference % 11 == 0:
            print("Hence number (", original_number,
                  ") is divisible by 11 because the difference of sum of digits in"
                  " odd positions and even positions (", difference, ")is a multiple of 11.")
            print()

        else:
            print("Hence number (", original_number,
                  ") is not divisible by 11 because the difference of sum of "
                  "digits in odd positions and even positions (", difference, ") is not a zero or a multiple of 11")
            print()

    except ValueError:
        print("The input (", raw_input, ") you entered is not a valid integer number. Please enter a valid integer "
                                        "number and try again.")
