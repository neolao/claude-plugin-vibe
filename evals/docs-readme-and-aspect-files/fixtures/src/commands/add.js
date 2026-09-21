const { readWidgets, writeWidgets } = require("../storage/store");

function addWidget(name) {
  const widgets = readWidgets();
  widgets.push({ name });
  writeWidgets(widgets);
}

module.exports = { addWidget };
