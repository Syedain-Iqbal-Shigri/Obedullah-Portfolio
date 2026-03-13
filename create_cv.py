from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from PIL import Image as PILImage
import os

# Register fonts
pdfmetrics.registerFont(TTFont('Times New Roman', '/usr/share/fonts/truetype/english/Times-New-Roman.ttf'))
pdfmetrics.registerFont(TTFont('Calibri', '/usr/share/fonts/truetype/english/calibri-regular.ttf'))
registerFontFamily('Times New Roman', normal='Times New Roman', bold='Times New Roman')
registerFontFamily('Calibri', normal='Calibri', bold='Calibri')

# Page size
width, height = A4

# Create document
doc = SimpleDocTemplate(
    "/home/z/my-project/download/portfolio/Obedullah_CV.pdf",
    pagesize=A4,
    rightMargin=1.5*cm,
    leftMargin=1.5*cm,
    topMargin=1.5*cm,
    bottomMargin=1.5*cm,
    title='Obedullah_CV',
    author='Z.ai',
    creator='Z.ai',
    subject='Professional CV/Resume for Obedullah - UI/UX Designer'
)

# Styles
styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    'NameStyle',
    fontName='Times New Roman',
    fontSize=28,
    leading=34,
    alignment=TA_CENTER,
    textColor=colors.HexColor('#1a1a2e'),
    spaceAfter=4
)

title_style = ParagraphStyle(
    'TitleStyle',
    fontName='Times New Roman',
    fontSize=14,
    leading=18,
    alignment=TA_CENTER,
    textColor=colors.HexColor('#6366f1'),
    spaceAfter=8
)

contact_style = ParagraphStyle(
    'ContactStyle',
    fontName='Times New Roman',
    fontSize=10,
    leading=14,
    alignment=TA_CENTER,
    textColor=colors.HexColor('#6b6b8a'),
    spaceAfter=16
)

section_header_style = ParagraphStyle(
    'SectionHeader',
    fontName='Times New Roman',
    fontSize=14,
    leading=18,
    textColor=colors.HexColor('#1a1a2e'),
    spaceBefore=16,
    spaceAfter=8
)

body_style = ParagraphStyle(
    'BodyStyle',
    fontName='Times New Roman',
    fontSize=10,
    leading=14,
    alignment=TA_LEFT,
    textColor=colors.HexColor('#4a4a6a'),
    spaceAfter=4
)

skill_style = ParagraphStyle(
    'SkillStyle',
    fontName='Times New Roman',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#4a4a6a'),
)

story = []

# Header with Profile Image
try:
    # Get image dimensions
    pil_img = PILImage.open('/home/z/my-project/download/portfolio/profile.jpg')
    orig_w, orig_h = pil_img.size
    
    # Create header table with image and name
    img_width = 80
    img_height = img_width * (orig_h / orig_w)
    
    profile_img = Image('/home/z/my-project/download/portfolio/profile.jpg', width=img_width, height=img_height)
    
    header_data = [[
        profile_img,
        [
            Paragraph('<b>Obedullah</b>', name_style),
            Paragraph('UI/UX & Graphic Designer', title_style),
            Paragraph('obedullah.design@email.com | +1 234 567 8900', contact_style),
        ]
    ]]
    
    header_table = Table(header_data, colWidths=[90, width - 3*cm - 90])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('ALIGN', (1, 0), (1, 0), 'LEFT'),
        ('LEFTPADDING', (1, 0), (1, 0), 15),
    ]))
    
    story.append(header_table)
except:
    # Fallback without image
    story.append(Paragraph('<b>Obedullah</b>', name_style))
    story.append(Paragraph('UI/UX & Graphic Designer', title_style))
    story.append(Paragraph('obedullah.design@email.com | +1 234 567 8900', contact_style))

# Horizontal line
story.append(Spacer(1, 8))
line_data = [['']]
line_table = Table(line_data, colWidths=[width - 3*cm])
line_table.setStyle(TableStyle([
    ('LINEABOVE', (0, 0), (-1, 0), 2, colors.HexColor('#6366f1')),
]))
story.append(line_table)

# Professional Summary
story.append(Paragraph('<b>PROFESSIONAL SUMMARY</b>', section_header_style))
story.append(Paragraph(
    'Creative and detail-oriented UI/UX Designer with 5+ years of experience crafting intuitive digital experiences. '
    'Specialized in user-centered design, wireframing, prototyping, and brand identity development. '
    'Proven track record of delivering high-quality designs that enhance user engagement and drive business growth. '
    'Passionate about transforming complex ideas into visually stunning, functional interfaces.',
    body_style
))

