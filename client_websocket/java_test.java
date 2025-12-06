// // Test01.java
// import java.util.Scanner;

// public class Test01 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter name: ");
//         String name = sc.nextLine();
//         System.out.print("Enter age: ");
//         int age = Integer.parseInt(sc.nextLine());
//         System.out.printf("Hello %s, you are %d years old.%n", name, age);
//     }
// }












// // Test02.java
// import java.util.Scanner;

// public class Test02 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Score (0-100): ");
//         int score = sc.nextInt();
//         String grade = score >= 90 ? "A" :
//                        score >= 80 ? "B" :
//                        score >= 70 ? "C" : "F";
//         System.out.println("Grade: " + grade);
//     }
// }








// // Test03.java
// import java.util.Scanner;

// public class Test03 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Count to: ");
//         int n = sc.nextInt();
//         for (int i = 1; i <= n; i++) {
//             System.out.print(i + " ");
//         }
//         System.out.println();
//     }
// }










// // Test04.java
// import java.util.Scanner;

// public class Test04 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int total = 0;
//         while (true) {
//             System.out.print("Number (q to quit): ");
//             String s = sc.next();
//             if (s.equals("q")) break;
//             try {
//                 int num = Integer.parseInt(s);
//                 total += num;
//             } catch (NumberFormatException e) {
//                 System.out.println("Invalid, ignored.");
//                 continue;
//             }
//         }
//         System.out.println("Sum = " + total);
//     }
// }











// // Test05.java
// import java.util.Scanner;
// import java.util.Arrays;

// public class Test05 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Numbers (space-separated): ");
//         String[] parts = sc.nextLine().split("\\s+");
//         int[] nums = new int[parts.length];
//         for (int i = 0; i < parts.length; i++) {
//             nums[i] = Integer.parseInt(parts[i]);
//         }
//         System.out.println("Original: " + Arrays.toString(nums));
//         int[] squares = new int[nums.length];
//         for (int i = 0; i < nums.length; i++) {
//             squares[i] = nums[i] * nums[i];
//         }
//         System.out.println("Squares: " + Arrays.toString(squares));
//     }
// }













// // Test06.java
// import java.util.ArrayList;
// import java.util.Scanner;

// public class Test06 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         ArrayList<String> list = new ArrayList<>();
//         System.out.println("Enter words (empty to stop):");
//         while (true) {
//             String word = sc.nextLine();
//             if (word.isEmpty()) break;
//             list.add(word);
//         }
//         System.out.println("You entered: " + list);
//     }
// }















// // Test07.java
// import java.util.Scanner;

// public class Test07 {
//     static String greet(String name, String greeting) {
//         return greeting + ", " + name + "!";
//     }

//     static double stats(String op, double... nums) {
//         if (nums.length == 0) return 0;
//         double sum = 0;
//         for (double n : nums) sum += n;
//         return op.equals("avg") ? sum / nums.length : sum;
//     }

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Name: ");
//         String name = sc.nextLine();
//         System.out.println(greet(name, "Hi"));
//         System.out.println(stats("avg", 1, 2, 3, 4));
//     }
// }







// // Test08.java
// import java.util.Scanner;

// public class Test08 {
//     static long factorial(int n) {
//         return n <= 1 ? 1 : n * factorial(n - 1);
//     }

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("n! = ");
//         int n = sc.nextInt();
//         System.out.println(n + "! = " + factorial(n));
//     }
// }














// // Test09.java
// import java.util.Scanner;

// public class Test09 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         try {
//             System.out.print("a: ");
//             int a = Integer.parseInt(sc.nextLine());
//             System.out.print("b: ");
//             int b = Integer.parseInt(sc.nextLine());
//             System.out.println(a / b);
//         } catch (ArithmeticException e) {
//             System.out.println("Division by zero!");
//         } catch (NumberFormatException e) {
//             System.out.println("Invalid number!");
//         } finally {
//             System.out.println("Done.");
//         }
//     }
// }







// // Test10.java
// import java.util.Scanner;

