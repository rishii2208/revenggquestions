def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    primes = []
    num = 2
    while len(primes) < 26:  # Only need 26 primes for A-Z
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def prime_decode(encoded_text: str) -> str:
    primes = generate_primes()
    decoded = []
    for num in encoded_text.split():
        if num == '0':  # Non-alphabetic characters
            decoded.append(' ')
        else:
            num = int(num)
            if num in primes:
                index = primes.index(num)
                decoded.append(chr(index + ord('A')))
            else:
                decoded.append('?')  # Unknown prime
    return ''.join(decoded)

if __name__ == "__main__":
    encoded_input = input().strip()
    print(prime_decode(encoded_input))