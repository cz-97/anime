import xml.etree.ElementTree as etree
from config import colors
from random import choice


def save_d_to_file(d_elements, file_path):
    root = etree.Element("i")
    for time, text in d_elements:
        p = f"{time},1,25,{choice(colors)},0,0,0,0"
        d = etree.SubElement(root, "d")
        d.set("p", p)
        d.text = text
    etree.ElementTree(root).write(file_path, encoding="utf-8", xml_declaration=True)


def get_comments_from_xml(file_path):
    return etree.parse(file_path).getroot().findall("d")
