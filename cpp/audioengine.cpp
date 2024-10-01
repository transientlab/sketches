#include <iostream>

#include <sndfile.h>

using namespace std;

SF_INFO wf_info;
SNDFILE* wavefile = sf_open("in.wav", SFM_READ, &wf_info);;


int main (void) 
{
    cout << wf_info.samplerate;
    
    return 0;
}

