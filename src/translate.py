import requests
import json
import re
from options import options

def sentance(sentance:str) -> str :

    sl = "en"
    tl = "id"

    domain = options.proxy

    if "https://" not in domain :
        domain = "https://" + domain    

    translated_sentance = requests.get(f"{domain}/m?sl={sl}&tl={tl}&q={sentance}&hl={tl}").text

    try :
        pattern = r'<div[^>]*class="result-container"[^>]*>([\s\S]*?)</div>'
        match = re.search(pattern, r""+translated_sentance)

        return match.group(1).strip()
    
    except Exception as e :
        return f"Failed to Translate : {e}"
