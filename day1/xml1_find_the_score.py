# Exercise: https://www.hackerrank.com/challenges/xml-1-find-the-score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node) -> int:
    """
    Function that calculates the total number of attributes in an XML tree.

    Args:
        node (xml.etree.ElementTree.Element): The root element of the XML tree.

    Returns:
        int: The total number of attributes in the XML tree.
    """
    return sum(len(el.attrib) for el in node.iter())


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))