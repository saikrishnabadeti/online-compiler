

// // Valid program – should compile and run
// using System;

// class Program
// {
//     static void Main()
//     {
//         Console.WriteLine("Hello, World!");
//     }
// }











// using System;

// class Program
// {
//     static void Main()
//     {
//         Console.Write("Enter your name: ");
//         string name = Console.ReadLine();
//         Console.WriteLine($"Hello, {name}!");
//     }
// }




















// using System;

// class Program
// {
//     static void Main()
//     {
//         Console.WriteLine("test")   // <-- missing ;
//         Console.WriteLine("ok");
//     }
// }



















// using System;

// class Program
// {
//     static void Main()
//     {
//         if (true)
//         {
//             Console.WriteLine("ok");
//         // missing closing brace for Main
//     }
// }


















// using System;

// class Program
// {
//     static void Main()
//     {
//         x = 42;               // x not declared
//         Console.WriteLine(x);
//     }
// }

















// using System;

// class Program
// {
//     static int Main(string[] args)   // returns int but no return statement
//     {
//         Console.WriteLine("bad");
//     }
// }



















// using System;

// class Program
// {
//     static void Main()
//     {
//         int a = 10;
//         int b = 0;
//         int c = a / b;               // throws DivideByZeroException
//         Console.WriteLine(c);
//     }
// }




















// using System;

// class Program
// {
//     static void Main()
//     {
//         string s = null;
//         Console.WriteLine(s.Length); // throws NullReferenceException
//     }
// }




















// using System;

// class Program
// {
//     static void Main()
//     {
//         int[] arr = { 1, 2, 3 };
//         Console.WriteLine(arr[5]);   // index 5 does not exist
//     }
// }


















// using System;

// class Program
// {
//     static void Main()
//     {
//         int i = 42;
//         double d = i;               // implicit
//         int j = (int)d;             // explicit
//         Console.WriteLine($"{i} {d} {j}");
//     }
// }

















// using System;
// using System.Collections.Generic;

// class Program
// {
//     static void Main()
//     {
//         List<string> list = new List<string>();
//         list.Add("C#");
//         list.Add("rocks");
//         foreach (var s in list) Console.Write(s + " ");
//     }
// }















// using System;
// using System.Linq;

// class Program
// {
//     static void Main()
//     {
//         int[] numbers = { 1, 2, 3, 4, 5, 6 };
//         var evens = numbers.Where(n => n % 2 == 0).Select(n => n * 10);
//         Console.WriteLine(string.Join(", ", evens));
//     }
// }




















// using System;

// class Program
// {
//     static void Main()
//     {
//         try
//         {
//             int x = int.Parse("not a number");
//         }
//         catch (FormatException)
//         {
//             Console.WriteLine("Bad format!");
//         }
//         finally
//         {
//             Console.WriteLine("Done.");
//         }
//     }
// }



















// using System;
// using System.Threading.Tasks;

// class Program
// {
//     static async Task Main()
//     {
//         Console.WriteLine("Start");
//         await Task.Delay(100);   // simulate async work
//         Console.WriteLine("End");
//     }
// }


















// using System;

// class Person
// {
//     public string Name { get; set; } = "Anonymous";
//     public int Age { get; set; }
// }

// class Program
// {
//     static void Main()
//     {
//         var p = new Person { Name = "Bob", Age = 30 };
//         Console.WriteLine($"{p.Name} is {p.Age}");
//     }
// }















// using System;

// abstract class Shape
// {
//     public abstract double Area();
// }

// class Circle : Shape
// {
//     public double Radius { get; set; }
//     public override double Area() => Math.PI * Radius * Radius;
// }

// class Program
// {
//     static void Main()
//     {
//         Shape s = new Circle { Radius = 2 };
//         Console.WriteLine($"Area = {s.Area():F2}");
//     }
// }




















// using System;

// class Publisher
// {
//     public event Action<int> NumberChanged;

//     public void SetNumber(int n)
//     {
//         NumberChanged?.Invoke(n);
//     }
// }

// class Program
// {
//     static void Main()
//     {
//         var pub = new Publisher();
//         pub.NumberChanged += n => Console.WriteLine($"Got {n}");
//         pub.SetNumber(7);
//     }
// }











// using System;
// using System.Collections.Generic;

// class Program
// {
//     static void Main()
//     {
//         List<int> nums = new List<int> { 1, 2, 3, 4 };
//         nums.ForEach(x => Console.Write(x * x + " "));
//     }
// }


















// using System;

// class Program
// {
//     static void Main()
//     {
//         object o = "Hello";
//         if (o is string s)
//             Console.WriteLine(s.ToUpper());

//         // switch expression (C# 8+)
//         string result = o switch
//         {
//             string str when str.Length > 0 => "non-empty",
//             null => "null",
//             _ => "other"
//         };
//         Console.WriteLine(result);
//     }
// }









// #nullable enable
// using System;

// class Program
// {
//     static void Main()
//     {
//         string? maybe = null;
//         // Console.WriteLine(maybe.Length); // warning CS8602
//         Console.WriteLine(maybe ?? "default");
//     }
// }
















// using System;

// public record Point(int X, int Y);

// class Program
// {
//     static void Main()
//     {
//         var p1 = new Point(1, 2);
//         var p2 = new Point(1, 2);
//         Console.WriteLine(p1 == p2); // true (value equality)
//         Console.WriteLine(p1);
//     }
// }












// using System;

// [AttributeUsage(AttributeTargets.Class)]
// public class GenerateAttribute : Attribute { }

// [Generate]
// public class MyClass { }















// using System;

// class Program
// {
//     static void Main()
//     {
//         Console.WriteLine("Infinite loop starting...");
//         while (true)
//         {
//             // No break condition
//         }
//     }
// }









































