import xml.etree.ElementTree as ET
from pathlib import Path

# function to read text from guidetext.xml using a list of names passed as a list of strings
def readText(g_names):
    path = Path('guideText.xml')
    tree = ET.parse(path)
    root = tree.getroot()
    out = {}

    # for each name passed find the text associated and append it to a dictionary
    for name in g_names :
        g_text = root.find(".//guide[@name='" + name + "']").text
        g_text = g_text.split("\n")
        out[name] = g_text 
    
    return out
