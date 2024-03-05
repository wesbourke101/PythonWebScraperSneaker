def parse_number_with_suffix(number_str):
    # Convert the string to uppercase for case insensitivity
    number_str_upper = number_str.upper()

    # Check if the string ends with 'K'
    if number_str_upper.endswith('K'):
        # Remove 'K' and convert the rest of the string to an integer
        return int(float(number_str_upper[:-1]) * 1000)
    # Check if the string ends with 'M'
    elif number_str_upper.endswith('M'):
        # Remove 'M' and convert the rest of the string to an integer
        return int(float(number_str_upper[:-1]) * 1000000)
    # Check if the string is a hyphen (or any other non-numeric value)
    elif not number_str_upper.isdigit():
        # Return 0 for non-numeric values
        return 0
    else:
        # If no suffix is found and the string is numeric, convert it to an integer directly
        return int(number_str)