#include "stdio.h"

enum something {
    one,
    two,
    three,
    four
};

int main (void) 
{
    enum something number = two;
    switch (number)
    {
    case one:
        printf("hejsia psiapsi\n");
        break;
    case two:
        printf("hejeczka psiapsini\n");
        break;
    default:
        printf("no hii\n");
        break;
    }
    return 0;
}