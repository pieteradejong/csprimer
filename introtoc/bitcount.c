#include <assert.h>
#include <stdio.h>

// int main2() {
//     assert(bitcount(0) == 0);
//     assert(bitcount(1) == 1);
//     assert(bitcount(3) == 2);
//     assert(bitcount(8) == 1);
//     // harder case:
//     // assert(bitcount(0xffffffff) == 32);
//     printf("OK\n");
// }

void isKthBitSet(int n, int k) {
    if(n & (1<<k)) {
        printf("bit is set");
    } else {
        printf("bit is not set");
    }
}

int main() {
    isKthBitSet(8, 3);
    return 0;
}
