#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<double> v;
int temp=1;
    double m;
    double sum = 0,i=0;
    cout << "Enter  numbers: "<< std::endl;

    while (temp!=0) {
        cin >> temp;
        if(temp==0)break;
        sum += temp;
        v.push_back(temp);
        i+=1;
                    }

double average;
    average=sum/(i);
    std::cout<<"Average : "<< average<< std::endl;





    sort(v.begin(), v.end());

    m = v.size()/2;

double median;
if (v.size()% 2 == 1)
{
     median= v[m];
}else
    {
         median =(v[m]+(v[m-1]))/2.0;

}
    sort(v.begin(), v.end(), greater<>());

    std::cout<<"Median : " << median;
    cout << "\nDescending : ";
    for (int j = 0; j < i; ++j)
        cout << v[j]  <<" ";

    return 0;
}