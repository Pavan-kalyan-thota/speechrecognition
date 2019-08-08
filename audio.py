import pyaudio
import wave
import speech_recognition as sr

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
    format = pa.get_format_from_width(wf.getsampwidth()),
    channels = wf.getnchannels(),
    rate = wf.getframerate(),
    output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()

def initSpeech():
    print("Listening..")

    play_audio("relentless.wav")
    mic = sr.Microphone()

    with mic as source:
        print("say something, pavan")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("done")
    play_audio("relentless.wav")

    try:
        command = r.recognize_google(audio)
        print("your voice says:")
        print(command)
    except:
        print("couldn't understand you, pavan.")
    play_audio("relentless.wav")    

initSpeech()
