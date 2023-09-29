---

# 0x10. Python - Network #0 - Project README

Welcome to the fascinating world of Python and web networking! This project is designed to teach us the fundamentals of working with URLs, HTTP, and using cURL to interact with web servers. Let's get started!

## Project Details

- **By:** Guillaume
- **Weight:** 1
- **Project Start:** Sep 28, 2023 4:00 AM
- **Project End:** Sep 29, 2023 4:00 AM
- **Checker Release:** Sep 28, 2023 10:00 AM
- **Auto Review:** Will be launched at the deadline

## Learning Objectives

By the end of this project, we should be able to explain to anyone (without Google's help):

### General

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for an HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

### Copyright - Plagiarism

We need to come up with solutions for the tasks ourselves. Copying and pasting someone else's work is strictly forbidden, and any form of plagiarism will result in removal from the program.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- A README.md file at the root of the folder of the project is mandatory
- All our Bash scripts will be tested on Ubuntu 20.04 LTS
- All Bash scripts should be exactly 3 lines long (`wc -l file` should print 3)
- All our files should end with a new line
- All our files must be executable
- The first line of all our Bash files should be exactly `#!/bin/bash`
- The second line of all our Bash scripts should be a comment explaining what the script is doing
- All `curl` commands must have the option `-s` (silent mode)
- All our Python files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all our Python files should be exactly `#!/usr/bin/python3`
- Our code should use pycodestyle (version 2.8.*)
- All our modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All our classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All our functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not just a word; it's a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)

## Tasks

### 0. cURL body size (mandatory)

We need to write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response. The size must be displayed in bytes, and we have to use `curl`. We should test our script using the web server running on port 5000 in the provided sandbox.

Example:

```shell
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
```

### 1. cURL to the end (mandatory)

This task requires us to write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response. We should display only the body of a 200 status code response, and we have to use `curl`. Once again, we should test our script using the web server running on port 5000 in the sandbox.

Example:

```shell
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
```

### 2. cURL Method (mandatory)

For this task, we need to write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response. We have to use `curl` and should test our script using the web server running on port 5000 in the provided sandbox.

Example:

```shell
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
```

### 3. cURL only methods (mandatory)

Our task here is to write a Bash script that takes in a URL and displays all HTTP methods the server will accept. We have to use `curl` and, once again, test our script using the web server running on port 5000 in the sandbox.

Example:

```shell
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
```

### 4. cURL headers (mandatory)

In this task, we should write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable `X-School-User-Id` must be sent with the value `98`, and we have to use `curl`. Testing is done using the web server running on port 5000.

Example:

```shell
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
```

### 5. cURL POST parameters (mandatory)

Here, we need to write a Bash script that takes in a URL, sends a POST request to the URL, and displays the body of the response. Two variables, `email` with the value `test@gmail.com` and `subject` with the value `I will always be here for PLD`, should be sent. We have to use `curl`, and testing is done using the web server running on port 5000.

Example:

```shell
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
```

### 6. Find a peak (mandatory)

This is a technical interview preparation task. We need to write a function that finds a peak in a list of unsorted

 integers. The prototype should be `def find_peak(list_of_integers):`. We are not allowed to import any modules, and our algorithm should have the lowest complexity (hint: we don't need to go through all numbers to find a peak). Our solution should be contained in `6-peak.py`, and `6-peak.txt` should contain the complexity of our algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n2)). Note that there may be more than one peak in the list.

Example:

```shell
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
```

---

Let's dive into these networking tasks and Python challenges! Happy coding!

---

*Copyright © 2023 ALX, All rights reserved.*
