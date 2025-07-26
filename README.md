📱 Wikipedia Android App – Mobile Test Automation Framework
🔧 Project Summary
This project showcases a mobile native app automation framework built using Python, Appium, and Behave (BDD).
The automation targets the Wikipedia Android application, focusing on validating its search functionality through end-to-end test flows.

The framework is designed using the Page Object Model (POM) architecture for clean code organization and scalability.
Tests were executed on Android Studio emulators and validated using Appium Inspector to ensure locator reliability and test robustness.

✅ What I Accomplished
✅ Built a mobile automation framework from scratch using Python + Appium + Behave

✅ Successfully tested the search functionality of the Wikipedia app

✅ Created dynamic and reusable Page Objects for core screens and UI components

✅ Integrated BDD Gherkin scenarios to validate user interactions and app behavior

✅ Practiced using Appium Inspector to locate mobile elements dynamically

✅ Validated test cases using real and emulated Android devices

🧪 Tools & Technologies
Tool	Purpose
Python	Test scripting
Appium	Mobile automation driver
Behave (BDD)	Writing readable test cases with Gherkin
Android Studio	Emulator/device management
Appium Inspector	Element inspection and locator validation
POM (Design)	Code reusability & maintainability

📁 Framework Structure
bash
Copy
Edit
python-appium-automation/
│
├── app/                        # App-level utilities (optional)
│
├── features/
│   ├── steps/                  # Step definitions
│   └── tests/                  # Feature files & environment setup
│       ├── wiki_search.feature
│       ├── environment.py
│       └── __init__.py
│
├── mobile_app/                # Appium driver/session utils
│
├── pages/                     # Page Object Model classes
│
├── screenshots/               # Saved screenshots during test runs
│
├── appium_script.py           # Optional runner or utility script
├── .gitignore
└── README.md
🧪 Sample Gherkin Scenario
gherkin
Copy
Edit
Scenario: User can search on Wikipedia
  Given Click to Skip onboarding
  When Click Search icon
  And Search for "Python (programming language)"
  Then Verify first result is "Python (programming language)"
▶️ How to Run the Tests
🔧 Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
📱 Start Android Emulator using Android Studio

🚀 Launch Appium Server

🧪 Run Behave Tests

bash
Copy
Edit
behave features/tests/wiki_search.feature
📸 Screenshots
Screenshots are saved automatically to the /screenshots/ directory after each test run.

📌 Notes
Appium sessions are managed dynamically before and after each scenario using environment.py

Element locators are built to be flexible and reusable across screens

The Wikipedia app was used strictly for educational and testing purposesreens

The Wikipedia app was used for educational automation testing purposes only
