#include <iostream>
#include <vector>
#include <string>

std::string zigzagDecode(const std::string& s, int numRows) {
    if (numRows == 1) return s;

    // Step 1: Calculate the number of characters per row
    std::vector<int> rowCounts(numRows, 0);
    int currentRow = 0;
    bool goingDown = false;
    for (size_t i = 0; i < s.size(); ++i) {
        rowCounts[currentRow]++;
        if (currentRow == 0 || currentRow == numRows - 1) {
            goingDown = !goingDown;
        }
        currentRow += goingDown ? 1 : -1;
    }

    // Step 2: Split the encoded string into rows based on counts
    std::vector<std::string> rows(numRows);
    int pos = 0;
    for (int row = 0; row < numRows; ++row) {
        if (rowCounts[row] > 0) {
            rows[row] = s.substr(pos, rowCounts[row]);
            pos += rowCounts[row];
        }
    }

    // Step 3: Rebuild the original string by traversing the ZigZag path
    std::string decoded;
    currentRow = 0;
    goingDown = false;
    std::vector<int> rowIndices(numRows, 0); // Track the current index in each row
    for (size_t i = 0; i < s.size(); ++i) {
        decoded += rows[currentRow][rowIndices[currentRow]++];
        if (currentRow == 0 || currentRow == numRows - 1) {
            goingDown = !goingDown;
        }
        currentRow += goingDown ? 1 : -1;
    }

    return decoded;
}

int main() {
    std::string encoded;
    int numRows;
    std::getline(std::cin, encoded);
    std::cin >> numRows;
    std::cout << zigzagDecode(encoded, numRows) << std::endl;
    return 0;
}