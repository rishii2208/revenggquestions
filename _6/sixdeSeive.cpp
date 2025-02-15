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

// Function to decode the original x from the given output prime
int decode(int output_prime) {
    // Step 1: Find the prime number's index in the primes array
    auto it = find(primes.begin(), primes.end(), output_prime);
    if (it == primes.end()) {
        cerr << "Error: Prime not found in the list!" << endl;
        return -1;
    }
    int index = distance(primes.begin(), it);

    // Step 2: Reverse XOR operation
    index = (index ^ 54321) % primes.size();

    // Step 3: Reverse the noise addition
    int recovered_x = -1;
    for (int x = 0; x < 100003; x++) {  // Brute-force potential x values
        int noise = ((x * 17) + (x / 2)) % 99991;
        if ((x + noise) % primes.size() == index) {
            recovered_x = x;
            break;
        }
    }

    if (recovered_x == -1) {
        cerr << "Error: Unable to recover x." << endl;
        return -1;
    }

    // Step 4: Reverse the modular transformations
    for (int x = 0; x < 100003; x++) {
        if (((x * x * 3 + 5) % 50021) == recovered_x) {
            recovered_x = x;
            break;
        }
    }

    for (int x = 0; x < 100003; x++) {
        if (((x * 7) + 13) % 100003 == recovered_x) {
            return x;  // Final recovered value of original x
        }
    }

    cerr << "Error: Could not fully decode x." << endl;
    return -1;
}

int main() {
    sieve(); 

    int output_prime;
    cin >> output_prime;  // Enter the prime number obtained from the original program

    int original_x = decode(output_prime);
    if (original_x != -1) {
        cout << "Recovered x: " << original_x << endl;
    }

    return 0;
}
