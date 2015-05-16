#include <iostream>
#include <array>
#include <math.h>
#include <numeric>
#include <string>
#include <boost/range/irange.hpp>
using namespace boost;
using namespace std;

int main () {
    
    int maxP = 0;
    int maxS = 0;
    
    for (auto p : irange(2,1002,2)){
        int s = 0;
        for (auto c : irange(1,p)){
            for (auto b : irange(1,c+1)){
                int a = p - c - b;
                if (pow(a,2)+pow(b,2)==pow(c,2)){
                  s++;
                }  
            }
        }
        if (s > maxS){
            maxS = s;
            maxP = p;
        }
    }
    
    cout << "Max p is: " << maxP << endl;
    cout << "It has " << maxS << " solutions." << endl;

    return 0;
}
