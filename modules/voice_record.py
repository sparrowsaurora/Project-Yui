import pyaudio
import wave
import keyboard  # Install with: pip install keyboard

def record_audio_wav(filename, rate=44100, chunk=1024):
    # Set up the parameters for recording
    audio_format = pyaudio.paInt16  # 16-bit resolution
    channels = 1                    # Mono audio
    sample_rate = rate               # 44.1kHz sample rate
    chunk_size = chunk               # 1024 samples per chunk

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Start Recording
    print("Recording... Press Enter to stop.")
    stream = p.open(format=audio_format, channels=channels,
                    rate=sample_rate, input=True,
                    frames_per_buffer=chunk_size)

    frames = []

    try:
        while True:
            if keyboard.is_pressed('enter'):  # Stop recording when Enter key is pressed
                print("Recording stopped.")
                break
            data = stream.read(chunk_size)
            frames.append(data)
    except KeyboardInterrupt:
        print("Recording interrupted.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio as a .wav file
    with wave.open(f"{filename}.wav", "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(audio_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {filename}.wav")

# Example usage: Record until Enter key is pressed and save it as "output.wav"
record_audio_wav("output")

