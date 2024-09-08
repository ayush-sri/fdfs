import speak
def main():
  # speech = sr.Recognizer()
  # with sr.Microphone() as source:#with keyword is used for automatically ending the microphone
  #   print("Say something !")
  #   audio = speech.listen(source)
  #   print("Done !")
  try:
    # text = speech.recognize_google(audio)
    # print("you said : "+text)
    lang = 'en'
    speak.tts("welcome to the movie rating app",lang)

  except Exception as e:
    print(e)

if __name__ == '__main__':
    main()