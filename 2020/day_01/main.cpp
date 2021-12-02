#include <iostream>
using namespace std;

int main() {
    FILE *f;
    f = fopen("input.txt", "r");
    char c;

    while ((c = getc(f)) != EOF) {
        cout << c;
    }

    return 0;
}