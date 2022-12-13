#include <iostream>
#include <vector>
#include <string>
#include "account.h"

using namespace std;



int main() {
    vector<student> dt;

    student st;


    getline(cin, st.name);

    while (st.name != "stop") {

        getline(cin, st.course_name);

        while (st.course_name != "stop") {

            cin >> st.grade;
            cin.ignore();
            if (st.course_name != "stop")
                dt.push_back(st);
            getline(cin, st.course_name);

        }
        getline(cin, st.name);

    }


    for (auto i = 0; i < dt.size(); ++i) {
        dt[i].print();
    }

    return 0;
}