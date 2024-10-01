
import math

NUMBER_OF_CHANNELS = 12     # 
NUMBER_OF_TONES = 9         #
START_TONE = 64             # in Hz

f, i = 0, 0
while(NUMBER_OF_CHANNELS - i):
    
    print(f'channel number: {i+1}')
    i+=1
    while(NUMBER_OF_TONES - f):
        freq = START_TONE * pow(2,f)
        print(f'\tfrequency: {freq}')
        f+=1
    f = 0
i = 0



