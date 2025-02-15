# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Function for decoding
def decode(encoded_value, C):
    """ Decodes the encoded value back to N. """
    encoded_value -= 5
    fact = encoded_value // C
    N = 1
    while factorial(N) < fact:
        N += 1
    if factorial(N) == fact:
        return N
    return -1  # In case no valid N found

# Function to revert the inverted binary
def revert_inverted_binary(inverted_binary_str):
    """ Reverts the inversion: '1' becomes '0' and '0' becomes '1'. """
    return ''.join('1' if bit == '0' else '0' for bit in inverted_binary_str)

# Function to convert binary string to integer
def binary_to_integer(binary_str):
    """ Converts a binary string to its integer representation. """
    return int(binary_str, 2)

# Fixed constant C
C = 2

# Main function to run the decoder
if __name__ == "__main__":
    inverted_binary = input()  # Example: '00001010'
    
    # Step 1: Revert the inverted binary
    original_binary = revert_inverted_binary(inverted_binary)
    
    # Step 2: Convert the reverted binary back to an integer
    encoded_value = binary_to_integer(original_binary)
    
    # Step 3: Decode the integer to find N
    decoded_value = decode(encoded_value, C)
    
    # Output results
    print(decoded_value)
