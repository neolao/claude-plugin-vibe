// Called by the game board on every tick to render the remaining time.
function formatDuration(totalSeconds) {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return `${minutes}:${seconds}`;
}

module.exports = { formatDuration };
