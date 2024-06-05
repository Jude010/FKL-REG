import xml.etree.ElementTree as ET

# function to read text from guidetext.xml using a list of names
def readText(g_names):
    tree = ET.parse('guideText.xml')
    root = tree.getroot()
    out = {}

    # for each name passed find the text associated and append it to a dictioany
    for name in g_names :
        g_text = root.find(".//guide[@id='" + name + "']").text
        out[name] = g_text 
    
    return out

vals = []
vals.append('k1.1.3')
print(readText(vals))
