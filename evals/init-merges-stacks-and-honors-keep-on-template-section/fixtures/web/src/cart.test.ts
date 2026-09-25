import { describe, expect, it } from "vitest";
import { cartTotal } from "./cart";

describe("cartTotal", () => {
  it("returns 0 for an empty cart", () => {
    expect(cartTotal([])).toBe(0);
  });
});
