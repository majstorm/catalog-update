#!/usr/bin/env python3
from reportlab.platypus import Paragraph, Spacer, Table, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title,styles["h1"])
    paragraph_data = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title, paragraph_data])
