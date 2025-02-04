import requests
import json
import re
from info import opt, languages
import json
import sys
from copy import copy

list_to_str = lambda x : "".join(x)

def split_word( paragraph:str , word_per_line) -> str:

    words = [f"{word} " for word in paragraph.split(" ")] # Add space for each word
    copy_w = copy(word_per_line)

    index = 0
    for word in words :
        if index == word_per_line :
            words[index] = words[index] + "\n"      
            word_per_line = word_per_line + copy_w

        index += 1

    return list_to_str(words)

def search_language(langs) :
    for lang in langs :
        lang_id = languages[lang] if lang in languages.keys() else lang

        if lang_id not in languages.values() :
            raise ValueError("Invalid Language")
            sys.exit()
        
        else :
            yield lang_id

def sentance(sentance:str) -> str :

    sl, tl = search_language([opt.sl, opt.tl])

    domain = opt.proxy

    if "https://" not in domain :
        domain = "https://" + domain

    translated_sentance = requests.get(f"{domain}/m?sl={sl}&tl={tl}&q={sentance}&hl={tl}").text

    try :
        pattern = r'<div[^>]*class="result-container"[^>]*>([\s\S]*?)</div>'
        match = re.search(pattern, r""+translated_sentance)

        return split_word(match.group(1).strip(), opt.wordsWrap)
    
    except Exception as e :
        return f"Failed to Translate : {e}"
