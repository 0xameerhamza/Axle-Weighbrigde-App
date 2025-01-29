@echo off
call venv\scripts\activate
rem pip install openpyxl
rem pip install pytest-html
rem pytest -s -v -m "smoke" --html .\reports\test_report_chrome.html
pytest -s -v --html .\reports\test_report_chrome.html
rem pytest -s -v -m "TripVerification"  --html .\reports\test_report_chrome.html
pause