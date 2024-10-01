#include <iostream>
#include <random>
#include <map>

class Matter
{
    public:
    Matter(int id) : _identifier(id)
    {
        std::cout << "Matter for " << _identifier << " created\n";
    }
    ~Matter()   
    {
        std::cout << "Matter for " << _identifier << " destroyed\n";
    }
    private:
    const int _identifier;
};

class CelestialBody
{
    public:
    CelestialBody(double mass) : _mass(mass)
    {
        std::cout << "Celestial body of mass" << _mass << " created";
    }
    ~CelestialBody()
    {
        std::cout << "Celestial body destroyed";
    }
    private:
    const double _mass;
};

class Star : public CelestialBody
{
    public:
    Star(double mass, double brightness, int identifier) : CelestialBody(mass), _brightness(brightness), _identifier(identifier)
    {
        std::cout << "Star of brightness " << _brightness << " created";
    }
    ~Star()
    {
        std::cout << "Star destroyed";
    }
    void PrintID() {
        std::cout << "Star numbah: " << _identifier << "\n";
    }
    private:
    const double _brightness;
    const int _identifier;
};

class World
{
    public:
    World(int id) : _identifier(id), _matter(id)           // the only place you can assign sth, if obj constructor has no argument it can be omitted here
    {
        std::cout << "Heelo universe" << _identifier << "\n";
    }
    ~World()    
    { 
        std::cout << "The end of the world " << _identifier << "\n";
    }
    void PrintID() {
        std::cout << "Uninv numbah: " << _identifier << "\n";
    }
    private:
    const int       _identifier;      // conventionally with underscore
    const Matter    _matter;
};



class InputNum
{
    public:
    InputNum()
    {
        std::cout << "enter numbahrggggrrr: ";
        std::cin >> _num;
    }
    ~InputNum()
    {

    }
    int GetValue() const
    {
        return _num;
    }
    void SetValue(int num)
    {
        _num = num;
    }

    private:
    int _num;
};


World TheUniverse(1);

int main() {
    std::random_device rd {};
    std::mt19937 gen {rd()};
    InputNum inputer;
    std::extreme_value_distribution();
    std::cout << inputer.GetValue() << " numbah was put\n";
    std::cout << "now it is " << inputer.GetValue() << "\n";
    int n = inputer.GetValue();
    World *stars[n];

    const int norm = 10000;
    std::map<int, int> hist {};
    for (int n = 0; n != norm; ++n)
    ++hist[std::round(d(gen))];

    while(n)
    {
        std::cout<<n;
        if (n == 3)
        {
                
        }
        
        n--;
    }
    stars[5]->PrintID();

    return 0;
}