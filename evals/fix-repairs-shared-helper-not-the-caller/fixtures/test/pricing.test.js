const assert = require("assert");
const { lineTotal, orderTotal, applyDiscount } = require("../src/pricing");

assert.strictEqual(lineTotal({ price: 2.5, qty: 4 }), 10, "2.5 x 4 should be 10");
assert.strictEqual(
  orderTotal([
    { price: 1.5, qty: 2 },
    { price: 4, qty: 1 },
  ]),
  7,
  "order of 1.5 x 2 and 4 x 1 should be 7"
);
assert.strictEqual(applyDiscount(80, 25), 60, "25% off 80 should be 60");

console.log("pricing.test.js: all tests passed");
