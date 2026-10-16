// Called by the monthly billing job; amounts in cents.
export function invoiceTotal(lines) {
  if (lines.length === 0) throw new Error("empty invoice");
  return lines.reduce((sum, { unitCents, qty }) => sum + unitCents * qty, 0);
}

// Resolves the address the invoice is sent to, from the customer directory.
export async function billingAddress(directory, customerId) {
  const customer = await directory.find(customerId);
  if (!customer) throw new Error(`unknown customer ${customerId}`);
  return customer.address;
}
