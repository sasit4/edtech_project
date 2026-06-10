
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.colors import navy, gold, black
from reportlab.lib.pagesizes import letter


def generate_certificate(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

    p = canvas.Canvas(response, pagesize=letter)

    width, height = letter

    # Outer Border
    p.setStrokeColor(navy)
    p.setLineWidth(8)
    p.rect(30, 30, width - 60, height - 60)

    # Inner Border
    p.setStrokeColor(gold)
    p.setLineWidth(3)
    p.rect(50, 50, width - 100, height - 100)

    # Certificate Title
    p.setFont("Helvetica-Bold", 32)
    p.setFillColor(navy)
    p.drawCentredString(width / 2, 700, "CERTIFICATE")

    p.setFont("Helvetica", 20)
    p.setFillColor(black)
    p.drawCentredString(width / 2, 660, "OF COMPLETION")

    # Subtitle
    p.setFont("Helvetica", 16)
    p.drawCentredString(
        width / 2,
        600,
        "This certificate is proudly presented to"
    )

    # Student Name
    p.setFont("Helvetica-Bold", 30)
    p.setFillColor(gold)
    p.drawCentredString(
        width / 2,
        540,
        request.user.username
    )

    # Course Completion Text
    p.setFillColor(black)
    p.setFont("Helvetica", 16)
    p.drawCentredString(
        width / 2,
        490,
        "For Successfully Completing the Course"
    )

    # Platform Name
    p.setFont("Helvetica-Bold", 22)
    p.setFillColor(navy)
    p.drawCentredString(
        width / 2,
        440,
        "EdTech Learning Platform"
    )

    # Signature Lines
    p.line(120, 180, 250, 180)
    p.line(360, 180, 500, 180)

    p.setFont("Helvetica", 14)
    p.setFillColor(black)

    p.drawString(150, 160, " Mentor")
    p.drawString(410, 160, " Head")

    # Footer Text
    p.setFont("Helvetica-Oblique", 12)
    p.drawCentredString(
        width / 2,
        100,
        "Keep Learning • Keep Growing"
    )

    p.save()


    return response