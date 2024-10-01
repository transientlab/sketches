#include <iostream>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>

void func(short* counter);

int main(void) 
{
    // using namespace std;
    const char* my_name = "PABEL";
    double random_numbah;
    for(int i=0; i < 10; i++)
    {
    srand(i);
    random_numbah = rand();
    srand(i*2);
    random_numbah = pow(random_numbah, rand()/100000000);
    srand(i*3);
    random_numbah = random_numbah / rand();
    // std::cout << random_numbah << std::endl;
    }

    // std::cout << UINT32_MAX << std::endl;
    // std::cout << "uint32_t is " << sizeof(uint32_t) << " bytes" << std::endl;
    long long piano;
    // std::cout << sizeof(piano) << std::endl;
    piano = LLONG_MAX;
    // std::cout << piano << std::endl;
    // std::cout << std::hex << piano << std::endl;
    // std::cout << std::oct << piano << std::endl;
    // std::cout << std::dec << piano << std::endl;

    char c;
    for(int z=0; z<128; z++)
    {
        c=z;
        // std::cout << z << " : " << c << std::endl;
    }

    // std::cout << "const name: " << &my_name << std::endl;
    bool ready = true;

    float krank = 10.0 / 3.0;
    double kranki = 10.0 / 3.0;
    // std::cout << krank * 1000000000 << std::endl << kranki  * 1000000000 << std::endl;

    const int LENGTH = 5;
    long long thearray[LENGTH];
    static short counter = 0;
    for(int i = 0; i < LENGTH; i++)
    {
        thearray[i] = pow(3, i);
        // std::cout << thearray[i] << std::endl;
        func(&counter);
    }
    std::cout << "separate" << std::endl;
    counter++;
    for(int i = 0; i < LENGTH; i++)
    {
        thearray[i] = pow(3, i);
        // std::cout << thearray[i] << std::endl;
        func(&counter);
    }

    std::string elo = "heelo";
    std::cout <<  elo.size() << std::endl;

    std::string majcior;
    std::getline(std::cin, majcior);
    std::cout << majcior << std::endl;


    return 0;
}

void func(short* counter) {
    std::cout << *counter << std::endl;
    char inputline[20] = "hasztag#";
    // std::cin.getline(inputline, 20);
    for(int i = 0; i < *counter; i++)
    {
        std::cout << inputline;
    }
    std::cout << std::endl;
    (*counter)++;
}