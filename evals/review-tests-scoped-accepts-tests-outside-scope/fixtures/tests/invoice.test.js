import { test } from "node:test";
import assert from "node:assert/strict";

import { billingAddress, invoiceTotal } from "../src/billing/invoice.js";

test("sums the lines", () => {
  assert.equal(invoiceTotal([{ unitCents: 250, qty: 2 }, { unitCents: 100, qty: 1 }]), 600);
});

test("rejects an empty invoice", () => {
  assert.throws(() => invoiceTotal([]), /empty invoice/);
});

test("resolves the billing address", async () => {
  const directory = { find: async () => ({ address: "1 Main St" }) };
  assert.equal(await billingAddress(directory, "c-1"), "1 Main St");
});

test("rejects an unknown customer", async () => {
  const directory = { find: async () => null };
  await assert.rejects(billingAddress(directory, "c-404"), /unknown customer c-404/);
});
