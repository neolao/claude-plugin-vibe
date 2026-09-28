import { test } from "node:test";
import assert from "node:assert/strict";

import { cartTotal } from "../src/cart.js";

test("small order through the real catalog", () => {
  assert.equal(cartTotal([{ sku: "sku-apple", qty: 2 }]), 300);
});

test("bulk order through the real catalog", () => {
  assert.equal(cartTotal([{ sku: "sku-melon", qty: 2 }]), 1620);
});
