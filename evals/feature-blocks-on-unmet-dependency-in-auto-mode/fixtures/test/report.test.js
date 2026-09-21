const assert = require("assert");
const { formatRow } = require("../src/report");

assert.strictEqual(formatRow("Coffee", 250), "Coffee: 2.50");
console.log("ok");
