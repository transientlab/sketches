#include <iostream>
#include <cmath>
#include <climits>
#include <cstring>
#include <random>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include "unistd.h"

class new_test :
{
private:
    int ID;
public:
    new_test(int num) : ok(num)
    {

    }
    ~new_test();

    int ok;
};

new_test::new_test(int num)
{
    ok = num;
    ID = ok * 3;
}

new_test::~new_test()
{

}

int main (void) 
{

    int n = 0;
    while(true) 
    {
        std::cout<<n;
        usleep(1000000);
        n++;
    }

    return 0;

}