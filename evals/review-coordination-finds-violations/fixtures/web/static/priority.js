// Priority selector of the ticket form; the server validates the value again.
const PRIORITIES = ["low", "normal", "urgent"];

export function renderPrioritySelect(current) {
  const options = PRIORITIES.map(
    (p) => `<option value="${p}"${p === current ? " selected" : ""}>${p}</option>`
  );
  return `<select name="priority">${options.join("")}</select>`;
}
