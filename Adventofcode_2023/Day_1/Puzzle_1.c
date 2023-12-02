#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

FILE *fptr;

int concat(int a, int b)
{

    char s1[20];
    char s2[20];

    // Convert both the integers to string
    sprintf(s1, "%d", a);
    sprintf(s2, "%d", b);

    // Concatenate both strings
    strcat(s1, s2);

    // Convert the concatenated string
    // to integer
    int c = atoi(s1);

    // return the formed integer
    return c;
}

int main() {
    fptr = fopen("Input_1.txt", "r");
    char line[100];
    int sum = 0;

    while(fgets(line, 100, fptr)){
        int len, firstDigit, lastDigit;
        len = strlen(line);
        for (int i = 0; i < len; i++){
            if (isdigit(line[i])){
                firstDigit = line[i] - '0';
                printf("%d", firstDigit);

                break;
            }
        }
        for (int i = len - 1; i >= 0; i--) {
            if (isdigit(line[i])){
                lastDigit = line[i] - '0';
                printf("%d\n", lastDigit);
                break;
            }
        }
        sum += concat(firstDigit, lastDigit);
    }
    fclose(fptr);
    printf("\nTotal Sum: %d\n", sum);
    return 0;
}