from xml.dom import minidom

f = 'media/sen1.xml'
xmldoc = minidom.parse(f)
print(xmldoc)