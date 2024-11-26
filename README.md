Bing Point Collector 🤖


🤔 What Does the App Do? 🤔

This app automates the process of collecting Bing search rewards by:

    Compiling a Bing URL using AI-generated prompts.
    Copying the URL, pasting it into the browser, and performing searches.
        The default is 10 searches. To change this, modify the following line in the code:

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

    Clone the Repository:

git clone https://github.com/Mr-Banana-Egg/Bing_point_collector.git

Install Dependencies:

cd BrawlStarsBot
pip install -r requirements.txt

Update the Repository (if needed):

    cd BrawlStarsBot
    git pull

🔧 Improvements to Be Made 🔧

    Add support for macOS.





