#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool are_equal(char str1[], char str2[]) {
    if (strcmp(str1, str2) == 0) {
        return true;
    }
    return false;
}
bool are_sub(char str1[], char str2[]) {
    if (strstr(str1, str2) != 0) {
        return true;
    }
    return false;
}
bool are_sub2(char str1[], char str2[]) {
    if (strstr(str2, str1) != 0) {
        return true;
    }
    return false;
}


int main() {
   char str[100]={0};
    char str3[100], str2[100]={0};

    printf("enter a string");
   fgets(str, 100, stdin);
    str[strlen(str)-1] = 0;
    printf("enter a string");
    fgets(str2, 100, stdin);
    str2[strlen(str2)-1] = 0;
    if (are_equal(str,str2)){
        printf("The words are equal\n");
    }
    else
    {
        printf("The words are not equal\n");
    }
    if (are_sub(str,str2)){
        printf("Word 2 is a substring of word 1\n");
    }
    else if (are_sub2(str,str2)){
        printf("Word 1 is a substring of word 2\n");
    }
    else
    {
        printf("No substrings found\n");
    }

    return 0;
}