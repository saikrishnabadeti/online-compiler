// #include <iostream>
// #include <string>

// int main() {
//     std::cout << "Enter your name: ";
//     std::string name;
//     std::getline(std::cin, name);

//     std::cout << "Hello, " << name << "!\n";
//     return 0;
// }







// #include <iostream>

// int main() {
//     int a = 10, b = 3;
//     std::cout << "a + b = " << a + b << '\n';
//     std::cout << "a - b = " << a - b << '\n';
//     std::cout << "a * b = " << a * b << '\n';
//     std::cout << "a / b = " << a / b << '\n';
//     std::cout << "a % b = " << a % b << '\n';
//     std::cout << "a++   = " << a++ << '\n';
//     std::cout << "++a   = " << ++a << '\n';
//     return 0;
// }

















// #include <iostream>

// int main() {
//     int x;
//     std::cout << "Enter a number (1-10): ";
//     std::cin >> x;

//     if (x < 1 || x > 10) {
//         std::cout << "Out of range!\n";
//     } else if (x % 2 == 0) {
//         std::cout << x << " is even.\n";
//     } else {
//         std::cout << x << " is odd.\n";
//     }

//     std::cout << "Counting down: ";
//     for (int i = x; i >= 1; --i) {
//         std::cout << i << (i > 1 ? ", " : "\n");
//     }
//     return 0;
// }













// #include <iostream>

// int add(int a, int b) { return a + b; }
// double add(double a, double b) { return a + b; }

// template<class T>
// T max(T a, T b) { return (a > b) ? a : b; }

// int main() {
//     std::cout << add(2, 3) << '\n';
//     std::cout << add(2.5, 3.7) << '\n';
//     std::cout << max(10, 20) << '\n';
//     std::cout << max('A', 'Z') << '\n';
//     return 0;
// }









// #include <iostream>

// void swap(int& x, int& y) {
//     int tmp = x; x = y; y = tmp;
// }

// int main() {
//     int a = 100, b = 200;
//     int* p = &a;

//     std::cout << "a = " << a << ", b = " << b << ", *p = " << *p << '\n';
//     swap(a, b);
//     std::cout << "After swap: a = " << a << ", b = " << b << '\n';
//     return 0;
// }


















// #include <iostream>
// #include <string>

// class Person {
//     std::string name;
//     int age;
// public:
//     Person(std::string n, int a) : name(n), age(a) {}
//     void introduce() const {
//         std::cout << "Hi, I'm " << name << " and I'm " << age << " years old.\n";
//     }
//     void birthday() { ++age; }
//     int getAge() const { return age; }
// };

// int main() {
//     Person p("Bob", 25);
//     p.introduce();
//     p.birthday();
//     std::cout << "Next year age: " << p.getAge() << '\n';
//     return 0;
// }




















// #include <iostream>

// class Animal {
// public:
//     virtual void speak() const { std::cout << "???\n"; }
//     virtual ~Animal() = default;
// };

// class Dog : public Animal {
// public:
//     void speak() const override { std::cout << "Woof!\n"; }
// };

// class Cat : public Animal {
// public:
//     void speak() const override { std::cout << "Meow!\n"; }
// };

// void makeSpeak(const Animal& a) { a.speak(); }

// int main() {
//     Dog d; Cat c;
//     makeSpeak(d);
//     makeSpeak(c);
//     return 0;
// }
















// #include <iostream>
// #include <vector>
// #include <map>
// #include <algorithm>

// int main() {
//     std::vector<int> v = {5, 2, 9, 1, 5};
//     std::sort(v.begin(), v.end());

//     std::cout << "Sorted vector: ";
//     for (int x : v) std::cout << x << ' ';
//     std::cout << '\n';

//     std::map<std::string, int> scores;
//     scores["Alice"] = 95;
//     scores["Bob"]   = 87;

//     std::cout << "Bob's score: " << scores["Bob"] << '\n';
//     return 0;
// }











// #include <iostream>
// #include <stdexcept>

// double divide(double a, double b) {
//     if (b == 0) throw std::runtime_error("division by zero");
//     return a / b;
// }

// int main() {
//     try {
//         std::cout << divide(10, 0) << '\n';
//     } catch (const std::exception& e) {
//         std::cout << "Caught: " << e.what() << '\n';
//     }
//     return 0;
// }
















// #include <iostream>
// #include <vector>

// std::vector<int> createBig() {
//     std::vector<int> v;
//     for (int i = 0; i < 1'000'000; ++i) v.push_back(i);
//     return v;               // should be moved, not copied
// }

// int main() {
//     auto v = createBig();   // NRVO / move
//     std::cout << "Size = " << v.size() << '\n';
//     return 0;
// }
















// #include <iostream>
// int main() {
//     std::cout << "Hello"   // <-- missing ;
//     return 0;
// }













// #include <iostream>
// int main() {
//     std::cout << "Unterminated string;
//     return 0;
// }










// int main() {
//     int @x = 5;   // @ is not a valid token
//     return 0;
// }






// int main() {
//     x = 10;       // x never declared
//     return 0;
// }
















// int main() {
//     int a = "string literal";   // cannot initialise int with const char*
//     return 0;
// }











// extern void bar();
// int main() { bar(); return 0; }








// int global = 42;     // definition with external linkage














// #include <iostream>
// int main() {
//     int* p = nullptr;
//     *p = 42;                     // <-- segfault
//     std::cout << "Never reached\n";
//     return 0;
// }











// #include <iostream>
// int main() {
//     int a[5] = {0,1,2,3,4};
//     std::cout << a[10] << '\n';   // out-of-bounds read → UB
//     a[10] = 99;                   // out-of-bounds write → UB
//     return 0;
// }









// #include <cassert>
// #include <iostream>
// int main() {
//     int x;
//     std::cout << "Enter a positive number: ";
//     std::cin >> x;
//     assert(x > 0 && "Input must be positive!");
//     std::cout << "You entered " << x << '\n';
//     return 0;
// }







// #include <iostream>
// int main() {
//     int a = 10, b = 0;
//     std::cout << a / b << '\n';   // integer division by zero
//     return 0;
// }















    // #include <iostream>

    // int main() {
    //     std::cout << "Infinite loop starting..." << std::endl;
    //     while (true) { // or while(1)
    //         // break
    //     }
    //     return 0; // This line will never be reached
    // }









