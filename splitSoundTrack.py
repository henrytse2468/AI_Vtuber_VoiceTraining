import os
from datetime import datetime, timedelta
from getTimeStamp import getTimeStamp, getTranscipt
import wave

def timestamp_to_frames(timestamp, frame_rate):
    time_format = "%H:%M:%S.%f"
    dt = datetime.strptime(timestamp, time_format)
    total_seconds = dt.hour * 3600 + dt.minute * 60 + dt.second + dt.microsecond / 1e6
    return int(total_seconds * frame_rate)



def writeFileList(txt, wav):
    def split_audio_by_timestamp(input_file, output_folder, start_timestamp, end_timestamp):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        with wave.open(input_file, 'rb') as input_wave:
            frame_rate = input_wave.getframerate()
            start_frame = timestamp_to_frames(start_timestamp, frame_rate)
            end_frame = timestamp_to_frames(end_timestamp, frame_rate)

            input_wave.setpos(start_frame)
            frames = input_wave.readframes(end_frame - start_frame)

        output_file = os.path.join(output_folder, f"{input_file}_{start_frame}_{end_frame}.wav")
        output_file_list.append(f"{input_file}_{start_frame}_{end_frame}.wav")

        with wave.open(output_file, 'wb') as output_wave:
            output_wave.setnchannels(input_wave.getnchannels())
            output_wave.setsampwidth(input_wave.getsampwidth())
            output_wave.setframerate(frame_rate)
            output_wave.writeframes(frames)

    os.chdir('input_file')

    timestampList = getTimeStamp(txt)
    output_file_list = []
    
    for i in range(0, len(timestampList)-2):
        split_audio_by_timestamp(wav, '../output_folder', timestampList[i], timestampList[i+1])

    transcript = getTranscipt(txt)[:-2]
    pairedList = list(zip(output_file_list, transcript))
    output_file_path = 'train.txt'

    os.chdir('..')

    with open(output_file_path, 'a', encoding='utf-8') as file:
        for item in pairedList:
            line = f"{item[0]}|{item[1]}\n"
            file.write(line)

    print(f"Data written to {output_file_path}")


#writeFileList('HololiveTestTimeStamp.txt', 'HololiveTest1.wav')