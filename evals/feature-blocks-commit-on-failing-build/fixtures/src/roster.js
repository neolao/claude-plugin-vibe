function totalScore(players) {
  return players.reduce((sum, p) => sum + p.score, 0);
}

module.exports = { totalScore };
