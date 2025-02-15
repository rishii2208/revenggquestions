# Function to check if a number is prime
def is_prime(n: int) -> bool:
    """
    Returns True if n is a prime number, otherwise False.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Function to generate the first 26 prime numbers (for A-Z)
def generate_primes():
    """
    Generates the first 26 prime numbers and returns them as a list.
    """
    primes = []
    num = 2  # Start checking from 2
    while len(primes) < 26:  # Need exactly 26 primes
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Function to encode text using prime numbers
def prime_encode(text: str) -> str:
    """
    Encodes each alphabetic character (A-Z) to its corresponding prime number.
    Non-alphabetic characters are mapped to '0'.
    """
    primes = generate_primes()  # Get the first 26 primes
    encoded = []
    
    for char in text.upper():  # Convert text to uppercase for uniformity
        if char.isalpha():
            index = ord(char) - ord('A')  # Map A=0, B=1, ..., Z=25
            encoded.append(str(primes[index]))  # Use corresponding prime
        else:
            encoded.append('0')  # Non-alphabetic characters get '0'
    
    return ' '.join(encoded)  # Return space-separated encoded values

if __name__ == "__main__":
    input_text = input().strip()  # Read input and remove extra spaces
    print(prime_encode(input_text))  # Print encoded output
