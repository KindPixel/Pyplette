import pyaudio
import wave
import keyboard
import time

def record_audio(output_filename, sample_rate=44100, chunk=1024):
    audio_format = pyaudio.paInt16  # 16-bit resolution
    channels = 1  # 1 channel for mono
    audio = pyaudio.PyAudio()
    frames = []

    def callback(in_data, frame_count, time_info, status):
        frames.append(in_data)
        return (in_data, pyaudio.paContinue)

    stream = audio.open(format=audio_format, channels=channels,
                        rate=sample_rate, input=True,
                        frames_per_buffer=chunk, stream_callback=callback)
    stream.start_stream()

    print("Recording... Press and hold the spacebar to record.")

    while not keyboard.is_pressed('space'):
        time.sleep(0.1)

    print("Recording started...")

    while keyboard.is_pressed('space'):
        time.sleep(0.1)

    print("Recording stopped.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(audio_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))