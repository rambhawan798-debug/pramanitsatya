import speech_recognition as sr

def test_voice():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("sun rahe hain...kripy kuch boliye:")
      
        
        try:
            audio = r.listen(source, timeout=10)
            print("Aawaz record ho gayi, text me badla ja raha hai...")

            # Yahan language=hi-IN" hi rahega taaki Google aapki Hindi aawaz ko pehchaan sake
            text = r.recognize_google(audio,language="en-US")
            
            # Print karte samay roman/English style mein dikhayega taaki CMD mein ??? na aaye
            print("Aapne jo bola woh yeh hai -> " + text)

        except sr.WaitTimeoutError:
            print("Samay samapt ho gaya,aapne kuch nahi bola.")
        except sr.UnknownValueError:
            print("Aawaz samajh nahi aayi,kripya dobara saaf bolein.")
        except Exception as e:
            print("Koi takniki dikkat ya internet error aa gaya hai: " + str(e))

if __name__ == "__main__":
    test_voice() 