import requests
import json
import re
import dotenv

dotenv.load_dotenv()

def sentance(sentance:str) -> str :

    sl = "en"
    tl = "id"

    domain = "https://translate.google.com/m" # You could change the proxy here.
    translated_sentance = requests.get(f"{domain}?sl={sl}&tl={tl}&q={sentance}&hl={tl}").text

    pattern = r'<div[^>]*class="result-container"[^>]*>([\s\S]*?)</div>'
    match = re.search(pattern, r""+translated_sentance)

    return match.group(1).strip()
