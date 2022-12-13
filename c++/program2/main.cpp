#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int main() {

    map<string, string> mappy;
    ifstream in("countries.txt");
    string country, code;
    cout<<"enter a choice to search\n"
          "1 for country\n"
          "2 for code\n"
          "3 for exit\n";
    int enter;
    cin>>enter;
    if(enter==2)
    {
        while (getline(in, code) && getline(in, country))
            mappy[country] = code;


        string temp;
        cout<<"search for a country";
        cin>>temp;
        auto iterator = mappy.find(temp);
        if (iterator != mappy.cend())
            cout << "Country code : "<<
                 iterator->second <<endl;
        else
            cout << temp << "no" <<"\n";
    }



    else if (enter==1) {
        while (getline(in, country) && getline(in, code))
            mappy[country] = code;


        string temp;
        cout << "search for a country by code";
        cin >> temp;
        auto anotheriterator = mappy.find(temp);
        if (anotheriterator != mappy.cend())
            cout << "Country name : "<< anotheriterator->second << endl;
        else
            cout << temp << "no" << "\n";
    }
    return 0;
}
