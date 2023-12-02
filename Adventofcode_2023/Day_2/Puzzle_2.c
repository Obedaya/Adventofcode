#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int getColorCount(char *set, char *color);

int main() {
    FILE *fptr = fopen("Input_1.txt", "r");
    if (fptr == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    char line[200];
    int sumOfPowers = 0;

    while (fgets(line, 200, fptr)) {
        int red = 0, green = 0, blue = 0, sum = 0;
        char *token = strtok(line, ";");
        while (token != NULL) {
            int tempRed = getColorCount(token, "red");
            int tempGreen = getColorCount(token, "green");
            int tempBlue = getColorCount(token, "blue");

            if (tempRed > red){
                red = tempRed;
            }
            if (tempGreen > green){
                green = tempGreen;
            }
            if (tempBlue > blue){
                blue = tempBlue;
            }
            token = strtok(NULL, ";");
        }
        sum = red * green * blue;
        sumOfPowers += sum;
    }

    printf("\nTotal: %d", sumOfPowers);
    fclose(fptr);
    return 0;
}

int getColorCount(char *set, char *color) {
    char buffer[50];
    sprintf(buffer, "%s", set);
    char *colorPos = strstr(buffer, color);
    if (colorPos != NULL) {
        int count = 0;
        sscanf(colorPos - 3, "%d", &count);
        return count;
    }
    return 0;
}

