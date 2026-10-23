const { exclaim } = require('./format');

function greet(name) {
  return exclaim(`Helo, ${name}`);
}

module.exports = { greet };
