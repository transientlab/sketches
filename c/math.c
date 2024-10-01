#include <stdio.h>
#include <stdlib.h>

#define BUFFERSIZE 32

char input_string[BUFFERSIZE];
char output_string[BUFFERSIZE];
int int_tmp1, int_tmp2;
int is_div_3(char str[BUFFERSIZE], int size);


int main () {
    printf("Enter number: ");
    scanf("%[^\n]%*c", input_string);

    int_tmp1 = atoi(input_string);
    printf("int+tmp1:    %d\n", int_tmp1);
    int_tmp2 = is_div_3(input_string, BUFFERSIZE);
    

    // itoa(int_tmp2, output_string, 10);
    printf("Result is:    %s", output_string);
}


int is_div_3(char str[BUFFERSIZE], int size) {
    int tmp1, tmp2, tmp3, i;
    tmp2 = 0;
    tmp1 = atoi(str);
    printf("tmp2:    %d\n", tmp2);
    while(tmp1) {
        printf("tmp1:    %d\n", tmp1);
        tmp3 = tmp1%10;
        tmp2 += tmp3;
        tmp1/=10;
        

    }
    return tmp2%3;
}
