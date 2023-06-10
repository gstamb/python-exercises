# Exercise:https://www.hackerrank.com/challenges/xml-1-find-the-score


def get_attr_number(node):
    count = 0
    for child in node.iter():
        count+= len(child.attrib)
    return count

