import subprocess

LABEL_HTML = """<html><body>
<h1>{recipient_name}</h1>
<p>{street}<br>{postcode} {city}</p>
<p>Tracking: {tracking_number}</p>
</body></html>"""


def render_pdf(shipment):
    """Returns the shipment's 4x6 inch label as PDF bytes."""
    html = LABEL_HTML.format(**shipment)
    result = subprocess.run(
        ["wkhtmltopdf", "--page-width", "4in", "--page-height", "6in", "-", "-"],
        input=html.encode(),
        capture_output=True,
        check=True,
        timeout=30,
    )
    return result.stdout