// abstract class Animal {
//     String name;
//     Animal(String name) { this.name = name; }
//     abstract String speak();
// }

// class Dog extends Animal {
//     Dog(String name) { super(name); }
//     String speak() { return "Woof!"; }
// }

// public class Test10 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Dog name: ");
//         Dog d = new Dog(sc.nextLine());
//         System.out.println(d.name + " says " + d.speak());
//     }
// }











// // Test11.java
// import java.util.Scanner;

// interface Speakable {
//     String speak();
//     default String shout() { return speak().toUpperCase() + "!"; }
// }

// class Cat implements Speakable {
//     public String speak() { return "Meow"; }
// }

// public class Test11 {
//     public static void main(String[] args) {
//         Speakable c = new Cat();
//         System.out.println(c.speak() + " -> " + c.shout());
//     }
// }







// // Test12.java
// import java.util.Scanner;
// import java.io.*;

// public class Test12 {
//     public static void main(String[] args) throws IOException {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("File: ");
//         String file = sc.nextLine();
//         System.out.print("Text: ");
//         String text = sc.nextLine();
//         try (PrintWriter pw = new PrintWriter(file)) {
//             pw.println(text);
//         }
//         System.out.println("Read: " + new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get(file))).trim());
//     }
// }









// // Test13.java
// import java.util.*;
// import java.util.stream.*;

// public class Test13 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Numbers: ");
//         List<Integer> nums = Arrays.stream(sc.nextLine().split("\\s+"))
//                                    .map(Integer::parseInt)
//                                    .collect(Collectors.toList());
//         List<Integer> evensSquared = nums.stream()
//                                          .filter(n -> n % 2 == 0)
//                                          .map(n -> n * n)
//                                          .collect(Collectors.toList());
//         System.out.println("Evens squared: " + evensSquared);
//     }
// }



// // Test14.java
// import java.util.*;

// class Box<T extends Number> {
//     T value;
//     Box(T v) { value = v; }
//     double doubleValue() { return value.doubleValue(); }
// }

// public class Test14 {
//     public static void main(String[] args) {
//         Box<Integer> b = new Box<>(42);
//         System.out.println("Double: " + b.doubleValue());
//     }
// }











// // Test15.java
// enum Day { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY }

// public class Test15 {
//     public static void main(String[] args) {
//         for (Day d : Day.values()) {
//             System.out.println(d + " is weekend? " + (d == Day.SATURDAY || d == Day.SUNDAY));
//         }
//     }
// }









// // Test16.java
// import java.util.Scanner;
// import java.io.*;

// public class Test16 {
//     public static void main(String[] args) {
//         System.out.print("File to read: ");
//         String file = new Scanner(System.in).nextLine();
//         try (Scanner fileSc = new Scanner(new File(file))) {
//             while (fileSc.hasNextLine()) {
//                 System.out.println(">> " + fileSc.nextLine());
//             }
//         } catch (FileNotFoundException e) {
//             System.out.println("File not found!");
//         }
//     }
// }













// // Test17.java
// import java.lang.annotation.*;
// import java.lang.reflect.*;

// @Retention(RetentionPolicy.RUNTIME)
// @interface Test { String value(); }

// public class Test17 {
//     @Test("Hello")
//     public static void run() {}

//     public static void main(String[] args) throws Exception {
//         Method m = Test17.class.getMethod("run");
//         Test ann = m.getAnnotation(Test.class);
//         System.out.println("Annotation: " + ann.value());
//     }
// }


















// // Test18.java
// import java.util.Scanner;

// public class Test18 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Command (quit/greet): ");
//         String cmd = sc.next();
//         String result = switch (cmd) {
//             case "quit" -> "Bye!";
//             case "greet" -> {
//                 System.out.print("Name: ");
//                 String name = sc.next();
//                 yield "Hi " + name + "!";
//             }
//             default -> "Unknown";
//         };
//         System.out.println(result);
//     }
// }













// // Test19.java
// record Point(int x, int y) {}

