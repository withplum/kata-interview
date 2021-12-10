using System;
using System.Collections.Generic;

namespace unusual_spending_c_sharp
{
    class Payments
    {
        public static List<Payment> fetch(string userId, int year, int month)
        {
            throw new NotImplementedException();
        }
    }
    
    struct Payment
    {
        double amount;
        string category;
        string description;
    }
}