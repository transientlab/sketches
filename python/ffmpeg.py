import os
import subprocess

os.chdir(os.path.dirname(__file__))
directory = os.getcwd()
input_files = []
for input_file in os.listdir():
    if input_file.endswith('mp4'):
        input_files.append(input_file.split('.')[0])

for i in input_files: print(i)

# choose what to do
commands = 'ec'

extract_audio_cmd = 'ffmpeg -i {} -vn -c:a copy -async 1 {}'
convert_audio_cmd = 'ffmpeg -i {} -c:a pcm_s16le {}'
replace_audio_cmd = 'ffmpeg -i {} -i {} -c:v copy -map 0:v:0 -c:a aac -map 1:a:0 -async 1 -to 01:00:15 {}'
scrop_vid_cmd = 'ffmpeg -i {} -vf "crop=2880:1620:480:100" -s 1920x1080 -b:v 2M {}' # 16:9
scrop_vid_cmd = 'ffmpeg -i {} -vf "crop=3072:1728:384:188" -s 1920x1080 -b:v 2M {}' # 16:9
scrop_vid_cmd = 'ffmpeg -i {} -vf "crop=2688:1680:576:180, scale=1920:-1" -b:v 2M -async 1 -to 1:00:15 {}' # 16:10
gen_test_signal = 'ffmpeg -f lavfi -i testsrc=size=3840x2160:rate=60 -f lavfi -i anullsrc=r=48000:cl=stereo -c:v libx264 -preset fast -tune zerolatency -b:v 40M -c:a aac -b:a 192k -pix_fmt yuv420p -t 10 output_4k60_test.mp4'
play_fs_in_loop = 'ffplay -loop 0 -fs {}'
delay_audio_per_channel = 'ffmpeg -i input.mp4 -filter_complex "[0:a]adelay=1000|2000|3000|4000|5000|6000[a]" -map 0:v -map "[a]" -c:v copy -c:a aac output.mp4'

for file in input_files:
    
    if 'e' in commands:
        cmd = extract_audio_cmd.format(file+'.mp4', file+'.aac')
    elif 'c' in commands:
        cmd = extract_audio_cmd.format(file+'.aac', file+'.wav')
    elif 'r' in commands:
        cmd = replace_audio_cmd.format(file+'.mp4', file+'.wav', 'new_'+file+'.mp4')
    elif 's' in commands:
        cmd = scrop_vid_cmd.format(file+'.mp4', 'scaled_'+file+'.mp4')
    else:
        cmd = f'ffprobe -i {file}'
    print(f"\n\n ---------------------------- \n {file} \n {cmd} \n")
    subprocess.call(cmd, shell=True)
    
    


