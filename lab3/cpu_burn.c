#include <math.h>

int main() {

    int i = 0;
    while (i++ < 600000000) {
        pow(1.2, 2.3);
    }
    return 0;
}