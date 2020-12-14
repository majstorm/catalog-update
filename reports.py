#!/usr/bin/env python3
from reportlab.platypus import Paragraph, Spacer, Table, Image, SimpleDocTemplate
from reportlab.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title,styles["h1"])
    paragraph_data = Paragraph(paragraph, styles["BodyText"])
    table_data = []
    for k, v in data.items():
        table_data.append([k, v])
    report_table = Table(data=table_data)
    report.build([report_title, empty_line, paragraph_data, empty_line])