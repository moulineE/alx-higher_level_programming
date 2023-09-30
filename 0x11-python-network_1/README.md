---

# 0x11. Python - Network #1 - Project README

Welcome to the exciting world of Python and network programming! This project will dive deeper into working with internet resources using the Python packages urllib and requests. By the end of this project, you'll be well-versed in fetching internet resources, handling HTTP requests, and decoding responses.

## Project Details

- **By:** Guillaume, CTO at Holberton School
- **Weight:** 1
- **Project Start:** Sep 29, 2023 4:00 AM
- **Project End:** Sep 30, 2023 4:00 AM
- **Checker Release:** Sep 29, 2023 10:00 AM
- **Auto Review:** Will be launched at the deadline

## Learning Objectives

By the end of this project, you should be able to explain the following concepts to anyone, without the help of Google:

### General

- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests (remember, it's simpler than urllib!)
- How to make an HTTP GET request
- How to make HTTP POST/PUT/etc. requests
- How to fetch JSON resources
- How to manipulate data from an external service

## Copyright - Plagiarism

Remember, you're tasked with coming up with solutions for the tasks yourself. Copying and pasting someone else's work is strictly forbidden, and any form of plagiarism will result in removal from the program.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- You must use `get` to access dictionary values by key (it won't throw an exception if the key doesn't exist in the dictionary)
- A documentation is not just a single word; it's a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## Tasks

### 0. What's my status? #0 (mandatory)

Write a Python script that fetches https://alx-intranet.hbtn.io/status. You must use the `urllib` package, and you are not allowed to import any packages other than `urllib`. The body of the response must be displayed as shown in the example.

Example:

```shell
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
```

### 1. Response header value #0 (mandatory)

Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response. You must use the `urllib` and `sys` packages, and you are not allowed to import any packages other than `urllib` and `sys`. The value of this variable is different for each request.

Example:

```shell
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
```

### 2. POST an email #0 (mandatory)

Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8). The email must be sent in the `email` variable. You must use the `urllib` and `sys` packages, and you are not allowed to import any packages other than `urllib` and `sys`.

Example:

```shell
guillaume@ubuntu@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```

### 3. Error code #0 (mandatory)

Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8). You must manage `urllib.error.HTTPError` exceptions and print "Error code:" followed by the HTTP status code. You must use the `urllib` and `sys` packages, and you are not allowed to import any packages other than `urllib` and `sys`.

Example:

```shell
guillaume@ubuntu@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:500

0/status_500
Error code: 500
```

### 4. What's my status? #1 (mandatory)

Write a Python script that fetches https://alx-intranet.hbtn.io/status using the `requests` package. You are not allowed to import packages other than `requests`. The body of the response must be displayed as shown in the example.

Example:

```shell
guillaume@ubuntu@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
```

### 5. Response header value #1 (mandatory)

Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable in the response header. You must use the `requests` and `sys` packages, and you are not allowed to import any packages other than `requests` and `sys`. The value of this variable is different for each request.

Example:

```shell
guillaume@ubuntu@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
```

### 6. POST an email #1 (mandatory)

Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response. The email must be sent in the variable `email`. You must use the `requests` and `sys` packages, and you are not allowed to import any packages other than `requests` and `sys`.

Example:

```shell
guillaume@ubuntu@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
```

### 7. Error code #1 (mandatory)

Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response. If the HTTP status code is greater than or equal to 400, print "Error code:" followed by the value of the HTTP status code. You must use the `requests` and `sys` packages, and you are not allowed to import any packages other than `requests` and `sys`.

Example:

```shell
guillaume@ubuntu@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
```

### 8. Search API (mandatory)

Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter. The letter must be sent in the variable `q`. If no argument is given, set `q=""`. If the response body is properly JSON formatted and not empty, display the id and name as shown in the example. Otherwise, display "Not a valid JSON" if the JSON is invalid, and "No result" if the JSON is empty. You must use the package `requests` and `sys`, and you are not allowed to import any packages other than `requests` and `sys`.

Example:

```shell
guillaume@ubuntu@ubuntu:~/0x11$ ./8-json_api.py 
No result
guillaume@ubuntu@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
guillaume@ubuntu@ubuntu:~/0x11$ ./8-json_api.py 2
No result
guillaume@ubuntu@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
```

### 9. My GitHub! (mandatory)

Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id. You must use Basic Authentication with a personal access token as the password to access your information (only read:user permission is needed). The first argument will be your username, and the second argument will be your password (in your case, a personal access token as the password). You must use the package `requests` and `sys`, and you are not allowed to import any packages other than `requests` and `sys`. You don't need to check arguments passed to the script (number or type).

Example:

```shell
guillaume@ubuntu@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
guillaume@ubuntu@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
```

---
