//
// Created by obada on 23.11.2022.
//
#include<string.h>
#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next_to_link;
    //index=0;

    Node()
    {
    //
        data = 0;
        next_to_link = nullptr;
    }

    Node(int data)
    {
        //link=head;
        this->data = data;
        this->next_to_link = nullptr;
    }
};
int tall;

class The_linket_list{
    Node *Head;
    public:
    The_linket_list()
    {
        Head = nullptr;
    }

    //'void push_back(const int value)',
   // 'size_t size1()',
    int& at(size_t index){
    }
  //  'void remove1(size_t index)'
   // void retrieve_index(int);
   // size_t index();
   // void push_back(const int value)
    //Add a value to the back of your list
   //         size_t size1()
   // Get the item count
   // int& at(size_t index)
   // Retrieve item by index
   // void remove1(size_t index)
  //  Remove item at specified index

     size_t retrieve_index(size_t index) {
        Node *current = Head;
        Node *temporary = Head;
        int counter;
        counter = 0;
// prints the last index not found always error
        while (current != nullptr) {
            if (counter == index)
                cout << "Integer at index " << index << ": " << current->data << endl;
            // return (current->data) ;

            counter++;
            current = current->next_to_link;

        } //if (index !=);

        cout << "List contains no integers" << endl;

        //assert(0);
    };

    void push_back1(const int value){}
    size_t size(){}
    int& at1(size_t index){}
    void remove(size_t index){}


    void push_back(const int value) {
        Node *newNode = new Node(value);
        //
        if (Head == nullptr) {
            Head = newNode;
            return;
            //return0;
        }
        Node *temporary = Head;
        while (temporary->next_to_link != nullptr) {
            temporary = temporary->next_to_link;
            //
            //
            //
        }
        temporary->next_to_link = newNode;
        //cout<<""<<endlt;
    }
    size_t size1(){
        Node *temporary = Head;
        tall = 0;
        if (Head == nullptr) {
            cout << "List contains no integers" << endl;
        }
        while (temporary != nullptr) {
            temporary = temporary->next_to_link;
            tall++;
        }
    }
    void remove1(size_t node1) {
        Node *usable1 = Head, *usable2 = nullptr;
        int Size_ofli = 0;

        if (Head == nullptr) {
            cout << "List contains no integers" << endl;
            return;
        }
//goint to next
        while (usable1 != nullptr) {
            usable1 = usable1->next_to_link;
            Size_ofli++;
        }

//end n print
        if (Size_ofli < node1) {
            cout << "list index out of range"<< endl;
            return;
        }
        usable1 = Head;
        if (node1 == 0) {
            //deletion
            Head = Head->next_to_link;
            delete usable1;
            return;
        }
        //jumping while (){]]}
        while (node1-- > 0) {
            usable2 = usable1;
            usable1 = usable1->next_to_link;
        }
        //
        usable2->next_to_link = usable1->next_to_link;
        delete usable1;
    }
    void printList() {
        Node *temporary = Head;
        tall = 0;
        if (Head == nullptr) {
            cout << "List contains no integers" << endl;

        }
        cout << "List contains "<< size1() << " integers: ";
        while (temporary != nullptr) {
                cout << temporary->data << ' ';
                tall++;
                temporary = temporary->next_to_link;

            }

         cout << endl;


    }




    const char * printer(){

        cout << "List contains "<< size1() << " integers: ";
        printList();
        cout << endl;


    }void hello(){
        //int result = strcmp(printer(), "List contains List contains no integers\n"
          //                                  "1875946688 integers: List contains no integers");
       // if (){cout<<"List contains no integers"<<endl;}
        //else{printer();}
    }
};



int main()
{
    The_linket_list list;

    int integer;
//cin >> integer;
//cout<< "enter a number";
    while (integer != 5){
        cout<< "1. Add integer"<<endl;
        cout<< "2. Show integer at index"<<endl;
        cout<< "3. Remove integer at index"<<endl;
        cout<< "4. Print information"<<endl;
        cout<< "5. Exit"<<endl;
        cin >> integer;


        if (integer==1){
            cout<<"enter a number to be added"<<endl;
            int number;
            cin>>number;
            list.push_back(number);
        }
        else if (integer==2){
            cout<<"enter an index"<<endl;
            int number1;
            cin>>number1;
            list.retrieve_index(number1);

        }
        else if (integer==3){
            cout<<"enter an index"<<endl;
            int number1;
            cin>>number1;
            list.remove1(number1);
            cout << "Elements of the list are: ";
            list.printList();
        }
        else if (integer==4){
            //list.hello();
            list.printList();

        }

    }
    if (integer==10101010){
        list.at(1);
        list.size1();
        list.push_back(1);
        list.remove1(1);
    }
    return 0;
}