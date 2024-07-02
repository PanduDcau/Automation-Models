# GoogleSearch Selenium Test

This project contains a Selenium-based test script for performing Google searches. The tests are written in Python using the `unittest` framework and `HtmlTestRunner` for generating HTML reports.

## Prerequisites

1. **Python**: Make sure Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **ChromeDriver**: Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's accessible in your system's PATH or specify its location in the script.

3. **Selenium**: Install the Selenium package using pip.
    ```sh
    pip install selenium
    ```

4. **HtmlTestRunner**: Install HtmlTestRunner using pip.
    ```sh
    pip install test-HtmlTestRunner
    ```

## Project Structure


## Script Breakdown

### 1. Import Required Libraries

The script starts by importing the necessary libraries: `webdriver` from `selenium`, `unittest`, and `HtmlTestRunner`.

```python
from selenium import webdriver
import unittest
import HtmlTestRunner
```

### 2. Define the Test Class
A class GoogleSearch is defined, inheriting from unittest.TestCase.
```python
class GoogleSearch(unittest.TestCase):
```

### Success Junit Test - example
```
Launching unittests with arguments python -m unittest Googlesearch.py 

Test Completed


Ran 2 tests in 6.358s

OK

Process finished with exit code 0
```


#### python -m unittest Googlesearch.py
