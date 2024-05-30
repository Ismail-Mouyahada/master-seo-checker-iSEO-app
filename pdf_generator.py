from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from io import BytesIO
import streamlit as st

def generer_rapport_pdf(url, score_seo, score_performance, audits_seo):
    try:
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        elements = []

        elements.append(Paragraph("Rapport d'Analyse SEO Lighthouse", styles['Title']))
        elements.append(Paragraph(f"URL : {url}", styles['Normal']))
        elements.append(Spacer(1, 12))

        elements.append(Paragraph(f"Score SEO : {score_seo}", styles['Heading2']))
        elements.append(Paragraph(f"Score de Performance : {score_performance}", styles['Heading2']))
        elements.append(Spacer(1, 12))

        data_audit = [['Titre', 'Description', 'Score']]
        for audit in audits_seo:
            data_audit.append([Paragraph(audit['titre'], styles['Normal']), Paragraph(audit['description'], styles['Normal']), audit['score']])

        table_audit = Table(data_audit, colWidths=[100, 350, 50])
        table_audit.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table_audit)
        elements.append(Spacer(1, 12))
        elements.append(Paragraph("Créé par Ismail MOUYAHADA", styles['Normal']))
        doc.build(elements)
        buffer.seek(0)
        return buffer
    except Exception as e:
        st.toast(f"Erreur lors de la génération du rapport PDF : {e}", icon="⚠️")
        return None
