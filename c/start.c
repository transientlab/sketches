#include <stdio.h>


#define	LENGTH		1024



int main(int argc, char** argv) {

	
	char klucz = 61; //ASCI 61 '='
	unsigned int i = LENGTH;
	int k = 0;
	int h[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	float a = 3.5234;
	double b = 423423.223454;
	char d;
	int u = 0;

	printf("size of int %d\n", sizeof(k));
	printf("size of int[10] %d\n", sizeof(h));
	printf("%d\n", argc);
	printf("%c\n", argv[0]);

	printf("podaj cegle: int int char\n");
	scanf("%d %d %c", &u, &k, &d);    
	//printf("\b");
	//printf("\r");
	//printf("\t");
	//printf("\a");
	//printf("\0");

	while(i) {
		switch(k)
		{
				case 1: printf("wyszlo 1\n"); break;

				case 2: {
					if(d == klucz) {
						return 0;
						printf("aaasdada\n");
						break; 
						}
					else {
						printf("bbbbb\n");
						}
					}

				case 3: printf("wyszlo 3\n");
				
		}

		printf("siemanko    %-5d %+10.3f %20f %c %#10x \n", i, a, b, d, u);
		b -= i;
		i--;
	}

	return 0;

}