# Experience
story.append(Paragraph('<b>PROFESSIONAL EXPERIENCE</b>', section_header_style))

exp_data = [
    ['Senior UI/UX Designer', '2021 - Present'],
    ['TechStart Solutions, San Francisco', ''],
]
exp_table = Table(exp_data, colWidths=[width - 5*cm, 3*cm])
exp_table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, -1), 'Times New Roman'),
    ('FONTSIZE', (0, 0), (0, 0), 11),
    ('FONTSIZE', (1, 0), (1, 0), 10),
    ('FONTSIZE', (0, 1), (-1, 1), 10),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0, 1), (-1, 1), colors.HexColor('#6366f1')),
    ('TEXTCOLOR', (1, 0), (1, 0), colors.HexColor('#6b6b8a')),
    ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
story.append(exp_table)
story.append(Paragraph(
    '• Led UI/UX design for 20+ web and mobile applications, increasing user engagement by 45%<br/>'
    '• Collaborated with product and engineering teams to deliver pixel-perfect designs<br/>'
    '• Conducted user research and usability testing to optimize user flows<br/>'
    '• Established design system standards reducing development time by 30%',
    body_style
))

story.append(Spacer(1, 8))

exp_data2 = [
    ['UI/UX Designer', '2019 - 2021'],
    ['Innovate Labs, New York', ''],
]
exp_table2 = Table(exp_data2, colWidths=[width - 5*cm, 3*cm])
exp_table2.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, -1), 'Times New Roman'),
    ('FONTSIZE', (0, 0), (0, 0), 11),
    ('FONTSIZE', (1, 0), (1, 0), 10),
    ('FONTSIZE', (0, 1), (-1, 1), 10),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0, 1), (-1, 1), colors.HexColor('#6366f1')),
    ('TEXTCOLOR', (1, 0), (1, 0), colors.HexColor('#6b6b8a')),
    ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
story.append(exp_table2)
story.append(Paragraph(
    '• Designed responsive web interfaces and mobile app UI for fintech products<br/>'
    '• Created brand identities and marketing collateral for 15+ startups<br/>'
    '• Developed interactive prototypes using Figma and Adobe XD',
    body_style
))

# Skills
story.append(Paragraph('<b>SKILLS</b>', section_header_style))

skills_data = [
    [Paragraph('<b>Design Tools:</b>', skill_style), Paragraph('Figma, Adobe XD, Sketch, Photoshop, Illustrator, InDesign', skill_style)],
    [Paragraph('<b>Core Skills:</b>', skill_style), Paragraph('UI/UX Design, Wireframing, Prototyping, User Research, Design Systems', skill_style)],
    [Paragraph('<b>Additional:</b>', skill_style), Paragraph('HTML/CSS, Brand Identity, Social Media Design, Motion Graphics', skill_style)],
]

skills_table = Table(skills_data, colWidths=[3*cm, width - 6*cm])
skills_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 0),
    ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ('TOPPADDING', (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
]))
story.append(skills_table)

# Education
story.append(Paragraph('<b>EDUCATION</b>', section_header_style))
edu_data = [
    ['Bachelor of Fine Arts in Graphic Design', '2015 - 2019'],
    ['University of Design Arts', ''],
]
edu_table = Table(edu_data, colWidths=[width - 5*cm, 3*cm])
edu_table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, -1), 'Times New Roman'),
    ('FONTSIZE', (0, 0), (0, 0), 11),
    ('FONTSIZE', (1, 0), (1, 0), 10),
    ('FONTSIZE', (0, 1), (-1, 1), 10),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0, 1), (-1, 1), colors.HexColor('#6366f1')),
    ('TEXTCOLOR', (1, 0), (1, 0), colors.HexColor('#6b6b8a')),
    ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
story.append(edu_table)

# Certifications
story.append(Paragraph('<b>CERTIFICATIONS</b>', section_header_style))
story.append(Paragraph(
    '• Google UX Design Professional Certificate (2023)<br/>'
    '• Adobe Certified Expert - Photoshop (2022)<br/>'
    '• Figma Advanced Prototyping (2023)',
    body_style
))

# Languages & Interests
story.append(Spacer(1, 8))
lang_int_data = [
    [Paragraph('<b>Languages:</b> English (Native), Spanish (Intermediate)', body_style),
     Paragraph('<b>Interests:</b> Photography, Travel, Art History', body_style)],
]
lang_table = Table(lang_int_data, colWidths=[(width - 3*cm)/2, (width - 3*cm)/2])
lang_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
story.append(lang_table)

# Build PDF
doc.build(story)
print("CV PDF created successfully!")
