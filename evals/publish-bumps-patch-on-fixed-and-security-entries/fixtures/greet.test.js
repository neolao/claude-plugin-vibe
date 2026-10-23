const assert = require('assert');
const { greet } = require('./greet');

assert.strictEqual(greet('Ada'), 'Hello, Ada!');
assert.strictEqual(greet('A\u0007da'), 'Hello, Ada!');
console.log('ok');
