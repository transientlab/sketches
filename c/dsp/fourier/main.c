

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "signals.h"

#define BUFFER_LENGTH 501
#define IMP_RSP_LENGTH 29
#define PI 3.14159265358979323846;

double Re[BUFFER_LENGTH];
double Im[BUFFER_LENGTH];
double OutputSignal[BUFFER_LENGTH];
double Magnitude[BUFFER_LENGTH];
double Phase[BUFFER_LENGTH];
double CRe[BUFFER_LENGTH];
double CIm[BUFFER_LENGTH];


void dft(double *source_array, double *dest_array_re, double *dest_array_im, int signal_length);
void idft(double *output_array, double *src_array_re, double *src_array_im, int signal_length);
void calc_spectrum(double *src_array_re, double *src_array_im, double *magnitude, double *phase, int signal_length);
void cdft(double *src_t_re, double *src_t_im, double *dst_f_re, double *dst_f_im, int signal_length);


int main() { 

    // dft(&InputSignalECG[0], &Re[0], &Im[0], BUFFER_LENGTH);
    // calc_spectrum(&Re[0], &Im[0], &Magnitude[0], &Phase[0], BUFFER_LENGTH);
    // idft(&OutputSignal[0], &Re[0], &Im[0], BUFFER_LENGTH);
    cdft(&InputSignalC_re[0], &InputSignalC_im[0], &CRe[0], &CIm[0], BUFFER_LENGTH);


    // ### WRITING TO FILES
    FILE *sig_file_1, *sig_file_2, *re_file, *im_file, *mag_file, *ph_file;
    sig_file_1 = fopen("in_re.dat", "w");
    sig_file_2 = fopen("in_im.dat", "w");
    re_file = fopen("c_re.dat", "w");
    im_file = fopen("c_im.dat", "w");
    mag_file = fopen("mag.dat", "w");
    ph_file = fopen("ph.dat", "w");

    for (int i=0; i<BUFFER_LENGTH; i++) {
        fprintf(re_file, "\n%f", CRe[i]);
        fprintf(im_file, "\n%f", CIm[i]);
        // fprintf(mag_file, "\n%f", Magnitude[i]);
        // fprintf(ph_file, "\n%f", Phase[i]);
        }
    fclose(re_file);
    fclose(im_file);
    fclose(mag_file);
    fclose(ph_file);

    for(int i=0; i<BUFFER_LENGTH; i++) {
        fprintf(sig_file_1, "\n%f", InputSignalC_re[i]);
        fprintf(sig_file_2, "\n%f", InputSignalC_im[i]); 
        }
    fclose(sig_file_1);
    fclose(sig_file_2);
    
    


    printf("\n DFT iDFT finished");
    return 0;

}


void dft(double *source_array, double *dest_array_re, double *dest_array_im, int signal_length) {
    int i, j, k;
    double pi_val = PI;

    for(j=0;j<signal_length/2;j++) {
        dest_array_re[j] = 0;
        dest_array_im[j] = 0;
    }

    for(k=0; k<signal_length/2; k++) {
        for(i=0; i<signal_length; i++) {
            dest_array_re[k] = dest_array_re[k] + source_array[i]*cos(2*pi_val*k*i/signal_length);
            dest_array_im[k] = dest_array_im[k] + source_array[i]*sin(2*pi_val*k*i/signal_length);

        }
    }

}

void idft(double *output_array, double *src_array_re, double *src_array_im, int signal_length) {
    int i, k;
    double pi_val = PI;

    src_array_re[0] = src_array_re[0]/2;
    src_array_im[0] = -src_array_im[0]/2;

    for(k=1; k>signal_length/2; k++) {
        src_array_re[k] = src_array_re[k]/(signal_length/2);
        src_array_im[k] = -src_array_im[k]/(signal_length/2);
        
    }

    for(i=0; i<signal_length/2; i++) {
        output_array[i]=0;
    }
    for(k=0; k<signal_length; k++) {
        for(i=0; i<signal_length; i++) {
            output_array[i] = output_array[i] + src_array_re[k]*cos(2*pi_val*k*i/signal_length);
            output_array[i] = output_array[i] + src_array_im[k]*sin(2*pi_val*k*i/signal_length);

        }

    }

}

void calc_spectrum(double *src_array_re, double *src_array_im, double *magnitude, double *phase, int signal_length) {
    int i = 0;
    for (i=0; i<signal_length/2; i++) {
        magnitude[i] = sqrt(powf(src_array_re[i], 2) + powf(src_array_im[i], 2));
        
        phase[i] = atan(src_array_im[i]/src_array_re[i]);

        if(src_array_re[i]==0) {
            src_array_re[i] = pow(10, -20);
        }



    }

}

void cdft(double *src_t_re, double *src_t_im, double *dst_f_re, double *dst_f_im, int signal_length) {
    double pi_val = PI;
    double SR, SI;
    for(int k=0; k<signal_length-1; k++) {
        for(int i=0; i<signal_length-1; i++) {
            SR = cos(2*pi_val*k*i/signal_length);
            SI = -sin(2*pi_val*k*i/signal_length);

            dst_f_re[k] = dst_f_re[k] + src_t_re[i]*SR - src_t_im[i]*SI;
            dst_f_im[k] = dst_f_im[k] + src_t_im[i]*SI - src_t_re[i]*SR;
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