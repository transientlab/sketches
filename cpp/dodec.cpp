#include <iostream>
#include <cmath>


int main (void)
{
    int NUMBER_OF_CHANNELS = 12;     // 
    int NUMBER_OF_TONES = 9;         //
    int START_TONE = 64;             // in Hz

    int freq;
    for(int i = 0; i < NUMBER_OF_CHANNELS; i++)
    {
        std::cout << "channel number: " << i+1 << std::endl;
        for(int f = 0; f < NUMBER_OF_TONES; f++)
        {
            freq = START_TONE * std::pow(2, f);
            std::cout << "\tfrequency: " << freq << std::endl;
        }
        
    }

}

