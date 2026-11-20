// Renders the catalog pages from the API's JSON export into dist/.
const fs = require('node:fs');
const { format } = require('date-fns');
const { groupBy, sortBy } = require('lodash');

const products = JSON.parse(fs.readFileSync('export/products.json', 'utf8'));
const byCategory = groupBy(sortBy(products, 'name'), 'category');

fs.mkdirSync('dist', { recursive: true });
for (const [category, items] of Object.entries(byCategory)) {
  const rows = items.map((p) => `<li>${p.name} — ${p.price} €</li>`).join('\n');
  const generated = format(new Date(), 'yyyy-MM-dd');
  fs.writeFileSync(`dist/${category}.html`, `<h1>${category}</h1>\n<ul>\n${rows}\n</ul>\n<p>${generated}</p>\n`);
}
