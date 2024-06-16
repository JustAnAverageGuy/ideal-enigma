#include <iostream>
#include <vector>
#include <unordered_set>

std::vector<int> f() {
    std::vector<int> hmm = {1, 1};
    std::unordered_set<int> p = {1};
    int a = 1;
    
    for (int i = 0; i < 1000000; ++i) {
        int n = 1;
        while (p.find(n * a) != p.end()) {
            ++n;
        }
        p.insert(n * a);
        a = n;
        hmm.push_back(n);
    }
    
    return hmm;
}

int main() {
    std::vector<int> result = f();
    
    // Print the first 10 elements of the result to verify the output
    for (int i = 0; i < 1000000; ++i) {
        std::cout << result[i] << " ";
    }   
    std::cout << std::endl;
    
    return 0;
}

