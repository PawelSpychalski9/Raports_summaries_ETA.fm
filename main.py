import openai
from googletrans import Translator

key = "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"

#API key validation - exceptions handling
while True:
    openai.api_key = key
    try:
        openai.Completion.create(model="text-davinci-002", prompt="Test", max_tokens=1)
        print("Klucz API jest poprawny.")
        break

    except Exception as e:
        print(f"Błąd API: {e}")
        print("Klucz API jest niepoprawny. Proszę podać nowy klucz.")
        api_key = input("podaj nowy klucz API: ")


def ask_GPT(og_text):
#asking GPT model to summarize the text
    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
        {
          "role": "system",
          "content": "You will receive the text of the article your task will be to write a summary of this article in such a way that it can be provided to our website as a report writen by us and translate this into Polsih. Return only polish text. Do not use frazes like 'according to the article' or 'the article says'."
        },
        {
          "role": "user",
          "content": og_text
        }
      ],
      temperature=0,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    odpowiedz = response.choices[0].message['content']
    return odpowiedz

#header translation
def translate_english_to_polish(text):
  try:
    translator = Translator()
    translation = translator.translate(text, src='en', dest='pl')
    return translation.text
  except Exception as e:
    return str(e)

while True:
    print("\n")
    title = input("Enter the title of the article: ")
    og_text = input("Enter the text you want to summarize: ")

    if og_text == "exit":
        break

    # Pobranie odpowiedzi z atrybutu 'choices' w odpowiedzi od API

    # response print
    print("\n")
    print(translate_english_to_polish(title))
    print(ask_GPT(og_text))
    odpowiedz = ask_GPT(og_text)


    #file appending
    with open("bbb", "a", encoding="utf-8") as file:
      file.write('<h2 style="font-family: \'Poppins\', sans-serif; color: #4a4a4a; font-size: 1.2em;">')
      file.write(translate_english_to_polish(title))
      file.write('</h2> \n')
      file.write('<p style="font-family: \'Poppins\', sans-serif; line-height: 2;">')
      file.write(odpowiedz)
      file.write('</p> \n <div style="margin-top: 100px;"></div> \n \n \n \n')
