#include <stdio.h>
#include <string.h>
#include <ctype.h>
void string_lower(char lower[]){

    for (int i = 0; i <strlen(lower) ; ++i) {
        lower[i]=tolower(lower[i]);
    }
}
void string_upper(char upper[]) {

    for (int i = 0; i < strlen(upper); ++i) {
        upper[i] = toupper(upper[i]);
    }
}
int main() {

    char str[100];
int sr, br;
char str1[15]={0};
char str2[15]={0};

    printf("Enter a string:");
    gets(str);



    sr=strlen(str);
    br = sr/2;
    for (int i = 0; i <br ; ++i) {
        str1[i] = str[i];

    }
    for (int j = 0; j <br ; ++j) {
        str2[j]= str[j+br];

    }
    string_upper(str);
    printf("The word in uppercase is '%s'\n",str);
    string_lower(str);
    printf("The word in lowercase is '%s'\n",str);

printf("The word split in two is '%s - %s'",str1,str2);


    return 0;
}