// public class Test19 {
//     public static void main(String[] args) {
//         Point p = new Point(3, 4);
//         System.out.println(p);
//         System.out.println("Distance: " + Math.hypot(p.x(), p.y()));
//     }
// }











// // Test20.java
// sealed interface Shape permits Circle, Rectangle {}
// record Circle(double r) implements Shape {}
// record Rectangle(double w, double h) implements Shape {}

// public class Test20 {
//     static double area(Shape s) {
//         return switch (s) {
//             case Circle c -> Math.PI * c.r() * c.r();
//             case Rectangle r -> r.w() * r.h();
//         };
//     }
//     public static void main(String[] args) {
//         System.out.println(area(new Circle(5))); // ~78.5
//     }
// }
























// // Test21.java
// public class Test21 {
//     static String describe(Object o) {
//         return o instanceof String s && s.length() > 5 ? "Long string" :
//                o instanceof Integer i ? "Number: " + i : "Other";
//     }
//     public static void main(String[] args) {
//         System.out.println(describe("HelloWorld"));
//     }
// }












// // Test22.java
// public class Test22 {
//     public static void main(String[] args) throws InterruptedException {
//         Thread t = new Thread(() -> {
//             for (int i = 1; i <= 3; i++) {
//                 System.out.println("Thread: " + i);
//                 try { Thread.sleep(100); } catch (Exception e) {}
//             }
//         });
//         t.start();
//         t.join();
//         System.out.println("Main done");
//     }
// }







// // Test23.java
// public class Test23 {
//     static int counter = 0;
//     public static synchronized void inc() { counter++; }
//     public static void main(String[] args) throws InterruptedException {
//         Thread[] threads = new Thread[100];
//         for (int i = 0; i < 100; i++) {
//             threads[i] = new Thread(Test23::inc);
//             threads[i].start();
//         }
//         for (Thread t : threads) t.join();
//         System.out.println("Counter: " + counter); // Should be 100
//     }
// }


















// // Test24.java
// import java.util.Optional;

// public class Test24 {
//     public static void main(String[] args) {
//         Optional<String> opt = Optional.of("Java");
//         opt.map(String::toUpperCase)
//            .ifPresentOrElse(
//                s -> System.out.println("Found: " + s),
//                () -> System.out.println("Empty")
//            );
//     }
// }







// // ErrorTest.java
// public class ErrorTest {
//     public static void main(String[] args) {
//         try { System.out.println("1. " + (10 / 0)); }
//         catch (ArithmeticException e) { System.out.println("ERROR #1: ArithmeticException"); }

//         try { String s = null; s.length(); }
//         catch (NullPointerException e) { System.out.println("ERROR #2: NullPointerException"); }

//         try { int[] a = new int[5]; System.out.println(a[10]); }
//         catch (ArrayIndexOutOfBoundsException e) { System.out.println("ERROR #3: ArrayIndexOutOfBoundsException"); }

//         try { Integer.parseInt("abc"); }
//         catch (NumberFormatException e) { System.out.println("ERROR #4: NumberFormatException"); }

//         try { throw new IllegalArgumentException("Bad"); }
//         catch (IllegalArgumentException e) { System.out.println("ERROR #5: IllegalArgumentException"); }

//         try { Class.forName("NonExistent"); }
//         catch (ClassNotFoundException e) { System.out.println("ERROR #6: ClassNotFoundException"); }

//         System.out.println("All errors caught!");
//     }
// }







// public class SyntaxError {
//     // int x = ;           // Missing expression
//         // y = 1;          // Unexpected indent (not in Java, but test lexer)
//     // if (true) {         // Missing }
//     // System.out.println("Hi")
// }















// public class InfiniteLoopExample {
//     public static void main(String[] args) {
//         // This loop will run forever
//         System.out.println("Infinite loop starting...");
//         while (true) {
//             // System.out.println("This is an infinite loop!");
//             // You typically need a 'break' statement within the loop
//             // to eventually exit it under certain conditions.
//         }
//     }
// }


