[![Python application](https://github.com/wernaw/app_calculator/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/wernaw/app_calculator/actions/workflows/python-app.yml)

[![Pylint](https://github.com/wernaw/app_calculator/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/wernaw/app_calculator/actions/workflows/pylint.yml)

# Flask Calculator App

A simple **Flask** web application that provides basic arithmetic operations: **sum**, **subtract**, **multiply**, and **divide**.  
Includes unit tests with **pytest** and code coverage reporting.

---

## Features

- Perform arithmetic operations via HTTP GET requests:
  - `sum` – addition
  - `subtract` – subtraction
  - `multiply` – multiplication
  - `divide` – division (handles division by zero)
- Unit tests for all operations.
- Code coverage report in HTML format.

---

## Requirements

- Python 3.14  
- Flask  
- pytest  
- coverage  

You can install the dependencies via:

```bash
pip install -r requirements.txt
