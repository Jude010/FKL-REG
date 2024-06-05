import xml.etree.ElementTree as ET

# function to read text from guidetext.xml using 
def readText(g_names):
    tree = ET.parse('~/TGDsite/resources/guideText.xml')
    root = tree.getroot()

    # for each name passed find the text associated and append it to a dictioany
    for name in g_names :
        g_text = root.find(".//guide[@id='" + name + "']").text
    