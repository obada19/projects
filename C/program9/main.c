#include <stdio.h>
#include <stdlib.h>


int cmpfunc (const void * a, const void * b) {
    return ( *(int*)a - *(int*)b );
}



int main() {
    printf("enter number of integers\n");
    int size;
    scanf("%i",&size);
    printf("Count: %i\n", size);
    if (size==0)
    {
        printf("No numbers were given");
    } else {
        int *numbers = malloc(size * sizeof(int));


        for (int i = 0; i < size; ++i) {
            scanf("%i", &numbers[i]);
        }

        printf("Numbers: ");
        for (int j = 0; j < size; ++j) {
            printf("%i ", numbers[j]);
        }
        printf("\n");
        printf("Sorted: ");
        qsort(numbers, size, sizeof(int), cmpfunc);
        for (int k = 0; k < size; ++k) {
            printf("%i ", numbers[k]);
        }

        free(numbers);
        numbers = NULL;

    }
   return 0;
}