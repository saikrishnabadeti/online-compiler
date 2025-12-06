<?php

/*
// test_01.php
echo "Enter your name: ";
$name = trim(fgets(STDIN));
echo "Enter your age: ";
$age = (int) trim(fgets(STDIN));
printf("Hello %s, you are %d years old.\n", $name, $age);
*/





/*
// test_02.php
echo "Score (0-100): ";
$score = (int) trim(fgets(STDIN));
if ($score >= 90) {
    $grade = 'A';
} elseif ($score >= 80) {
    $grade = 'B';
} elseif ($score >= 70) {
    $grade = 'C';
} else {
    $grade = 'F';
}
echo "Grade: $grade\n";
*/





/*
// test_03.php
echo "Count to: ";
$n = (int) trim(fgets(STDIN));
for ($i = 1; $i <= $n; $i++) {
    echo "$i ";
}
echo "\n";
*/






/*
// test_04.php
$total = 0;
while (true) {
    echo "Number (or 'q' to quit): ";
    $s = trim(fgets(STDIN));
    if ($s === 'q') {
        break;
    }
    if (!ctype_digit($s)) {
        echo "Not a digit, ignored.\n";
        continue;
    }
    $total += (int) $s;
}
echo "Sum = $total\n";
*/





/*
// test_05.php
echo "Space-separated numbers: ";
$input = trim(fgets(STDIN));
$nums = array_map('intval', explode(' ', $input));
echo "Original: ";
print_r($nums);
echo "Squares: ";
print_r(array_map(fn($x) => $x * $x, $nums));
*/








/*
// test_06.php
echo "Word: ";
$word = trim(fgets(STDIN));
$counts = [];
foreach (str_split($word) as $ch) {
    $counts[$ch] = ($counts[$ch] ?? 0) + 1;
}
echo "Letter counts: ";
print_r($counts);
*/




/*
// test_07.php
function greet($name, $greeting = "Hi") {
    return "$greeting, $name!";
}

function stats(...$numbers) {
    $op = array_pop($numbers) ?? 'sum'; // Simulate op as last arg for simplicity
    $nums = $numbers;
    return match($op) {
        'sum' => array_sum($nums),
        'avg' => !empty($nums) ? array_sum($nums) / count($nums) : 0,
        default => 0
    };
}

echo "Name: ";
echo greet(trim(fgets(STDIN)));
echo "\n";
echo stats(1, 2, 3, 4, 'avg'), "\n";
*/

/*
// test_08.php
function fact($n) {
    return $n <= 1 ? 1 : $n * fact($n - 1);
}

echo "n! = ";
$n = (int) trim(fgets(STDIN));
echo "$n! = ", fact($n), "\n";
*/





/*
// test_09.php
try {
    echo "a: ";
    $a = (int) trim(fgets(STDIN));
    echo "b: ";
    $b = (int) trim(fgets(STDIN));
    if ($b == 0) {
        throw new DivisionByZeroError("Division by zero!");
    }
    echo $a / $b, "\n";
} catch (DivisionByZeroError $e) {
    echo "Division by zero!\n";
} catch (ValueError $e) {
    echo "Invalid integer!\n";
}
*/









/*
// test_10.php
class Animal {
    public function __construct(public string $name) {}
    public function speak() {
        return "???";
    }
}

class Dog extends Animal {
    public function speak() {
        return "Woof!";
    }
}

echo "Dog name: ";
$d = new Dog(trim(fgets(STDIN)));
echo $d->name, " says ", $d->speak(), "\n";
*/







 /*
// test_11.php
echo "File to create: ";
$filename = trim(fgets(STDIN));
echo "Text line: ";
$text = trim(fgets(STDIN));
file_put_contents($filename, $text . "\n");
$read = file_get_contents($filename);
echo "Read back: ", trim($read), "\n";
*/









