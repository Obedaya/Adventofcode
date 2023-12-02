#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int table1 [3] [3] = {
        {4, 1, 7},
        {8, 5, 2},
        {3, 9, 6}
};
int table2 [3] [3] = {
        {3, 1, 2},
        {4, 5, 6},
        {8, 9, 7}
};

char x [3] = {'A', 'B', 'C'};
char y [3] = {'X', 'Y', 'Z'};

int calculatepoints(char m, char e, int s){
    for (int i = 0; i < 3; ++i) {
        if( x[i] == e){
            for (int j = 0; j < 3; ++j) {
                if(y[j] == m){
                    if(s == 1){
                        return table1[j][i];
                    }
                    else{
                        return table2[j][i];
                    }
                }
            }
        }
    }
}


int main() {
    ifstream inputfile ("input.txt");
    int score;

    if ( inputfile.is_open() ) {
        while ( inputfile ) {
            int s;
            cout << "Puzzle day 2" << endl;
            cout << "Part 1 [1] or Part 2 [2] : ";
            cin >> s;
            for(string line;  getline (inputfile, line);){
                int tmpscore;
                char e = line[0];
                char m = line[2];
                tmpscore = calculatepoints(m, e, s);
                score += tmpscore;
                cout << line << ": " << tmpscore << '\n';
            }
        }
    }
    cout << "Your score is: " << score;
    return 0;
}
