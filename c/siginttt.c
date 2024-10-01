#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void handle_sigint(int signal) {
    if (signal == SIGINT) {
        printf("\b\bUser interrupt\n\n");
        exit(0);
    }
}

int main () {
    signal(SIGINT, handle_sigint);

    while(1) {
        printf("\b\bwaiting for SIGINT..\n");
        sleep(1);
    }
    return 0;
}