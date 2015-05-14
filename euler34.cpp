#include <iostream>
#include <array>
#include <math.h>
#include <numeric>
#include <string>
using namespace std;

// From stack-overflow, though I was thinking I should store them... =D
unsigned int factorial(unsigned int n) {
    static const unsigned int table[] = {1, 1, 2, 6, 24, 120, 720,
        5040, 40320, 362880, 3628800, 39916800, 479001600};
    if (n >= sizeof table / sizeof *table) // if appropriate, omit test if NDEBUG
        throw "Range error";
    return table[n];
    }

bool isFactDigit (int a) {
    std::string s = std::to_string(a);
    int digsum = 0;
    for (const auto& d: s){
        digsum += factorial((d-'0'));
    }
    if (digsum == a)
        return true;
    return false;
}

int main () {
    
    cout << isFactDigit(145) << endl;
    cout << factorial(5) << endl;
    long long int sum = 0;
    for (int i = 3; i < 9999999; i++){ // not as rigorous a bound as it could be... :p
        if (isFactDigit(i)) {
            sum += i;
            cout << i << endl;
        }
    }
    
    cout << "DONE!" << endl;
    cout << "The sum is: " << sum << endl;
    
    return 0;
}
