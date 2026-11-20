// Storefront API: lists the products and their delivery estimate.
const express = require('express');
const { addBusinessDays, formatISO } = require('date-fns');

const products = require('./products.json');

const app = express();

app.get('/products', (req, res) => {
  const shippedBy = formatISO(addBusinessDays(new Date(), 2), { representation: 'date' });
  res.json(products.map((p) => ({ ...p, shippedBy })));
});

app.listen(process.env.PORT || 3000);
