export interface CartLine {
  sku: string;
  quantity: number;
  unitPrice: number;
}

export function cartTotal(lines: CartLine[]): number {
  return lines.reduce((sum, line) => sum + line.quantity * line.unitPrice, 0);
}
