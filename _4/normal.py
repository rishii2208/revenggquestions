# Function to calculate factorial
def factorial(n):
    """
    Computes the factorial of a given number n.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i  # Multiply all numbers from 2 to n
    return result

# Function for encoding
def encode(N, C):
    """
    Encodes the value by multiplying factorial(N) with a constant C and adding 5.
    """
    return factorial(N) * C + 5  # Compute factorial and multiply by C

# Function to convert a number to its binary representation
def to_binary(num):
    """
    Converts an integer to its binary representation as a string.
    """
    return bin(num)[2:]  # Remove the '0b' prefix

# Function to invert binary representation
def invert_binary(binary_str):
    """
    Inverts the binary representation: '0' becomes '1' and '1' becomes '0'.
    """
    return ''.join('1' if bit == '0' else '0' for bit in binary_str)

# Main function to run the encoder
if __name__ == "__main__":
    N = int(input("Enter an integer N: "))  # Take integer input N
    C = 2  # Fixed constant C
    encoded_value = encode(N, C)  # Compute encoded value
    binary_representation = to_binary(encoded_value)  # Convert to binary
    inverted_binary = invert_binary(binary_representation)  # Invert binary digits
    print(f"Inverted binary representation: {inverted_binary}")
