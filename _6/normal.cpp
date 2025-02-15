#include <bits/stdc++.h>
using namespace std;

const int N = 1000000; 
vector<int> primes;

// Function to generate prime numbers using the Sieve of Eratosthenes
void sieve() {
    vector<bool> isPrime(N + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i <= N; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
            for (int j = 2 * i; j <= N; j += i) {
                isPrime[j] = false;
            }
        }
    }
}

int main() {
    sieve(); 

    int x;
    cin >> x; 

    // Apply a non-linear transformation on x
    x = ((x * 7) + 13) % 100003;  // Modulo with a large prime
    x = abs((x * x * 3 + 5) % 50021);  // Another mod operation with a different prime

    // Introduce misleading dummy calculations
    int noise = ((x * 17) + (x / 2)) % 99991;  
    int index = (x + noise) % primes.size(); 

    // Mask the index before accessing the primes array
    index = (index ^ 54321) % primes.size(); 
    cout << primes[index] << endl;  

    return 0;
}
// What This Code Does:
// Transforms x in a non-linear way
// First multiplication and addition (x = ((x * 7) + 13) % 100003)
// Then squared, multiplied, and another modulus (x = abs((x * x * 3 + 5) % 50021))
// Adds misleading computations (noise)
// A calculated noise variable is added to x before index selection.
// Applies XOR masking (index = (index ^ 54321))
// This makes it harder to reverse-engineer the index lookup.
// Ensures the index remains within bounds (% primes.size())
// Prevents out-of-range errors while still being unpredictable.