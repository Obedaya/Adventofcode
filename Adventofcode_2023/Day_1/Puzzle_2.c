#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

FILE *fptr;

int concat(int a, int b) {
    char s1[20];
    char s2[20];

    // Convert both the integers to string
    sprintf(s1, "%d", a);
    sprintf(s2, "%d", b);

    // Concatenate both strings
    strcat(s1, s2);

    // Convert the concatenated string to integer
    int c = atoi(s1);

    // return the formed integer
    return c;
}

int main() {
    char *charDigits[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int sum = 0;

    fptr = fopen("Input_1.txt", "r");

    char line[100];

    while(fgets(line, 100, fptr)) {
        int firstDigit = -1, lastDigit = -1;
        int len = strlen(line);

        // Find the first digit or word
        for (int i = 0; i < len; i++) {
            if (isdigit(line[i])) {
                firstDigit = line[i] - '0';
                break;
            }
            for (int j = 0; j < 10; j++) {
                if (strncmp(&line[i], charDigits[j], strlen(charDigits[j])) == 0) {
                    firstDigit = j;
                    i += strlen(charDigits[j]) - 1;
                    break;
                }
            }
            if (firstDigit != -1) {
                break;
            }
        }

        // Find the last digit or word
        for (int i = len - 1; i >= 0; i--) {
            if (isdigit(line[i])) {
                lastDigit = line[i] - '0';
                break;
            }
            for (int j = 0; j < 10; j++) {
                if (i >= strlen(charDigits[j]) - 1 && strncmp(&line[i - strlen(charDigits[j]) + 1], charDigits[j], strlen(charDigits[j])) == 0) {
                    lastDigit = j;
                    break;
                }
            }
            if (lastDigit != -1) {
                break;
            }
        }

        if (firstDigit != -1 && lastDigit != -1) {
            printf("%d", firstDigit);
            printf("%d \n", lastDigit);
            sum += concat(firstDigit, lastDigit);
        }
    }
    fclose(fptr);
    printf("\nTotal Sum: %d\n", sum);
    return 0;
}
