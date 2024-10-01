#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "signals.h"

#define BUFFER_LENGTH 320
#define IMP_RSP_LENGTH 29
#define PI 3.14159265358979323846
#define KERNEL_LENGTH 50


double OutputSignal[BUFFER_LENGTH];
double LoCutoffKernel[KERNEL_LENGTH];
double UpCutoffKernel[KERNEL_LENGTH];
double KernelArray[KERNEL_LENGTH];

// prototypes
void lp_wsinc(double *source_array, double  *dest_array, double *kernel, double cutoff, int filter_length, int signal_length);
void bp_wsinc(double *source_array, double  *dest_array, double *kernel, double *lo_cutoff, double *up_cutoff, double lo_cutoff_freq, double up_cutoff_freq, int filter_length, int signal_length);

int main() { 


    bp_wsinc(&InputSignal_1_15[0], &OutputSignal[0], &KernelArray[0], &LoCutoffKernel[0], &UpCutoffKernel[0], 0.002, 0.11, KERNEL_LENGTH, BUFFER_LENGTH);

    // ### WRITING TO FILES
    FILE *sig_file_1, *sig_file_2, *kernel_file;
    sig_file_1 = fopen("in.dat", "w");
    sig_file_2 = fopen("out.dat", "w");
    kernel_file = fopen("kernel.dat", "w");


    for (int i=0; i<KERNEL_LENGTH; i++) {
        fprintf(kernel_file, "\n%lf", KernelArray[i]);
        }

    for(int i=0; i<BUFFER_LENGTH-KERNEL_LENGTH; i++) {
        fprintf(sig_file_1, "\n%lf", InputSignal_1_15[i]);
        }
    for(int i=KERNEL_LENGTH; i<BUFFER_LENGTH; i++) {
        fprintf(sig_file_2, "\n%lf", OutputSignal[i]); 
        }
    fclose(sig_file_1);
    fclose(sig_file_2);
    
    


    printf("\n filtered");
    return 0;

}

void lp_wsinc(double *source_array, 
            double  *dest_array, 
            double *kernel, 
            double cutoff_freq, 
            int filter_length, 
            int signal_length) {

    // nyquist freq = 24kHz -> 0.5 normalized
    double pi_val = PI;

    for(int i=0; i<filter_length; i++) {
        if (i-filter_length/2 != 0) {
            kernel[i] = sin(2*pi_val*cutoff_freq*(i-filter_length/2))/(i-filter_length/2);
            kernel[i]=kernel[i]*(0.54-0.46*cos(2*pi_val*i/filter_length));
        }
        else if (i-filter_length/2 == 0) {
            kernel[i] = 2*pi_val*cutoff_freq;
        }
    }

    for(int j = filter_length; j<signal_length; j++) {
        dest_array[j] = 0;
        for(int i=0; i<filter_length; i++) {
            dest_array[j] = dest_array[j] + source_array[j-i]*kernel[i];
        }
    }

}



void bp_wsinc(double *source_array, 
            double  *dest_array, 
            double *kernel, 
            double *lo_cutoff, 
            double *up_cutoff,
            double lo_cutoff_freq,
            double up_cutoff_freq,
            int filter_length, 
            int signal_length) {

    // nyquist freq = 24kHz -> 0.5 normalized
    double pi_val = PI;

        //lower cutoff
    for(int i=0; i<filter_length; i++) {
        
        if (i-filter_length/2 == 0) {
            lo_cutoff[i] = 2*pi_val*lo_cutoff_freq;
        }
        else { // (i-filter_length/2 != 0) {
            lo_cutoff[i] = sin(2*pi_val*lo_cutoff_freq*(i-filter_length/2))/(i-filter_length/2);
            lo_cutoff[i]=lo_cutoff[i]*(0.42-0.5*cos(2*pi_val*i/filter_length));
        }
    }


        //upper cutoff
    for(int i=0; i<filter_length; i++) {
        
        if (i-filter_length/2 == 0) {
            up_cutoff[i] = 2*pi_val*up_cutoff_freq;
        }
        else { // (i-filter_length/2 != 0) {
            up_cutoff[i] = sin(2*pi_val*up_cutoff_freq*(i-filter_length/2))/(i-filter_length/2);
            up_cutoff[i]=up_cutoff[i]*(0.42-0.5*cos(2*pi_val*i/filter_length));
        }
    }

        //spectral inversion lp -> hp
    for(int i=0; i<filter_length; i++) {
        up_cutoff[i] = -(up_cutoff[i]);
    }
    up_cutoff[filter_length/2] = up_cutoff[filter_length/2]+1;

        //create kernel, add lp+hp -> bandstop
    for(int i=0; i<filter_length; i++) {
        kernel[i] = up_cutoff[i] + lo_cutoff[i];
    };

        //spectral inversion of kernel bs -> bp
    for(int i=0; i<filter_length; i++) {
        kernel[i] = -(kernel[i]);
        }
    kernel[filter_length/2] = kernel[filter_length/2]+1;

        //convolve input&kernel
    for(int j = filter_length; j<signal_length; j++) {
        dest_array[j] = 0;
        for(int i=0; i<filter_length; i++) {
            dest_array[j] = dest_array[j] + source_array[j-i]*kernel[i];
        }
    }

}



/*
add filter iresponses -> bandstop/bandreject
convolve filter iresponses -> bandpass
 

        time                freq            custom
FIR:    moving average      windowed-sinc   custom fir
IIR:    single pole         Chebyshev       custom iir
  
*/
