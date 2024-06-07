#!/usr/bin/python
print('Content-type: text/html\n')


'''
TODO:
    create module to pass dict data between these 2 files
    '''

import cgitb
import cgi
import os
cgitb.enable()

csvs = os.listdir('/home/students/even/2026/astahl60/10-final-mother-s-house/data')

data = {}
HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Hello</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""

for j in csvs[:20]:
    if j[-4:] == '.csv':
        deck = {}
        f = open("/home/students/even/2026/astahl60/10-final-mother-s-house/data/" + j)
        lines = f.readlines()
        template = lines[0].split('$')
        n = 0
        for i in lines[1:]:
            i = i.replace("$$$$", "$").split('$')
            temp_dict = {}
            for q in i:
                temp_dict[template[n]] = q
                n += 1
            deck[i[1]] = temp_dict
            n = 0
        data[j[:-4]] = deck
        f.close()

def get_data():
    return data


html = HTML_HEADER
html += "<body style=\"display: flex; flex-direction: column; text-align: center;max-width: 300px;margin: auto\">"
html += '''
<form action="query.py" method="GET">
      <input type="text" name="search" value="Search for a deck.">
      <input type="submit" name="submit">
</form>
'''
for i in data:
    html += "<div style=\"background-color: #D3CCCB; border-radius: 20px; padding: 20px; margin-top: 50px\">"
    html += "<h2 style=\"text-align: center\">" + i + "</h2>"
    html += "<details style=\"text-align: center\">"
    for j in data[i]:
        html += "<h4>" + j + "</h4>"
        html += "<details style=\"text-align: center\">"
        html += "<summary>Card Data</summary>"
        for q in data[i][j]:
            html += "<h4>" + q + "</h4>"
            html += "<p>" + data[i][j][q] + "</p>"
        html += "</details>"
    html += "</details>"
    html += "</div>"


html += HTML_FOOTER
print(html)

search = cgi.FieldStorage()['search']
if search in data:
    ans = ''
    for j in data[i]:
        ans += "<h4>" + j + "</h4>"
        ans += "<details style=\"text-align: center\">"
        ans += "<summary>Card Data</summary>"
        for q in data[i][j]:
            ans += "<h4>" + q + "</h4>"
            ans += "<p>" + data[i][j][q] + "</p>"
        ans += "</details>"
    print(ans)
else:
    print('oh no')
