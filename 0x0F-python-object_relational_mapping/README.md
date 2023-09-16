```markdown
# Python - Object-Relational Mapping

![Python](https://img.shields.io/badge/Python-3.8.5-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.x-blue)

This project demonstrates the use of Object-Relational Mapping (ORM) in Python, focusing on connecting to a MySQL database, executing SQL queries, and using SQLAlchemy as an ORM tool. The goal is to bridge the gap between databases and Python, abstracting storage and enabling easy manipulation of data through Python code.

## Table of Contents
- [Background Context](#background-context)
- [Before You Start](#before-you-start)
- [Tasks](#tasks)
  0. [Get all states](#0-get-all-states)
  1. [Filter states](#1-filter-states)
  2. [Filter states by user input](#2-filter-states-by-user-input)
  3. [SQL Injection...](#3-sql-injection)
  4. [Cities by states](#4-cities-by-states)
  5. [All cities by state](#5-all-cities-by-state)
  6. [First state model](#6-first-state-model)
  7. [All states via SQLAlchemy](#7-all-states-via-sqlalchemy)
  8. [First state](#8-first-state)
  9. [Contains 'a'](#9-contains-a)
  10. [Get a state](#)
  11. [Add a new state](#11-add-a-new-state)
  12. [Update a state](#12-update-a-state)
  13. [Delete states](#13-delete-states)
  14. [Cities in state](#14-cities-in-state)
- [Usage](#usage)
- [License](#license)

## Background Context
In this project, you will explore the world of Object-Relational Mapping (ORM) in Python. You will connect to a MySQL database, execute SQL queries, and utilize the SQLAlchemy library as an ORM tool. The aim is to abstract away the complexity of database interactions and perform operations using Python code.

## Before You Start
Before diving into the tasks, make sure you have MySQL 8.0 installed. If you're using Ubuntu 20.04, you can follow these steps to install MySQL 8.0:

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```

Also, install SQLAlchemy version 1.4.x:

```bash
$ sudo pip3 install SQLAlchemy
```

Please note that you may encounter a warning message during installation, which you can safely ignore.

## Tasks

## Usage
To run any of the provided scripts, use the following format:

```bash
$ ./script_name.py <username> <password> <database_name> <additional_arguments>

## License

This project is protected by the ALX license. All rights reserved.
```
