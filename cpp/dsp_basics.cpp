#include <iostream>
#include <cmath>
#include <fstream>

#define BIT_DEPTH 8
#define VALS 10 //for valus in histogram, calculate based on BIT_DEPTH

// statistics is used to interpret aquired, numerical data
// probability is used to understand the underlying process

using namespace std;



int table[8] = {0, 2, 1, 3, 1, 4, 1, 5};

//statistics
// DC signal
float mean(int* start, int N)
{
    float sum = 0;
    for(int i = 0; i < N; i++)
    {
        sum += *(start + i);
    }
    return float(sum) / N;
}

// power of AC component
float variance(int* start, int N)
{
    float mn = mean(start, N);
    float sum =0;
    for(int i = 0; i < N-1; i++)
    {
        sum += pow((*(start + i) - mn), 2);
    }
    return sum / (N -1);
}

// better representation of AC amplitude
float standard_deviation(int* start, int N)
{
    return sqrt(variance(start, N));
}

float coefficient_of_variation(int* start, int N)
{
    return standard_deviation(start, N) / mean(start, N);
}

float typical_error(int* start, int N)
{
    return standard_deviation(start, N)/sqrt(N);
}

// histogram also displays the aquired noise by uneven distribution
//


// probability mass function ~ a histogram of infinite samples (probability density function for analog)
int hist[VALS];
void histogram(int* start, int N)
{
    
    for(int i = 0; i < N; i++)
    {
        hist[*(start+i)] += 1;
    }

    for(int i = 0; i < VALS - 1; i++)
    {
        cout << hist[i] << endl;
    }
}
// rewrite statistics as based on histogram, measure time

int main(int argc, char * argv[])
{   
    int vals = VALS;
    cout << vals << endl;
    int N = atoi(argv[1]);
    cout << "mean:\t\t" << mean(table, N) << endl;
    cout << "variance:\t" << variance(table, N) << endl;
    cout << "std_dev:\t" << standard_deviation(table, N) << endl;
    cout << "cv:\t\t" << coefficient_of_variation(table, N) << endl;
    cout << "error:\t\t" << typical_error(table, N) << endl;
    histogram(table, N);
    
    return 0;
}
