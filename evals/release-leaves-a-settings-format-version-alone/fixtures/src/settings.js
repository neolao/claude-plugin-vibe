const settings = require('../config/settings.json');

// Settings files written by older releases carry version 1 and no pageSize.
function loadSettings() {
  if (settings.version < 2) {
    return { ...settings, pageSize: 10 };
  }
  return settings;
}

module.exports = { loadSettings };
