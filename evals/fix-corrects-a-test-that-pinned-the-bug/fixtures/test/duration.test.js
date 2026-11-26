const assert = require("assert");
const { formatDuration } = require("../src/duration");

assert.strictEqual(formatDuration(90), "1:30", "90 seconds");
assert.strictEqual(formatDuration(125), "2:5", "125 seconds");

console.log("duration.test.js: all tests passed");
