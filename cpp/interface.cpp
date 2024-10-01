#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <cstring>
#include <chrono>
#include <thread>

using namespace std;

string welcome = "_ t r a n s i e n t l a b ";

chrono::milliseconds sleeptime(50);

int main (int argc, char* argv[])
{
    cout << welcome << endl;
    cout << "pi:\t" << M_PI << endl;
    cout << "e:\t" << M_E << endl;
    cout << "-------------------------\n" << endl;

    cout << "opening \'" << argv[1] << "\' as WAV file" << endl;
    ifstream wavefile(argv[1], ios::binary);
    if (!wavefile.is_open())
    {
        cerr << "error reading file!" << endl;
        return 1;
    }

    wavefile.seekg(0, ios::end);
    streampos fileSize = wavefile.tellg();
    wavefile.seekg(0, ios_base::beg);


    if (fileSize < 44)
    {
        cerr << "file is not a valid WAV file!" << endl;
        return 1;
    }
    
    vector<char> header(44);
    wavefile.read(header.data(), 44);
    cout << "wavefile size:\t" << fileSize << " bytes" << endl;
    if (memcmp(header.data(), "RIFF", 4) != 0 || memcmp(header.data() + 8, "WAVE", 4) != 0 || memcmp(header.data() + 12, "fmt ", 4) != 0)
    {
        cerr << "file header invalid!" << endl;
        return 1;
    }

    int16_t audioFormat;
    int16_t numChannels;
    int32_t sampleRate;

    wavefile.seekg(20, ios::beg);
    wavefile.read(reinterpret_cast<char*>(&audioFormat), sizeof(audioFormat));
    wavefile.seekg(22, ios::beg);
    wavefile.read(reinterpret_cast<char*>(&numChannels), sizeof(audioFormat));
    wavefile.seekg(24, ios::beg);
    wavefile.read(reinterpret_cast<char*>(&sampleRate), sizeof(sampleRate));
    
    uint32_t headerSize;
    std::memcpy(&headerSize, header.data() + 16, sizeof(headerSize));

    if (audioFormat != 1) 
    {
        cerr << "it is not a PCM file" << endl;
        return 1;
    }

    cout << "PCM: " << numChannels << " channels @ " << sampleRate << " Hz" << endl;

    wavefile.seekg(headerSize, ios::beg);
    cout << "header size: " << headerSize;
    
    const size_t bufferSize = 4096;
    vector<int16_t> buffer(bufferSize / sizeof(int16_t));
    
    while (wavefile) {
        wavefile.read(reinterpret_cast<char*>(buffer.data()), bufferSize);
        streamsize bytesRead = wavefile.gcount() / sizeof(int16_t);

        for (streamsize i = 0; i < bytesRead; i+=10) {
            cout << i << ":\t" << buffer[i] << endl;
            this_thread::sleep_for(sleeptime);
        }
    }


    // ---- argument parsing
    // cout << "argument count:\t" << argc << endl;
    // cout << "arguments:" << endl;
    // for(int i = 0; i < argc; i++)
    // {
    //     cout << argv[i] << endl;
    // }

    // ---- input and stringstream to value
    // string in_string;
    // cout << "select command" << endl;
    // getline(cin, in_string);
    // double in_string_val;
    // stringstream(in_string) >> in_string_val;
    // cout << "value:\t" << in_string_val << endl;
    // cout << "type:\t" << sizeof(in_string_val) << endl;

    return 0;
}
