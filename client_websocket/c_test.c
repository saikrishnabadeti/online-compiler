// #include <stdio.h>

// int main() {
//     int a, b;
//     printf("Enter two numbers: ");
//     scanf("%d %d", &a, &b);
//     printf("Sum = %d\n", a + b);
//     return 0;
// }














// #include <stdio.h>

// int main() {
//     int n, i;
//     printf("Enter size: ");
//     scanf("%d", &n);
//     int arr[100];
//     printf("Enter %d elements:\n", n);
//     for(i = 0; i < n; i++) {
//         scanf("%d", &arr[i]);
//     }
//     printf("Reversed: ");
//     for(i = n-1; i >= 0; i--) {
//         printf("%d ", arr[i]);
//     }
//     printf("\n");
//     return 0;
// }

















// #include <stdio.h>

// void swap(int *x, int *y) {
//     int temp = *x;
//     *x = *y;
//     *y = temp;
// }

// int main() {
//     int a = 10, b = 20;
//     printf("Before: a=%d, b=%d\n", a, b);
//     swap(&a, &b);
//     printf("After: a=%d, b=%d\n", a, b);
//     return 0;
// }


















// #include <stdio.h>

// unsigned long long factorial(int n) {
//     if (n == 0 || n == 1) return 1;
//     return n * factorial(n - 1);
// }

// int main() {
//     int n;
//     printf("Enter n: ");
//     scanf("%d", &n);
//     if (n < 0) printf("Invalid\n");
//     else printf("Factorial(%d) = %llu\n", n, factorial(n));
//     return 0;
// }








// #include <stdio.h>
// #include <string.h>

// struct Student {
//     int roll;
//     char name[50];
//     float marks;
// };

// int main() {
//     struct Student s[2];
//     for(int i = 0; i < 2; i++) {
//         printf("Student %d - Roll: ", i+1);
//         scanf("%d", &s[i].roll);
//         printf("Name: ");
//         scanf(" %49[^\n]", s[i].name);  // Read full line
//         printf("Marks: ");
//         scanf("%f", &s[i].marks);
//     }
//     printf("\n--- Records ---\n");
//     for(int i = 0; i < 2; i++) {
//         printf("Roll: %d, Name: %s, Marks: %.2f\n", s[i].roll, s[i].name, s[i].marks);
//     }
//     return 0;
// }


















// #include <stdio.h>

// int main() {
//     FILE *fp = fopen("data.txt", "w");
//     if (!fp) { printf("Cannot open file\n"); return 1; }
//     fprintf(fp, "Hello from C compiler test!\n");
//     fprintf(fp, "Line 2: %d + %d = %d\n", 10, 20, 30);
//     fclose(fp);

//     fp = fopen("data.txt", "r");
//     char line[100];
//     while (fgets(line, sizeof(line), fp)) {
//         printf("%s", line);
//     }
//     fclose(fp);
//     return 0;
// }















// #include <stdio.h>

// #define PI 3.14159
// #define AREA(r) (PI * (r) * (r))
// #define DEBUG 1

// int main() {
//     float r;
//     printf("Enter radius: ");
//     scanf("%f", &r);
//     printf("Area = %.2f\n", AREA(r));
    
//     #ifdef DEBUG
//         printf("DEBUG: Radius was %.2f\n", r);
//     #endif
//     return 0;
// }

















// #include <stdio.h>

// int main() {
//     unsigned int a, b;
//     printf("Enter two numbers: ");
//     scanf("%u %u", &a, &b);
//     printf("AND: %u\n", a & b);
//     printf("OR: %u\n", a | b);
//     printf("XOR: %u\n", a ^ b);
//     printf("Left shift a<<1: %u\n", a << 1);
//     printf("Right shift b>>1: %u\n", b >> 1);
//     return 0;
// }





// #include <stdio.h>

// int main() {
//     int x = 10
//     printf("x = %d\n", x);
//     return 0;
// }














// #include <stdio.h>

// int main() {
//     printf("Value: %d\n", y);  // y not declared
//     char c = "A";              // wrong: string literal to char
//     return 0;
// }



















// #include <stdio.h>
// #include <stdlib.h>

// int main() {
//     int *p = malloc(sizeof(int));
//     *p = 42;
//     free(p);
//     printf("Value: %d\n", *p);  // Undefined Behavior
//     return 0;
// }













// #include <stdio.h>

// int main() {
//     printf("Infinite loop starting...\n");
//     while(1) {
//         // no break
//         // printf("Infinite loop starting...\n");
//     }
//     return 0;
// }









