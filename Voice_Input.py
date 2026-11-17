import speech_recognition as sr

def capture_voice_input(): 
    recognizer = sr.Recognizer()
    try:
       	 with sr.Microphone() as source:
             print("pramanit satya AI sunraha hai... kripya boliye.")
             recognizer.adjust_for_ambient_noise(source,duration=1)
             audio_data = recognizer.listen(source,timeout=5, phrase_time_limit=10)
             print("Aawaz record ho gayi hai,ab ise text me badla ja raha hai...")
             return audio_data
    except Exception as e:
        print(f"tay samay me aawaz sunai nahi di:{e}")
        return None

if __name__ == "__main__":
   # pahle hisse ki testing ke liye
   capture_voice_input()