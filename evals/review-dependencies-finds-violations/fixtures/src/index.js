const express = require("express");
const lodash = require("lodash");
const request = require("request");

const app = express();

app.get("/", (req, res) => {
  request.get("https://example.com/health", () => {
    res.send(lodash.escape("hello"));
  });
});

app.listen(3000);
