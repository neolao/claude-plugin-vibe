function exportCsv(rows) {
  return rows.map((r) => Object.values(r).join(",")).join("\n");
}

module.exports = { exportCsv };
