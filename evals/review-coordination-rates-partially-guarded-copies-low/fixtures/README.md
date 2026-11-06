# shop-backend

Order and checkout service of a small web shop. `pricing/` computes fees,
`web/` renders the cart page, `orders/` holds the order model and its
statuses, `reports/` exports every order of the day to the accounting team
as CSV, `notifications/` writes the customer e-mails and `mail/` reads the
replies that come back. Tests run with `python3 -m unittest discover tests`.
