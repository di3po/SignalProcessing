#b1 is about: multiplied 1 to dur

import wave
import struct

w = wave.open('C:/Users/Dinara/Desktop/Kuanysh_1_tel.wav', 'rb')
n = w.getnframes()
binarr = []
mx = 0
mn = 0

def output_wave(path, frames):
    output = wave.open(path,'w')
    output.setparams(1,2,16000,1)
    output.writeframes(frames)
    output.close()

for i in range(0, n):
    #a = int.from_bytes(w[i])
     b = w.readframes(1)
     a = int.from_bytes(b, byteorder = 'big', signed = True)/65535
     if a > mx:
         mx = a
     if a < mn:
         mn = a
#print(mx, mn)



     #if abs(a) >= 0.1:
     if a >= 0.2*(mx+mn)/2:
         binarr.append(1)
     else:
         binarr.append(0)

start_i = end_i = 0
#dur = [end_i-start_i]
flag = 0
A = binarr
#A = [1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1]
#n = 16
#print('elements length before: ', len(binarr))
for i in range(0, n):
    if A[i] == 0:
        #print('0 is here : ', i)
        if (start_i == end_i) and (flag == 0):
            start_i = end_i = i
            flag = 1
        else:
            end_i += 1

    else:
        if flag == 1:
            dur = end_i - start_i + 1
            if dur > 1:
                midp = (int)((start_i + end_i)/2)
                #print('Midp1 : ', midp)
                binarr.pop(midp)
            flag = 0
            start_i = end_i = i
            #print('Dur : ', dur)
            #print('elements: ', binarr)
            #print('elements length after: ', len(binarr))

    if i == n-1:
        if flag == 1:
            dur = end_i - start_i + 1
            if dur > 1:
                midp2 = (int)((start_i + end_i)/2)
                #print('Midp2 : ', midp2)
                binarr.pop(midp2)
            flag = 0
            start_i = end_i = i
            #print('Dur : ',dur)
            #print('elements: ', binarr)
    #print('elements length after: ', len(A))
    #k = int("".join(map(str, A)),2)
    #print(k)
    packedData = map(lambda v:struct.pack('h',v), A)
    frames = b''.join(packedData)
    output_wave('C:/Users/Dinara/Desktop/example.wav', frames)
print(len(A))
    #
# C = binarr.writeframes()
k = int("".join(map(str, A)),2)
print(k)
packedData = map(lambda v:struct.pack('h',v), A)
frames = b''.join(packedData)
output_wave('C:/Users/Dinara/Desktop/example.wav', frames)

# Read audio data.
#frames = binarr.readframes()
#print(len(frames))    # Read n_frames new frames.
#assert len(frames) == sample_width * n_frames

# Duplicate to a new WAV file.
# with wave.open("path_to_new_wav_file.wav", "wb") as wav_file:    # Open WAV file in write-only mode.
#     # Write audio data.
#     params = (n_channels, sample_width, framerate, n_frames, comp_type, comp_name)
#     wav_file.setparams(params)
#     wav_file.writeframes(frames)