/*
// test_12.php (run directly)
function secret() {
    return "Shhh!";
}

if (basename(__FILE__) === basename($_SERVER['SCRIPT_FILENAME'])) {
    echo "Running directly: ", secret(), "\n";
} else {
    echo "Included as module\n";
}
*/









/*
// test_13.php
function fib_upto($n) {
    $a = 0;
    $b = 1;
    while ($a <= $n) {
        yield $a;
        [$a, $b] = [$b, $a + $b];
    }
}

echo "Fib limit: ";
$limit = (int) trim(fgets(STDIN));
print_r(iterator_to_array(fib_upto($limit)));
*/









/*
// test_14.php
echo "Command (quit/greet/count): ";
$cmd = trim(fgets(STDIN));
$parts = explode(' ', $cmd);
$match = match (true) {
    $parts[0] === 'quit' => 'Good-bye',
    $parts[0] === 'greet' && isset($parts[1]) => "Hi {$parts[1]}!",
    $parts[0] === 'count' => 'Count: ' . (count($parts) - 1),
    default => 'Unknown'
};
echo $match, "\n";
*/










/*
// test_15.php
echo "Numbers: ";
$input = trim(fgets(STDIN));
$nums = array_map('intval', explode(' ', $input));
$evens = array_filter($nums, fn($x) => $x % 2 === 0);
$squares = array_map(fn($x) => $x * $x, $evens);
echo "Evens squared: ";
print_r($squares);
*/







/*
// test_16.php
#[\Attribute]
class TestAttr {}

#[TestAttr]
class Point {
    public function __construct(
        public readonly int $x,
        public readonly int $y
    ) {}
}

echo "x y: ";
[$x, $y] = array_map('intval', explode(' ', trim(fgets(STDIN))));
$p = new Point($x, $y);
echo $p->x, ', ', $p->y, "\n";
*/









/*
// test_17.php
set_error_handler(function($errno, $errstr) {
    echo "Custom Error: $errstr\n";
});

echo "Number: ";
$x = trim(fgets(STDIN));
if (!is_numeric($x)) {
    trigger_error("Bad input", E_USER_ERROR);
} else {
    echo "Squared: ", ($x * $x), "\n";
}
*/










/*
// test_18.php (simulate $_POST via args: php test_18.php key=value)
parse_str($argv[1] ?? '', $_GET); // Simulate GET
if (isset($_GET['line'])) {
    echo "You typed: {$_GET['line']}\n";
} else {
    echo "No input\n";
}
*/










