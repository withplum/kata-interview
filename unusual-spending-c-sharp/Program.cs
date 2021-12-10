using System;

namespace unusual_spending_c_sharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Email.send("", "", "");
            Payments.fetch("", 1, 2021);
        }
    }
}
