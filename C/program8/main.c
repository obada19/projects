#include <stdio.h>
#include "student.h"
#include <string.h>
#include <stdlib.h>

int main() {

int  choice;

while (1) {
    scanf("%i",&choice);

    if (choice == 1) {
        FILE *fptr = fopen("student_read.txt", "r");
        student_t student;

        fscanf(fptr, "%i", &student.id);
        fgetc(fptr);
        fgets(student.Name, 100, fptr);

        student.Name[strlen(student.Name) - 1] = 0;
        fscanf(fptr, "%i", &student.Age);

        printf("Student id: %i\n", student.id);
        printf("Name: %s\n", student.Name);
        printf("Age: %i\n", student.Age);

        fclose(fptr);
    } else if (choice == 2) {
        FILE *fptr1 = fopen("student_write.txt", "w");
        student_t student;

        printf("enter student id\n");
        scanf("%i", &student.id);
        getchar();

        printf("enter name\n");
        fgets(student.Name, 100, stdin);
        student.Name[strlen(student.Name) - 1] = '\0';

        printf("enter age\n");
        scanf("%i", &student.Age);
        getchar();

        fprintf(fptr1,"%i\n", student.id);
        fprintf(fptr1,"%s\n", student.Name);
        fprintf(fptr1,"%i\n", student.Age);


        fclose(fptr1);

    } else if (choice == 3) {
        break;

    } else {
        printf("enter 3 to exit\n");
    }
}

return 0;
}


