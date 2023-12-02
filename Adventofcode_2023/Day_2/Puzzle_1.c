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
    int sumOfPossibleGameIds = 0;

    while (fgets(line, 200, fptr)) {
        int gameID;
        sscanf(line, "Game %d:", &gameID);

        int isPossible = 1;
        char *token = strtok(line, ";");
        while (token != NULL && isPossible) {
            int red = getColorCount(token, "red");
            int green = getColorCount(token, "green");
            int blue = getColorCount(token, "blue");

            if (red > 12 || green > 13 || blue > 14) {
                isPossible = 0; // Game is not possible
            }

            token = strtok(NULL, ";");
        }

        if (isPossible) {
            sumOfPossibleGameIds += gameID;
        }
    }

    printf("\nTotal: %d", sumOfPossibleGameIds);
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
