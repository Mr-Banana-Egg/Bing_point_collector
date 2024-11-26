# Bing Point Collector 🤖

## 🤔 What Does the App Do? 🤔

This app automates the process of collecting Bing search rewards by:

1. Compiling a Bing URL using AI-generated prompts.
2. Copying the URL, pasting it into the browser, and performing searches.
   - The default is 10 searches. To change this, modify the following line in the code:
   
   ```python
   amount = int(10)  # Change the amount if needed

    After the searches, the app will open Microsoft Rewards and click the buttons to claim rewards.
        Button coordinates can be calibrated using the provided program. Update the coordinates in the following areas:

    reward_button_coords = [(939, 1649), (1766, 1649), (2404, 1649)]  # First set of coordinates
    secondary_coords = [(300, 1649), (939, 1649), (1766, 1649), (2404, 1649)]  # After scrolling

‼️ Requirements ‼️

    Windows OS
    Python
    Required libraries (see below for installation)

🔽 How to Install 🔽

```To install it you need to click on the Releases tab and install the source code as a zip unzip it and do 

1. cd Bing_point_collector-s

2.pip install -r requirements.txt
This will install the needed packages 
After that run "Bing point getter"
to use the App.

🔧 Improvements to Be Made 🔧

    Add support for macOS.












