#include <stdio.h>

int main() {
        float number = 0;
    float count = number;
    float sum = 0;
    float average = 0;
     printf("please enter a number: \n");
     scanf("%f", &number);
while (number != 0)
    {
    count ++;
    sum += number;
    printf( "try again:) \n");
    scanf("%f", &number);
    }
average = sum/count;
printf("Count: %g\n", count);
    printf("Sum: %g\n", sum);
    printf("Average: %g\n", average);

    return 0;
}