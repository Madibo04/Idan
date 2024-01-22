def roman_to_int(s):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for numeral in reversed(s):
        current_value = roman_numerals[numeral]
        
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        
        prev_value = current_value
    
    return result

# Example usage:
roman_numeral = "XX"
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}")
