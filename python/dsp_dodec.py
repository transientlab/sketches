# 

from signal import signal
import numpy
import os
import datetime
# from .python import helper

GEOMETRY_SIZE = 12 # number of planes
IMPULSE_RESPONSE_LENGTH = 9600

# txt data
path_to_test_signals = ''
list_of_test_signals = [audio_file for audio_file in os.listdir(path_to_test_signals) \
    if audio_file.endswith('.wav')]
timestamp = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
io_output_channels, io_input_channels = [], [] # driver enumeration and names

# read audio data to buffers
signal_test, signal_response = [], []

# write output data from 1 speaker measurement
def txt_output_for_1_spk(measurement_results):
    text_file_path = measurement_results['sig_path']('/')[-1][:-4] + measurement_results['timestamp'] + '.txt'
    with open(text_file_path, 'r') as result_file:
        result_file.write('TIMESTAMP:\t\t' + measurement_results['timestamp'] + '\n\n')
        result_file.write('TEST SIGNAL:\t\t' + measurement_results['sig_path'] + '\n\n')
        result_file.write('IMPULSE RESPONSES:\n')
        for ir in measurement_results['irs']:
            result_file.write(ir + '\n')


# DEFINE direction() - cell-pole: shortest path to center
# DEFINE measure()
# DEFINE step_function(direction)
# DEFINE all_planes_path_sequence[]
# DEFINE numbering_planes
# DEFINE route-to-center[]
# START     put me on a plane -> set plane_number to 1
# CHOOSE    direction
# GO        1 step in direction to another plane -> plane number
# CALCULATE orientation

# define translation matrix: when x is source, what is added to other speakers
# transaltion by linear algebra
# testing module with 'active compensation'
# translation_matrix (cartesian or dodecahedian geometry)




# find sensitivity/level to confirm mic measurement position
# measure correlation 1 - {2:12}, when 1 is source
# measure transfer function
def measure_basic_params():
    return 0


# start with random, find ir pattern
# shortest path, high frequency
def guess_orientation_to_mic():
    frontal_spk_index = 0
    rotation = 0
    return frontal_spk_index, rotation



# make 1-to-GEOMETRY_SIZE measurement
def make_1_measurement(channel_name, timestamp, test_signal, geometry_size):
    measurement_results = { 'timestamp'  : timestamp,
                            'channel'   : channel_name,
                            'sig_path'  : '',
                            'irs'       : geometry_size*[1]
                    }
    for k in geometry_size:
        response_signal = []
        play_and_record_in_sync(test_signal, response_signal)
        ir = calculate_ir(test_signal, response_signal)
        measurement_results['irs'][k] = ir

    return measurement_results

def play_and_record_in_sync(playback_buffer, record_buffer):
    return 0

def calculate_ir(impulse, response):
    impulse_response = []
    return impulse_response




# with the same speakers in each wall ir_matrix should be like, 
# where a is ir(test_signal(measured_spk), measured_spk)
# 0 1 2 3 4 5 6 7 8 9 a b
# a b c d e f g h i j k l
# b a 
# c   a
# d     a
# e       a
# f         a
# g           a
# h             a
# i               a
# j                 a
# k                   a
# l                     a
def create_ir_matrix_from_measurements():
    return 0


# 12-dimensional space, defined by R (center : congruent-points, platonic)
# define translation from 3d to 12d
def switch_geometry(input_matrix):
    output_matrix = input_matrix
    return output_matrix