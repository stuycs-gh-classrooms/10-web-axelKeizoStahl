#!/usr/bin/python
print('Content-type: text/html\n')
import main

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

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

data = main.get_data()

search = cgi.FieldStorage()['search']
ans = ''
if search in data:
    for j in data[i]:
        ans += "<h4>" + j + "</h4>"
        ans += "<details style=\"text-align: center\">"
        ans += "<summary>Card Data</summary>"
        for q in data[i][j]:
            ans += "<h4>" + q + "</h4>"
            ans += "<p>" + data[i][j][q] + "</p>"
        ans += "</details>"
else:
    ans = '<h3>RESULT NOT FOUND</h3>'

ans += HTML_FOOTER
print(ans)
