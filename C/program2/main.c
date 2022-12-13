#include <stdio.h>
#include <stdlib.h>

int sum(int array[],int count)
{
    int sum = 0;

    for (int i = 0; i <count; ++i) {
        sum += array[i];
    }

    return sum;
}
int minimum(int array[],int count){
  int  min = array[0];
    for (int i = 0; i <count; ++i) {
       if (min > array[i]){
           min = array[i];
       }
    }
    return min;
}
int maximum(int array[],int count){
    int  max = array[0];
    for (int i = 0; i <count; ++i) {
        if (max < array[i]){
            max = array[i];
        }
    }
    return max;
}

float average(float sum, float count){
float ave = sum/count;
return ave;
}

void sort(int array[], int count){
  int potet;
    for (int i = 0; i <count; ++i) {
        for (int j = 0; j < (10-i-1); ++j) {
            if (array[j]>array[j+1]){
                potet =array[j];
                array[j]=array[j+1];
                array[j+1]=potet;
            }
        }

    }

}

float median(int array[], int count){
    float median1 = (array[4]+ array[5])/2.0;
    return median1;
}



int main()
{
int count = 10;
    int  array[100];
    printf("please enter 10 integers\n");

    for (int i = 0; i < 10; i++)
    {
        scanf("%i", &array[i]);
    }

    int sum_ = sum(array, 10);

    printf("Sum: %i\n", sum_);
int minimum_ = minimum(array, 10);
printf("Minimum: %i\n", minimum_);

    int maximum_ = maximum(array, 10);
    printf("Maximum: %i\n", maximum_);

    float bro =average((float)sum_, (float)10);
printf("Average: %g\n", bro);


sort(array, count);
printf("Sorted:");
    for (int j = 0; j < count; ++j) {
        printf(" %i", array[j]);
    }
    printf("\n");

    float bros= median(array, count);
    printf("Median: %g\n", bros);

    return 0;
}