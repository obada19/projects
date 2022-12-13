#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool is_palindrome(char rev[], char string[]) {
    if (strcmp(rev, string) == 0) {
        return true;
    }
    return false;
}
void string_reverse(char string[], char rev[]) {
    int  k, j;


    k = strlen(string)-1;

    for (j = 0; j < strlen(string); j++) {
        rev[j] = string[k];
        k--;
    }

}


int main() {

    int i;
    char str[100] = {0};
    char bra[100]= {0};


    printf("Enter a string:\n");
    fgets(str, 100, stdin);

    str[strlen(str)-1]=0;


    for (i = 0; str[i] != '\0'; ++i);
    printf("The word contains %d letters\n", i);

    // not reversed
    string_reverse(str, bra);
    // reversed
    printf("The word reversed is '%s'", bra);

    if (is_palindrome(str,bra))
        printf("\nThe word is a palindrome");
    else
        printf("\nThe word is not a palindrome");


    return 0;
}
