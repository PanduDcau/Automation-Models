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

### 3. Setup Method
The setUpClass class method initializes the Chrome WebDriver, maximizes the window, and sets an implicit wait.
```python
@classmethod
def setUpClass(cls):
    options = webdriver.ChromeOptions()
    cls.driver = webdriver.Chrome(options=options)
    cls.driver.implicitly_wait(10)
    cls.driver.maximize_window()
```
### 4. Setup Method
Two test methods are defined to perform Google searches.
##### a. 'test_search_automationstepbystep'
This method searches for "Automation Step by Step".
```python
@classmethod
def test_search_automationstepbystep(self):
    self.driver.get("https://google.com")
    self.driver.find_element("name", "q").send_keys("Automation Step by Step")
    self.driver.find_element("name", "btnK").click()
```
##### b. 'test_search_pandu'
This method searches for "Batman Costumes".
```python
def test_search_pandu(self):
    self.driver.get("https://google.com")
    self.driver.find_element("name", "q").send_keys("Batman Costumes")
    self.driver.find_element("name", "btnK").click()
    self.driver.implicitly_wait(5)
```

### 5. Setup Method
The tearDownClass class method closes the browser and quits the WebDriver.
```python
@classmethod
def tearDownClass(cls):
    cls.driver.close()
    cls.driver.quit()
    print("Test Completed")
```

## How to run the Script
1. Clone the Repository: Clone the repository to your local machine or download the _Googlesearch.py_ file.
2. Navigate to the Project Directory: Open a terminal and navigate to the directory containing _Googlesearch.py_.
3. Execute the Script: Run the script using Python.

`python Googlesearch.py`


### Success Junit Test - example
```
Launching unittests with arguments python -m unittest Googlesearch.py 

Test Completed


Ran 2 tests in 6.358s

OK

Process finished with exit code 0
```


#### python -m unittest Googlesearch.py
