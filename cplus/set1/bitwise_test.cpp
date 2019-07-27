#include <stdio.h>
//#include <array>
#include <iostream>
#include <vector>

using namespace std; 
//g++ -std=c++11  

int bitwiseComplement(int N) {
        vector<int> result; 
        if (N == 0) return 1; 
        
        while (N) { 
            if (N % 2) result.push_back(0); 
            else result.push_back(1); 
            // 10: 1 0 1 0 --> 0 1 0 1  
            N = N / 2; 
        }

        for (auto i: result) { 
            cout << i << endl; 
        } 


        reverse(result.begin(), result.end());
        int sum = 0; 
        for (auto i: result) { 
            cout << "adding " << i << endl; 
            sum = sum * 2 + i; 
        }
        cout << "the result is " << sum << endl; 
        return sum; 
}


int main() { 
    cout<<"Hello World!"<<endl; 

    int result = bitwiseComplement(10); 

    cout << "the result 10 is " << result << endl; 

   result = bitwiseComplement(5); 

    cout << "the result 5 is " << result << endl; 


    result = bitwiseComplement(7); 

    cout << "the result 7 is " << result << endl; 

    return 0; 
} 

