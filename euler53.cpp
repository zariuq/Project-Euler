#include <iostream>
#include <math.h>
#include <string>
#include <boost/range/irange.hpp>
using namespace boost;
using namespace std;

int main () {
    int count = 0;    

    const int limit = 100;
    for (auto n : irange(1,limit+2)){
        double C = 1; // long long int wasn't big enough.. oh well.
        //cout << n-1 << ": "; // I suppose a trick is that you don't need to compute numbers beyond 10000
        for (auto i : irange(1,n+1)){
            if (n == 100)
                cout << C << " ";
            C = C * (n - i) / i;
            if (C >= 1000000) {
                count += n - 2 * (i); // I guess I'll notice this speed-up with bigger numbers <_<;
                break;
            }
        }
        //cout << endl;
    }

    cout << endl;
    cout << "The count is " << count << endl;




    return 0;
}
