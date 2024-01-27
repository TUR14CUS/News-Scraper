import requests
from send_mail import send_mail


topic = "samsung" # Enter your topic hereo

api_key = "526a7d61a08c4169bae38561ae84ba3f"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=526a7d61a08c4169bae38561ae84ba3f&" \
      "language=en"

request = requests.get(url)

contect = request.json()

body = ""
for article in contect["articles"][:20]:
    if article ["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article ["title"] + "\n" + article ["description"] + "\n" + article ["description"] + "\n" + article ["url"] + 2*"\n"
        
        
body = body.encode("utf-8")
send_mail(message=body)
