# 0x12. JavaScript - Warm up

![JavaScript](https://img.shields.io/badge/Language-JavaScript-yellow.svg)
![Author](https://img.shields.io/badge/Author-Guillaume-blue.svg)
![Weight](https://img.shields.io/badge/Weight-1-lightgrey.svg)
![Project Duration](https://img.shields.io/badge/Project%20Duration-Sep%2011,%202023%204%3A00%20AM%20to%20Sep%2012,%202023%204%3A00%20AM-green.svg)
![Auto Review](https://img.shields.io/badge/Auto%20Review-Scheduled-red.svg)

## Background Context

JavaScript is a versatile programming language used for scripting and web front-end development. In this project, we will focus on learning the basics of JavaScript to prepare for more advanced tasks, such as making our AirBnB project dynamic using JavaScript and JQuery.

## Resources

Before you begin, it's recommended to review the following resources:

- [Writing JavaScript Code](https://intranet.alxswe.com/rltoken/3HLjEesLsmyWfRUWnxgUGg)
- [Variables](https://intranet.alxswe.com/rltoken/zgOWmcpVLZFEmFlmuwayyg)
- [Data Types](https://intranet.alxswe.com/rltoken/VPd6JWaLrwOBzjAeXNAEqg)
- [Operators](https://intranet.alxswe.com/rltoken/3HLjEesLsmyWfRUWnxgUGg)
- [Operator Precedence](https://intranet.alxswe.com/rltoken/PHtcJJk30gBNmlFQ9R4RVg)
- [Controlling Program Flow](https://intranet.alxswe.com/rltoken/tsreKcNh_KmTmLPHsfvJRw)
- [Functions](https://intranet.alxswe.com/rltoken/e3EfHIxICdIncGBwwIDbXQ)
- [Objects and Arrays](https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g)
- [Intrinsic Objects](https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g)
- [Module Patterns](https://intranet.alxswe.com/rltoken/g-MgvO09Ur02RhM63gVyXw)
- [var, let and const](https://intranet.alxswe.com/rltoken/gJi61GeJTRX0g-M0Rx-0Iw)
- [JavaScript Tutorial](https://intranet.alxswe.com/rltoken/Y8hkOcy5jO22lQGyF6_NiA)
- [Modern JS](https://intranet.alxswe.com/rltoken/NZawtiBjWUpiojnrtVywNw)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without Google's help:

### General
- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- Differences between var, const, and let
- All available data types in JavaScript
- How to use if and if...else statements
- How to use comments
- How to assign values to variables
- How to use while and for loops
- How to use break and continue statements
- What is a function and how to use functions
- What a function that doesn't use a return statement returns
- Scope of variables
- Arithmetic operators and how to use them
- How to manipulate dictionaries
- How to import a file

### Copyright - Plagiarism

Please note that you are required to come up with solutions for the tasks on your own to meet the learning objectives. Plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the project folder is mandatory
- Your code should be semistandard compliant (version 16.x.x) with semicolons
- All your files must be executable
- The length of your files will be tested using `wc`

### More Info

To get started, you'll need to install Node.js 14 and the semistandard library:

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
$ sudo npm install semistandard --global
```

### 1. 3 languages (1-multi_languages.js)
- Write a script that prints 3 lines:

  - The first line: “C is fun”
  - The second line: “Python is cool”
  - The third line: “JavaScript is amazing”
  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`

```bash
$ ./1-multi_languages.js
C is fun
Python is cool
JavaScript is amazing
```

### 2. Arguments (2-arguments.js)
- Write a script that prints a message depending on the number of arguments passed:

  - If no arguments are passed to the script, print “No argument”
  - If only one argument is passed to the script, print “Argument found”
  - Otherwise, print “Arguments found”
  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`

```bash
$ ./2-arguments.js
No argument
$ ./2-arguments.js Best
Argument found
$ ./2-arguments.js Best School
Arguments found
```

### 3. Value of my argument (3-value_argument.js)
- Write a script that prints the first argument passed to it:

  - If no arguments are passed to the script, print “No argument”
  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`
  - You are not allowed to use `length`

```bash
$ ./3-value_argument.js
No argument
$ ./3-value_argument.js School
School
```

### 4. Create a sentence (4-concat.js)
- Write a script that prints two arguments passed to it in the following format: “ is ”

  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`

```bash
$ ./4-concat.js c cool
c is cool
$ ./4-concat.js c
c is undefined
$ ./4-concat.js
undefined is undefined
```

### 5. An Integer (5-to_integer.js)
- Write a script that prints "My number: <first argument converted to an integer>" if the first argument can be converted to an integer:

  - If the argument can't be converted to an integer, print "Not a number"
  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`
  - You are not allowed to use try/catch

```bash
$ ./5-to_integer.js
Not a number
$ ./5-to_integer.js 89
My number: 89
$ ./5-to_integer.js "89"
My number: 89
$ ./5-to_integer.js 89.89
My number: 89
$ ./5-to_integer.js School
Not a number
```

### 6. Loop to languages (6-multi_languages_loop.js)
- Write a script that prints 3 lines (similar to 1-multi_languages.js) but by using an array of strings and a loop:

  - The first line: “C is fun”
  - The second line: “

Python is cool”
  - The third line: “JavaScript is amazing”
  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`
  - You are not allowed to use any if/else statement
  - You can use only one `console.log`
  - You must use a loop (while, for, etc.)

```bash
$ ./6-multi_languages_loop.js
C is fun
Python is cool
JavaScript is amazing
```

### 7. I love C (7-multi_c.js)
- Write a script that prints "C is fun" x times, where x is the first argument of the script:

  - If the first argument can't be converted to an integer, print "Missing number of occurrences"
  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`
  - You can use only two `console.log`
  - You must use a loop (while, for, etc.)

```bash
$ ./7-multi_c.js 2
C is fun
C is fun
$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
$ ./7-multi_c.js
Missing number of occurrences
$ ./7-multi_c.js -3
```

### 8. Square (8-square.js)
- Write a script that prints a square:

  - The first argument is the size of the square
  - If the first argument can't be converted to an integer, print "Missing size"
  - You must use the character "X" to print the square
  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`
  - You must use a loop (while, for, etc.)

```bash
$ ./8-square.js
Missing size
$ ./8-square.js School
Missing size
$ ./8-square.js 2
XX
XX
$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$ ./8-square.js -3
```

### 9. Add (9-add.js)
- Write a script that prints the addition of 2 integers:

  - The first argument is the first integer
  - The second argument is the second integer
  - You have to define a function with this prototype: `function add(a, b)`
  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`

```bash
$ ./9-add.js
NaN
$ ./9-add.js 1
NaN
$ ./9-add.js 1 7
8
$ ./9-add.js 13 89
102
```

### 10. Factorial (10-factorial.js)
- Write a script that computes and prints a factorial:

  - The first argument is an integer used for computing the factorial
  - The factorial of NaN is 1
  - You must do it recursively
  - You must use a function
  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`

```bash
$ ./10-factorial.js
1
$ ./10-factorial.js 3
6
$ ./10-factorial.js 89
1.6507955160908452e+136
$ ./10-factorial.js 333
Infinity
```

### 11. Second biggest! (11-second_biggest.js)
- Write a script that searches the second biggest integer in the list of arguments:

  - You can assume all arguments can be converted to integers
  - If no argument is passed, print 0
  - If the number of arguments is 1, print 0
  - You must use `console.log(...)` to print all output
  - You are not allowed to use `var`

```bash
$ ./11-second_biggest.js
0
$ ./11-second_biggest.js 1
0
$ ./11-second_biggest.js 4 2 5 3 0 -3
4
```

### 12. Object (12-object.js)
- Update this script to replace the value 12 with 89:

```bash
$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
```

### 13. Add file (13-add.js)
- Write a function that returns the addition of 2 integers:

  - The function must be visible from outside
  - The name of the function must be `add`

```bash
$ ./13-main.js
8
```

## License
This project is protected by the ALX license. All rights reserved.
