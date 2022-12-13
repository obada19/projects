#include <iostream>
#include <map>
#include <string>
#include <iterator>
#include<string.h>
using namespace std;


int main() {

    string input;
    cout << "enter a word"<<endl;
    int counter1=-1;
    map <string, int> mappy;
    string input1;

    while ( input1 != "stop") {
        cin >> input1;
        mappy[input1]++;
        counter1++;

    }
    mappy.erase("stop");

        int counter=0;
        int anouthercounter=0;
        for (auto& t : mappy)
          //  if(t.second==1)
                counter++;
        std::cout << "Total"<< " : "
                  << counter1 << " "<<endl;

    for (auto& t : mappy)
            anouthercounter++;
    std::cout << "Unique"<< " : "
              << anouthercounter << " "<<endl;

        for (auto& t : mappy)
        std::cout << t.first << " : "
                  << t.second << " "<<endl;
        cout<<endl;

    return 0;
}
