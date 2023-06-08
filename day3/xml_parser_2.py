# Exercises: https://www.hackerrank.com/challenges/html-parser-part-2/

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if len(data.split("\n")) > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data.rstrip())

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
a = parser.feed(html)
parser.close()
