-- Applied by the deploy pipeline before the API starts.
CREATE TABLE invoices (
    id            SERIAL PRIMARY KEY,
    reference     TEXT NOT NULL UNIQUE,
    currency      CHAR(3) NOT NULL CHECK (currency IN ('EUR', 'USD', 'GBP')),
    amount_cents  INTEGER NOT NULL CHECK (amount_cents > 0),
    created_at    TIMESTAMP NOT NULL DEFAULT now()
);
