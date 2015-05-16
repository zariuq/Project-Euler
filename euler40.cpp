#include <iostream>
#include <math.h>
#include <string>
#include <boost/range/irange.hpp>
using namespace boost;
using namespace std;

int main () {
    
    string champ = ".";
    int i = 1;
    // i goes to 185186.. damn
    // Could be calculated more intelligently, but... why bother? :p
    while (champ.length() < 1000001) {
        champ += std::to_string(i);
        i++;
    }
    
    int dprod = 1;
    for ( auto i : irange(1,7) ){
        int power = pow(10,i);
        dprod *= (champ[power] - '0'); 
        cout << "d" << std::to_string(power) << ": " << champ[power] << endl;
    }
    
    cout << dprod << endl;

    return 0;
}
