#include <stdio.h>
#include "student.h"
#include <stdlib.h>
#include <string.h>
int  Youngestandoldest(const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}


int main() {

    int count=0;

    s* se;
    se = malloc(sizeof(s)); // an "array" of students


    while(1) {
        printf("enter student name\n");
        fgets(se[count].name, 100, stdin);
        se[count].name[strlen(se[count].name)-1]='\0';

        if(strcmp("stop",se[count].name)==0){
            break;
        }

        printf("enter student age\n");
        scanf("%i", &se[count].age);
        getchar();


        count++;
        se =(s*) realloc(se, (count+2)*sizeof(s));
    }
    if (count == 0)
    {
        printf("No students were given");
        return 0;
    }


    printf("Count: %i\n",count);

    s* Youngest = &se[0];
    s* Oldest = &se[0];

    for (int i = 0; i < count ; ++i) {
        printf("Name = %s, Age = %i", se[i].name, se[i].age);

        printf("\n");
        if (Youngest->age < se[i].age)
        {
            Youngest = &se[i];
        }
        if (Oldest->age > se[i].age)
        {
            Oldest = &se[i];
        }
    }

// qsort(se,count-1, sizeof(s),Youngestandoldest);
    printf("Oldest: %s\n",Youngest->name);
    printf("Youngest: %s",Oldest->name);

    free(se);
    se = NULL;


    return 0;
}