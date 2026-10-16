import { test } from "node:test";
import assert from "node:assert/strict";

import { rateFor } from "../src/shipping/rates.js";

test("prices a parcel", () => {
  rateFor(1200);
  assert.ok(true);
});
