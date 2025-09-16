# 📱 Wikipedia Android App – Mobile Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Appium](https://img.shields.io/badge/Appium-Mobile--Testing-green)
![Behave](https://img.shields.io/badge/BDD-Behave-yellow)
![Status](https://img.shields.io/badge/Status-Working-success)

---

## 🔧 Project Summary

This is a **mobile automation framework** built using **Python**, **Appium**, and **Behave (BDD)** to test the **Wikipedia Android app**.  
It automates **search functionality** using real and emulated devices via Android Studio.

The code is organized using the **Page Object Model (POM)** for reusability and scalability.  
All UI elements are dynamically located using **Appium Inspector**, and test flows are written in **Gherkin syntax**.


https://github.com/user-attachments/assets/7f01ef5b-38db-4e87-8530-7b608fc3831e

---

## ✅ What I Accomplished

- ✅ Built a complete mobile automation framework using **Python + Appium + Behave**
- ✅ Successfully tested the **search functionality** of the **Wikipedia app**
- ✅ Designed dynamic and reusable **Page Objects**
- ✅ Wrote **BDD Gherkin scenarios** for clear test documentation
- ✅ Practiced using **Appium Inspector** for accurate mobile element location
- ✅ Executed tests on **real and emulated Android devices**

---

## 🧪 Tools & Technologies

| Tool             | Purpose                                      |
|------------------|----------------------------------------------|
| Python           | Test scripting                               |
| Appium           | Mobile automation driver                     |
| Behave (BDD)     | Writing readable test cases with Gherkin     |
| Android Studio   | Emulator/device management                   |
| Appium Inspector | Element inspection and locator validation    |
| POM (Design)     | Code reusability & maintainability           |

Appium setup instructions are [here](https://docs.google.com/document/d/1d8uaQW4R4MPP1XMDiUH8B3VjzgDYQo1oAkQ_oeS4qwk/edit#).


---

## 📁 Framework Structure

python-appium-automation/
│
├── app/ # App-level utilities (optional)
│
├── features/
│ ├── steps/ # Step definitions
│ └── tests/ # Feature files & environment
│ ├── wiki_search.feature
│ ├── environment.py
│ └── init.py
│
├── mobile_app/ # Appium driver/session utils
├── pages/ # Page Object Model classes
├── screenshots/ # Test execution screenshots
├── appium_script.py # Optional runner script
├── requirements.txt # Python dependencies
├── .gitignore # Ignore rules
└── README.md

---

## 🧪 Sample Gherkin Scenario

```gherkin
Feature: Wikipedia search functionality

  Scenario: User can search on Wikipedia
    Given Click to Skip onboarding
    When Click Search icon
    And Search for "Python (programming language)"
    Then Verify first result is "Python (programming language)"

---

## ▶️ How to Run the Tests
📦 Setup Instructions
🔧 Install dependencies
📱 Start Android Emulator using Android Studio
🚀 Launch Appium Server
🧪 Run Behave Tests

---

## 📸 Screenshots
Screenshots are saved automatically to the /screenshots/ directory after each test run.


## 📌 Note:

Appium sessions are managed before and after each scenario using environment.py

Locators and actions are modular and reusable across the app

This project is built for educational and demo purposes only

🔗 Credits
Created by Nicholas Olumese
Automation Engineer 
