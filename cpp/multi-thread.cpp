
#include <iostream>
#include <thread>
#include <chrono>
#include <random>

using namespace std;

std::random_device rd;
std::mt19937 gen(rd());
std::uniform_int_distribution<int> dis(0, std::numeric_limits<int>::max());

class looper
{
private:
    int ID;
    int counter;
    int rounds;
public:
    looper(int time, int number);
    ~looper();
    int start();
};

looper::looper(int time, int number)
{   
    gen();
    counter = time;
    rounds = number;
    ID = int(gen() * 1000000 % (counter*rounds));
    std::cout << "powstal looper " << ID << endl;
}

looper::~looper()
{
}

int looper::start()
{   
    for(int i = rounds; i > 0 ; i--)
    {   
        std::this_thread::sleep_for(std::chrono::milliseconds(counter));
        std::cout << ID << " : " << i << "/ " << rounds << endl;
    }
    return 0;
    
}


int main(int argc, char *argv[]) 
{   
    std::cout << argc << " " << argv[0] << " "  << argv[1] << endl;
    
    looper first_loop(atoi(argv[1]), atoi(argv[2]));
    looper second_loop(atoi(argv[1]) / 4, atoi(argv[2]) * 8);
    std::thread * th[atoi(argv[2])];
    std::thread th1 ([&first_loop]() { first_loop.start(); });
    std::thread th2 ([&second_loop]() { second_loop.start(); });
    th1.join();
    th2.join();

    // std::thread * th[atoi(argv[2])];
    // looper * ob[atoi(argv[2])];
    // int k = 0;
    // for (k = 0; k < atoi(argv[2]); k++) {
    //     ob[k] = new looper(atoi(argv[1]) / k / 2, atoi(argv[2]) * (k+1));
    // }   
    // for (k = 0; k < atoi(argv[2]); k++) {
    //     th[k] = new std::thread ([&ob](int k) { ob[k]->start(); });
    //     th[k]->join();

    //     std::cout << "ok: " << k << endl;
    // }   
    
        
    std::cout << "ale koniec" << endl;
    return 0;

}
