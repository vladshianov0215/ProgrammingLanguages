using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            CreateThread(new Token(" << SomeData >>", 20), 0);
            Console.Read();
        }

        static void CreateThread(Token token, int index)
        {
            Console.WriteLine(string.Format("Now work thread nuber "+ index.ToString()));
            if (index < token.Recipient)
            {
                Console.WriteLine(string.Format("Start next thread " + (index+1).ToString()));
                Thread tmpThr = new Thread(() => CreateThread(token, index + 1));
                tmpThr.Start();
            }
            else
            {
                Console.WriteLine(string.Format("It`s last thread num "+ index.ToString() + " and data is "+ token.Data));
            }
            Console.WriteLine(string.Format("Thread nember " + index.ToString()+ " is ended \r\n"));
    
        }
    }


    public class Token
    {
        private string _data;
        private int _recipient;//получатель

        public string Data { get { return _data; } }
        public int Recipient { get { return _recipient; } }

        public Token(string data, int recipient)
        {
            _data = data;
            _recipient = recipient;
        }
    }

}




