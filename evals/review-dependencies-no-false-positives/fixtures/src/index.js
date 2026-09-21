const express = require("express");
const lodash = require("lodash");
const { format } = require("date-fns");

const app = express();

app.get("/", (req, res) => {
  res.send(`${lodash.escape("hello")} @ ${format(new Date(), "yyyy-MM-dd")}`);
});

app.listen(3000);
