import { test } from "node:test";
import assert from "node:assert/strict";

import { billingAddress, invoiceTotal } from "../src/billing/invoice.js";

test("sums the lines", () => {
  assert.equal(invoiceTotal([{ unitCents: 250, qty: 2 }, { unitCents: 100, qty: 1 }]), 600);
});

test("resolves the billing address", () => {
  const directory = { find: async () => ({ address: "1 Main St" }) };
  billingAddress(directory, "c-1").then((address) => assert.equal(address, "1 Main St"));
});

test("rejects an unknown customer", async () => {
  const directory = { find: async () => null };
  try {
    await billingAddress(directory, "c-404");
  } catch (error) {
    assert.match(error.message, /unknown customer c-404/);
  }
});
