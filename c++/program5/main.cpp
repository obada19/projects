#include <iostream>

using namespace std;

    void cmp(string s1, string s2)
    {

        if(s1 !=s2){
            std::cout<< "The strings are not equal"<< std::endl;
        }else{
            std::cout << "The strings are equal"<<std::endl;
        }
    }
    void sub(string s1, string s2){
        if(s1.find(s2)!= std::string::npos){
            std::cout << "Last string is substring of first string"<< std::endl;
        }
        else if (s2.find(s1)!= std::string::npos){
            std::cout << "First string is substring of last string" << std::endl;
        }

        else {
            std::cout << "There are no substrings" << std::endl;
        }

    }
    int main() {



        std::string s1;
        std::string s2;
        std::getline(std::cin, s1);
        std::getline(std::cin, s2);


        cmp(s1, s2);


        sub(s1,s2);



        return 0;
}