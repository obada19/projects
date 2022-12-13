#include <stdio.h>
#include <string.h>
#include "student.h"
int main() {


    student_t student;
printf("enter student id\n");
    scanf("%d",&student.id);
    getchar();
    printf("enter name\n");
   fgets(student.Name,100,stdin);

    student.Name[strlen(student.Name)-1]=0;
    printf("enter age\n");
    scanf("%d",&student.Age);

    printf("Student id: %d\nName: %s\nAge: %d\n",student.id, student.Name, student.Age);

    return 0;
}