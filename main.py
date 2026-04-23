import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GROUP_ID = os.getenv("GROUP_ID")

def send_telegram_message(chat_id, text):
    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.get(url, params=params)
    print(response.text)

def get_bible_quote(line):

    # Wir suchen Johannes 3, Vers 16
    # Nutze "John" statt "Johannes", um Fehler zu vermeiden
    stelle = line
    url = f"https://bible-api.com/{stelle}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Wir ziehen uns einfach nur den Text-Teil aus der Antwort
        text = data["text"]
        print(f"Bibelvers gefunden:\n{text}")
    else:
        print(f"Fehler: {response.status_code}")
    return text

if __name__ == "__main__":
    for counter in range(1,2):
        quote = "John 8:"+str(counter)
        text = get_bible_quote( quote )
        send_telegram_message(GROUP_ID,text)
