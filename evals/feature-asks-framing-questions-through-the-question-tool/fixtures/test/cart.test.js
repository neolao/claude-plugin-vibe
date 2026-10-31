const assert = require("assert");
const { orderTotal } = require("../src/cart");

assert.strictEqual(orderTotal([]), 0);
assert.strictEqual(
  orderTotal([
    { priceCents: 1250, quantity: 2 },
    { priceCents: 499, quantity: 1 },
  ]),
  2999
);
assert.throws(() => orderTotal(null), /expects an array/);
assert.throws(() => orderTotal([{ priceCents: 1.5, quantity: 1 }]), /integer/);

console.log("cart tests passed");
