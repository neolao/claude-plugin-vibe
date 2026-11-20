from invoice_worker.render import render_pdf


def test_renders_one_line_per_invoice_line():
    invoice = {"lines": [{"label": "Hosting", "amount": 120}, {"label": "Support", "amount": 30.5}]}
    customer = {"name": "ACME"}
    assert render_pdf(invoice, customer) == b"ACME\nHosting: 120.00\nSupport: 30.50"
