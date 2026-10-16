function exportPdf(report) {
  return Buffer.from(`%PDF-1.4\n${report.title}\n${report.body}`);
}

module.exports = { exportPdf };
