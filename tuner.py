import pyaudio, struct, numpy, time, math, os

drop_d = [73,110,147,196,247,330] # D A D G B e

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNEL = 1
RATE = 44100
string = 0
get_audio = pyaudio.PyAudio()
stream_audio = get_audio.open(
        format = FORMAT,
        channels = CHANNEL,
        rate = RATE,
        input = True,
        output = True,
        frames_per_buffer = CHUNK
    )

   
while True:
    data = stream_audio.read(CHUNK)
    data = sum(numpy.array(struct.unpack(str(2 * CHUNK) + "B", data), dtype='b')[::2] + 127)
    # data = sum(struct.unpack(str(2 * CHUNK) + "B", data))
    
    # try:
    #     old_data = data
    #     data = 12 * (math.log(data/220)/math.log(2)) + 57
        
    #     # print(sum(data))
    #     if (data < drop_d[string]):
    #         print("Tune up @ {}Hz".format(int(data)))
            
    #     if (data > drop_d[string]):
    #         print("Tune down @ {}Hz".format(int(data)))
    #     if (drop_d[string]-1 <= data <= drop_d[string]+1):
    #         os.system('cls')
    #         print("perfect tuning @ {}Hz".format(int(data)))
            
    #         if (string != 6):
    #             os.system("pause")
    #             string += 1
    #         else:
    #             break
    # except:
    #     pass
    # time.sleep(1)
    
    
