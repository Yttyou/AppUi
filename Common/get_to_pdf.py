# coding:utf8
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.pagesizes import A4, inch
import time


def GetPdf(data,filename):
    pdfmetrics.registerFont(TTFont('simhei', 'simhei.ttf'))  # 注册字体
    elements = []
    #记录表格信息
    # 标题
    style = getSampleStyleSheet()
    ct_title = style['Normal']
    ct_title.fontSize = 18
    ct_title.leading = 50
    ct_title.textColor = colors.black
    ct_title.alignment = 1
    title = Paragraph('SP Android', ct_title)
    href_style = []
    for i in data[1:]:
        url_link = ('HREF', (2, i[0]), (2, i[0]),i[3])
        href_style.append(url_link)
    data_pdf = []
    for i in data:
        if len(i)>4:
            i.pop(-2)
            data_pdf.append(i)
        else:
            data_pdf.append(i)
    #表格
    tab = Table(data_pdf, colWidths=[25, 45, 400, 45])
    style_list = [('FONTNAME', (0, 0), (-1, -1), 'simhei'), #全体文字
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTSIZE', (0, 0), (-1, -1), 8),  # 字体大小
                            ('TEXTCOLOR', (2, 1), (2, len(data)-1), colors.HexColor("#71A9E5")),
                           ('BACKGROUND', (0, 0), (-1, 0), colors.blue),  # 设置第一行的背景颜色
                           ('TEXTCOLOR', (0, 0), (-1, -0), colors.white),  # 设置字体颜色
                           ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5]
                           ]
    style_list.extend(href_style)
    tab.setStyle(TableStyle(style_list))
    #时间信息
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    ct_time = style['Normal']
    ct_time.fontSize = 10
    ct_time.leading = 40
    ct_time.textColor = colors.black
    ct_time.alignment = 0
    datetime_last = Paragraph(time_stamp, ct_time)

    #空白行
    ct_kongbai = style['Normal']
    ct_kongbai.textColor = colors.white
    ct_kongbai.fontSize = 10
    ct_kongbai.leading = 30
    ct_kongbai.alignment = 0
    kongbai = Paragraph('hello', ct_kongbai)

    #添加到元素
    elements.append(title)   #标题
    elements.append(tab)     #表格
    elements.append(kongbai) #空白行
    elements.append(datetime_last) #时间打印
    doc = SimpleDocTemplate(filename, pagesize=(A4[0], A4[1]), topMargin=1 * inch, bottomMargin=1 * inch,
                            leftMargin=0.6 * inch, rightMargin=0.6 * inch)
    doc.build(elements)
    return doc
