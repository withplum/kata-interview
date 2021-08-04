interface Payment {
  category: string;
  amount: number;
}

const payments = [
  {
    category: 'some category name',
    amount: 13.37
  }
]

// eslint-disable-next-line @typescript-eslint/no-unused-vars,@typescript-eslint/ban-ts-comment
// @ts-ignore
async function getPayments(userId: string): Promise<Payment[]> {
  return payments
}

export {Payment, getPayments};
