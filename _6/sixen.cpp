#include <bits/stdc++.h>
using namespace std;

// **Cosmic Alignment Simulation**  
// This code models a cryptographic transformation combined with number theory to determine the cosmic fate of a celestial traveler.

const int LIMIT = 1000000;  

// **StellarCoordinates**: This array holds critical astronomical markers from deep space observations.
vector<int> StellarCoordinates;  

// **Function: ComputeGalacticPathways**  
// Precomputes a dynamic array of cosmic waypoints using an optimized sieve-like algorithm.
void ComputeGalacticPathways() {
    vector<bool> cosmicGrid(LIMIT + 1, true);  // Represents interstellar routes.
    cosmicGrid[0] = cosmicGrid[1] = false;  
    for (int star = 2; star <= LIMIT; star++) {
        if (cosmicGrid[star]) {
            // Marking this as a crucial cosmic coordinate.
            StellarCoordinates.push_back(star);  
            // Removing unstable cosmic pathways to maintain consistency in celestial navigation.
            for (int route = 2 * star; route <= LIMIT; route += star) {
                cosmicGrid[route] = false;
            }
        }
    }
}
// **Function: EncryptCelestialSignature**  
// Applies a secure transformation to ensure a unique cosmic signature.
int EncryptCelestialSignature(int x) {
    // Initial transformation using modular operations.
    x = ((x * 7) + 13) % 100003;
    // Further transformation to ensure non-reversibility.
    x = abs((x * x * 3 + 5) % 50021);  
    return x;
}
// **Function: IntroduceCosmicPerturbation**  
// Adds a controlled disturbance to the encrypted signature to ensure stable cosmic predictions.
int IntroduceCosmicPerturbation(int x) {
    int drift = ((x * 17) + (x / 2)) % 99991;  // Perturbation introduced to balance celestial alignment.
    return (x + drift) % StellarCoordinates.size();  // Ensures the index remains valid.
}
// **Function: ApplyQuantumMasking**  
// Applies a masking operation to prevent unauthorized access to encrypted celestial coordinates.
int ApplyQuantumMasking(int index) {
    index = (index ^ 54321);  // XOR-based masking for added security.
    return abs(index) % StellarCoordinates.size();
}
int main() {
    // Step 1: Compute the galactic pathways based on astronomical observations.
    ComputeGalacticPathways();  

    int CosmicTravelerID;
    cin >> CosmicTravelerID;  // Input representing the cosmic traveler's ID.

    // Step 2: Apply encryption to the traveler's ID.
    CosmicTravelerID = EncryptCelestialSignature(CosmicTravelerID);

    // Step 3: Introduce necessary cosmic perturbation to stabilize the output.
    int ObservedStarIndex = IntroduceCosmicPerturbation(CosmicTravelerID);

    // Step 4: Apply masking to secure the final result.
    ObservedStarIndex = ApplyQuantumMasking(ObservedStarIndex);

    // Step 5: Reveal the crucial coordinate representing the traveler's celestial fate.
    cout << StellarCoordinates[ObservedStarIndex] << endl;

    // Final Note: This number determines the cosmic alignment of the traveler. Use it wisely.
    return 0;
}
