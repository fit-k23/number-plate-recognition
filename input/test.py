from lxml import etree as ET

root = ET.Element('Doc')
level1 = ET.SubElement(root, 'S')
main = ET.SubElement(level1, 'Text')
main.text = 'Thanks for contributing an answer to Stack Overflow!'
second = ET.SubElement(level1, 'Tokens')
level2 = ET.SubElement(second, 'Token', word=u"low")


level3 = ET.SubElement(level2, 'Morph')
second1 = ET.SubElement(level3, 'Lemma')
second1.text = 'sdfs'
second1 = ET.SubElement(level3, 'info')
second1.text = 'qw'

level4 = ET.SubElement(level3, 'Aff')
second1 = ET.SubElement(level4, 'Type')
second1.text = 'sdfs'
second1 = ET.SubElement(level4, 'Suf')
second1.text = 'qw'

tree = ET.ElementTree(root)
tree.write('output.xml', pretty_print=True)