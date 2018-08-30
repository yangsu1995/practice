#coding:utf8
class HtmlOutPuter(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        font=open('output.html', 'w' ,encoding="utf-8")

        font.write("<html>")
        font.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        font.write("<body>")
        font.write("<table>")

        for data in self.datas:
            font.write("<tr>")
            font.write("<td>%s</td>" % data['url'])
            font.write("<td>%s</td>" % data['title'])
            font.write("<td>%s</td>" % data['summary'])
            font.write("</tr>")

        font.write("</table>")
        font.write("</body>")
        font.write("</html>")
        font.close()
