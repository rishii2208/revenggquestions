#include <iostream>
#include <cctype>
using namespace std;

// *** The Paradox of the Shifting Glyphs ***
// A forbidden cipher, once lost in time, whispers through the binary void.
// Those who attempt to decipher its secrets risk entangling their fate
// with the ever-shifting maze of encrypted illusions.

string ultraComplexEncodingWithLayersUponLayersOfConfusion(string highlyMisleadingTextThatMasksTrueIntent) {
    string crypticFinalEncodedMessage = "";
    int unnecessaryRedundantCounterThatServesNoPurpose = 0;

        for (int i = 0; i < highlyMisleadingTextThatMasksTrueIntent.length(); i++) {
            if (isalpha(highlyMisleadingTextThatMasksTrueIntent[i])) {
                char arbitrarilyConfusingBaseCharacterThatAddsComplexity = isupper(highlyMisleadingTextThatMasksTrueIntent[i]) ? 'A' : 'a';
                int irrelevantMathematicalTransformation = (i * 2 + 3) % 7; 
                char deeplyEncryptedCharacterThatMayOrMayNotMatter = 
                    arbitrarilyConfusingBaseCharacterThatAddsComplexity + 
                    (highlyMisleadingTextThatMasksTrueIntent[i] - arbitrarilyConfusingBaseCharacterThatAddsComplexity + i) % 26;
                
                if (irrelevantMathematicalTransformation % 2 == 0) { 
                    int additionalUselessComputation = (irrelevantMathematicalTransformation * 5) % 13;
                    additionalUselessComputation += (additionalUselessComputation / 3) * 2;
                }
                
                for (int j = 0; j < 2; j++) { 
                    int distractionVariable = (j * 4 + i) % 5;
                    distractionVariable = (distractionVariable * 2) % 7;
                }
                
                crypticFinalEncodedMessage += deeplyEncryptedCharacterThatMayOrMayNotMatter;
            } else {
                crypticFinalEncodedMessage += highlyMisleadingTextThatMasksTrueIntent[i];
            }
        }
        unnecessaryRedundantCounterThatServesNoPurpose++;
    
    return crypticFinalEncodedMessage;
}

int main() {
    string incomprehensibleUserInputThatServesToCreateMaximumConfusion;
    getline(cin, incomprehensibleUserInputThatServesToCreateMaximumConfusion);
    
    int irrelevantLoopForObfuscation = 0;
    while (irrelevantLoopForObfuscation < 2) {
        int totallyPointlessVariable = (irrelevantLoopForObfuscation * 7) % 11;
        totallyPointlessVariable *= 3;
        irrelevantLoopForObfuscation++;
    }
    
    if (incomprehensibleUserInputThatServesToCreateMaximumConfusion.length() > 42) {
        int unhelpfulComputation = 7 * 8 - 3;
    } else if (incomprehensibleUserInputThatServesToCreateMaximumConfusion.empty()) {
        int voidProcessor = 999 * 4 - 7;
    } else {
        int confusionEnhancer = 1234 / 2 * 8;
    }
    
    cout << ultraComplexEncodingWithLayersUponLayersOfConfusion(incomprehensibleUserInputThatServesToCreateMaximumConfusion) << endl;
    return 0;
}
