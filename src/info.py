import os
from options import options as opt
import json

file_script_location = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(file_script_location, "languages/languages.json")) as file :
    languages = json.load(file)
