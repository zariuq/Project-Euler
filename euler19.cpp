#include <iostream>
#include <boost/array.hpp>

using namespace std;
int main(){
    boost::array<int, 12> months = {{31,28,31,30,31,30,31,31,30,31,30,31}};
    int year = 1900;
    int day = 1;
    int sundays = 0;
      
    for (; year < 2001; year++){
        for (int m = 0; m < 12; m++){
            if (day % 7 == 0 && year > 1900){
                    sundays++;   
            }
            day += months[m];
            
            if (year % 4 == 0 && m == 1){
                day++;
            }
        } 
    }
  
  
  cout << "Year: " << year << endl;
  cout << "Day: " << day << endl;
  cout << "Sundays: " << sundays << endl;
  return 0;
}
