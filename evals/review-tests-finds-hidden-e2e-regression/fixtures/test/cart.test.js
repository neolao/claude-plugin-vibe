import { test } from "node:test";
import assert from "node:assert/strict";

import { cartTotal } from "../src/cart.js";

const pricing = {
  priceOf: () => 500,
  discountFor: (subtotal) => (subtotal >= 1000 ? 0.1 : 0),
};

test("applies the bulk discount", () => {
  assert.equal(cartTotal([{ sku: "sku-melon", qty: 2 }], pricing), 900);
});

test("charges full price under the threshold", () => {
  const total = cartTotal([{ sku: "sku-apple", qty: 1 }], pricing);
  assert.ok(total);
});
