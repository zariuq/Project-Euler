#include <iostream>
#include <math.h>
#include <string>
#include <array> // I got weird errors until I remembered to include this :x
using namespace std;

// Forgot to change bool -> int... -sigh-
// I should test how much slower this string conversion crap is than doing the modular arithmetic and division
// Computers are pretty optimized for that stuff... >__>
int sumofsquares(int n){
    std::string s = std::to_string(n);
    int sq = 0;
    for (std::string::iterator it = s.begin(); it != s.end(); ++it){
        sq = sq + pow(*it - '0',2);
    }
    return sq;
}

// don't call with 0
int chain(int n){
    while (n != 89 && n != 1){
        n = sumofsquares(n);
    }
    return n;
}

int main() {
    int count = 0;
    const int limit = 10000000;
    
    // As 9^2*7=567
    std::array<int,568> r;
    
    int temp;
    for (int i = 1; i < r.size(); i++){
        temp = chain(i);
        r[i] = temp;
        if (temp == 89)
            count++;
    }
    
    for (int i = 568; i < limit; i++)
        if (r[sumofsquares(i)] == 89)
            count++;
            
    // A bit faster than the brute-force below =]
    // A bit being an order of magnitude >_>;
    /*
    for (int i = 1; i <= limit; i++)
        if (chain(i) == 89)
            count++;
    */        
    cout << "There are " << count << " below " << limit << endl;
    
    return 0;
}
