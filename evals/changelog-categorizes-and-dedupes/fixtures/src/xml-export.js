function exportXml(rows) {
  return `<rows>${rows.map((r) => `<row>${JSON.stringify(r)}</row>`).join("")}</rows>`;
}

module.exports = { exportXml };
