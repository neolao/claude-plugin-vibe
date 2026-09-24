function search(query, records) {
  return records.filter((r) => r.includes(query));
}

module.exports = { search };
