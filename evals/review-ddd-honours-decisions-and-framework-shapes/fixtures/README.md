# webshop

Online shop back end. `orders/` holds the order model, its events, its
storage row and its repository, `catalog/` the products and their variants
mapped through SQLAlchemy and the nightly supplier import, `checkout/` the
use case behind the checkout page, `inventory/` the stock reservation,
`settings/` the shop preferences the admin page edits, and `api/` the Flask
routes.
