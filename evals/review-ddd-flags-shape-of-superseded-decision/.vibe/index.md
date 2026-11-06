# webshop

Online shop back end: the order model and its storage in `orders/`, the
product catalog mapped through SQLAlchemy in `catalog/`, the checkout use
case in `checkout/`, the Flask routes in `api/`.

## Modules
- `orders` — order aggregate, money, repository
- `catalog` — products and their variants, the supplier import
- `checkout` — place an order
- `api` — HTTP routes

## Decisions
- `decisions/001-buyer-kept-in-public-api.md`
- `decisions/002-customer-in-public-api.md`