/*
// errors.php
$errors = [];

// 1. ParseError (syntax) - Test separately in parser
// echo "Missing ;";

try {
    // 2. Notice: Undefined variable
    echo $undefined;
} catch (Error $e) {
    $errors[] = "ERROR #2: Notice - Undefined variable (suppressed in strict mode)";
}

// 3. Warning: Division by zero
$warnings = [];
set_error_handler(function($errno, $errstr) use (&$warnings) {
    $warnings[] = $errstr;
});
echo 10 / 0; // Warning
restore_error_handler();
if (strpos($warnings[0] ?? '', 'Division by zero') !== false) {
    $errors[] = "ERROR #3: Warning - Division by zero";
}

// 4. TypeError: ArgumentCountError
try {
    substr('abc', 0, 1, 4); // Too many args
} catch (ArgumentCountError $e) {
    $errors[] = "ERROR #4: TypeError - Too many arguments";
}

// 5. Error: Undefined array key
try {
    $arr = ['a' => 1];
    echo $arr['b'];
} catch (Error $e) {
    $errors[] = "ERROR #5: Error - Undefined array key";
}

// 6. Error: Trying to access array offset on value of non-array
try {
    $str = 'abc';
    echo $str[5];
} catch (Error $e) {
    $errors[] = "ERROR #6: Error - Cannot access offset on string";
}

// 7. Error: Call to undefined function
try {
    undefined_func();
} catch (Error $e) {
    $errors[] = "ERROR #7: Fatal error - Call to undefined function";
}

// 8. ValueError: Invalid argument
try {
    random_int('a', 10);
} catch (ValueError $e) {
    $errors[] = "ERROR #8: ValueError - Invalid argument";
}

// 9. DivisionByZeroError
try {
    throw new DivisionByZeroError();
} catch (DivisionByZeroError $e) {
    $errors[] = "ERROR #9: DivisionByZeroError";
}

// 10. ParseError (in eval)
try {
    eval('if: pass;');
} catch (ParseError $e) {
    $errors[] = "ERROR #10: ParseError in eval";
}

// 11. OutOfMemoryError (simulate large alloc)
try {
    $large = str_repeat('x', 10**9); // May vary by limits
} catch (Error $e) {
    $errors[] = "ERROR #11: Out of memory (or similar)";
}

// 12. TypeError: Return value
function testRet(): int {
    return 'string';
}
try {
    testRet();
} catch (TypeError $e) {
    $errors[] = "ERROR #12: TypeError - Return value must be int";
}

// 13. Error: Cannot use object as array
class Obj {}
try {
    $o = new Obj();
    $o['key'] = 1;
} catch (Error $e) {
    $errors[] = "ERROR #13: Error - Cannot use object as array";
}

// 14. Warning: include non-existent file
@include 'nonexistent.php';
$warnings = [];
set_error_handler(function($errno, $errstr) use (&$warnings) {
    if (strpos($errstr, 'No such file') !== false) $warnings[] = $errstr;
});
restore_error_handler();
if (!empty($warnings)) {
    $errors[] = "ERROR #14: Warning - Failed to open stream";
}

// 15. Deprecated notice (PHP 8+)
if (PHP_VERSION_ID >= 80000) {
    $warnings = [];
    // Simulate deprecated (e.g., create_function)
    set_error_handler(function($errno, $errstr) use (&$warnings) {
        if (strpos($errstr, 'Deprecated') !== false) $warnings[] = $errstr;
    });
    // @create_function('', ''); // Uncomment if available
    restore_error_handler();
    if (!empty($warnings)) {
        $errors[] = "ERROR #15: Deprecated warning";
    }
}

// 16. AssertionError (PHP 7+)
try {
    assert(false, 'Custom assert');
} catch (AssertionError $e) {
    $errors[] = "ERROR #16: AssertionError - Custom assert";
}

// 17. Error: Recursion limit
function rec() { rec(); }
try {
    rec();
} catch (Error $e) { // Actual: Segmentation fault or stack overflow
    $errors[] = "ERROR #17: Fatal error - Recursion exceeded";
}

// 18. TypeError: Incompatible types
try {
    $a = 1;
    $a += 'abc';
} catch (TypeError $e) {
    $errors[] = "ERROR #18: TypeError - Unsupported operand";
}

// 19. Error: Undefined constant
try {
    echo UNDEFINED_CONST;
} catch (Error $e) {
    $errors[] = "ERROR #19: Error - Undefined constant";
}

// 20. Warning: Illegal string offset
try {
    $str = 'abc';
    $str['x'] = 'd';
} catch (Error $e) {
    $errors[] = "ERROR #20: Warning - Illegal string offset";
}

echo "\n=== PHP ERROR TEST RESULTS ===\n";
foreach ($errors as $err) {
    echo $err, "\n";
}
echo "Total errors triggered: ", count($errors), "\n";
if (count($errors) >= 15) {
    echo "Your compiler handles exceptions correctly!\n";
}
*/






/*
// Missing ;
echo "Hello"

// Unexpected indent
    $x = 1;

// Unclosed quote
echo 'Hello;
*/















// // This loop will run forever until the script is manually stopped
// echo "Infinite loop starting...";
// while (true) {
//     // A 'break' statement is typically needed to exit this loop conditionally
//     // if ($some_condition) { break; }
// }















?>