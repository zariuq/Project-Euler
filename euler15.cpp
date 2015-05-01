#include <iostream>
#include <math.h> // For max
#include <string>
#include <vector>
#include <list>
#include <array>
#include <iterator>
using namespace std;


void SolveGrid(long long int* c, int size, int r, int d){
    if (r == size && d == size){
        (*c)++;
    }
    else{
        if (r < size) {
            SolveGrid(c, size, r+1, d);
        }
        if (d < size) {
            SolveGrid(c, size, r, d+1);
        }
    }
    //cout << "r and d: " << r << " " << d << endl;
}

// This answer * (size + 1) == our answer... so the possibilities we miss increases with size :o
void SolveGridt(long long int* c, int size, int r, int d){
    if (r == size && d == size){
        (*c)++;
    }
    else if (r >= d){
        if (r < size) {
            SolveGridt(c, size, r+1, d);
        }
        if (d < size) {
            SolveGridt(c, size, r, d+1);
        }
    }
}

int main() { 
  
    long long int c = 0;
    long long int ct = 0;
    int k = 10;
    for (k = 16; k < 21; k++){
        SolveGridt(&c,k,0,0);
        cout << "Count " << k << ": " << (c) << endl;
        cout << "Answer " << k << ": " << (c*(k+1)) << endl;
        c = 0;
    }
    //SolveGridt(&ct,k,0,0); // 2 = 6, 5 = 252, 10 = 184756, 15 = 155117520   
    //cout << "Test: " << (ct) << endl;
    //auto diff = c / ct;
    //cout << "diff: " << diff << endl;
   
    
    /*for (int i = 1; i < 16; i++){
        c = 0;
        ct = 0;
        SolveGrid(&c,i,0,0);
        SolveGridt(&ct,i,0,0);
        c = c*2;
        diff = c / ct;
        cout << "Count " << i << " = " << c << endl;
        cout << "test: " << ct << endl;
        cout << "diff: " << (c / ct) << endl;
    }*/
    
    
    
    return 0;
}

/*
Count 0: 2
Count 1: 2
Count 2: 6
Count 3: 20
Count 4: 70
Count 5: 252
Count 6: 924
Count 7: 3432
Count 8: 12870
Count 9: 48620
Count 10: 184756
Count 11: 705432
Count 12: 2704156
Count 13: 10400600
Count 14: 40116600
Count 15: 155117520
*/






