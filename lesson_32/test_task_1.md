# SOURCE: https://github.com/p2cbbb/torrow_qa_test

# Test task for the position SDET/QA Automation Engineer

## The task is:
> Write several scenarios for the authentication process.

Examples of scenarios:
 - A successful autency. by sms/email
 - Autent. sms/email with incorrect code entered once or more
 - Too much waiting for code input

# Appendix:
Приложение для тестирования находится по адресу https://dev1.torrow.net
The sent code to the phone/email can be obtained by the following addresses:
- https://smsdev1.torrow.net/api/phone/phone/[phoneNumber]

  (example: https://smsdev1.torrow.net/api/phone/7911123456)
- https://emaildev1.torrow.net/api/email/[email]

  (example: https://smsdev1.torrow.net/api/abc@gmail.com)

# Requirements:
- The test project should be written in Python and Selenium.
- Use PageObject pattern (ex.: https://docs.specflow.org/projects/specflow/en/latest/ui-automation/Selenium-with-Page-Object-Pattern.html) 

# SOLUTION:

## Copy repository and dependency installation
```bash
git clone https://github.com/p2cbbb/torrow_qa_test
cd torrow_qa_test
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Running the tests
 - Before the test is launched, you need to go to the project directory `torrow_qa_test`

Arguments of the launch:
- -s - show the awnings in the process of execution
- -v - verbose mode to see which tests were launched
```bash
python -m pytest -v -s test_torrow_auth.py
```
