import pyautogui
import time
import pyperclip
import random
ammount=int(10)#Change  the ammount you want to search (if needed)
#sq (by Chat GPT)
sq = ["Symptoms of the flu",
    "Best exercise for weight loss",
    "Who won the Nobel Prize in Physics 2023?",
    "How to improve your sleep quality",
    "Tips for better time management",
    "How to start a small business",
    "Latest iPhone release date",
    "What is the square root of 144?",
    "Best books of all time",
    "What causes global warming?",
    "How to train for a marathon",
    "How to make a budget plan",
    "Who is the current president of the USA?",
    "What is machine learning?",
    "How to reduce stress at work",
    "What are the health benefits of meditation?",
    "Best places to visit in Europe",
    "What are the symptoms of anxiety?",
    "What is cryptocurrency?",
    "How does solar energy work?",
    "Top 5 movies to watch in 2024",
    "How to create a website from scratch",
    "What is the meaning of life?",
    "How to learn a new language fast",
    "What is the best diet for weight loss?",
    "Top tourist destinations in Asia",
    "What is artificial intelligence?",
    "How to fix a leaky faucet",
    "What is blockchain technology?",
    "How to make homemade pizza",
    "Best productivity tools for remote teams",
    "What is the Pythagorean theorem?",
    "How to improve your public speaking skills",
    "Top 10 video games of 2024",
    "How to become a digital nomad",
    "What is quantum computing?",
    "What are the side effects of caffeine?",
    "What is the difference between a virus and bacteria?",
    "How to write a great resume",
    "What is the best way to learn to code?",
    "How to save money on groceries",
    "How does a car engine work?",
    "What are the best strategies for SEO?",
    "What is the theory of relativity?",
    "How to make a smoothie",
    "Best practices for email marketing",
    "What is the difference between an asteroid and a comet?",
    "How to plan a wedding on a budget",
    "What is the best way to invest money?",
    "What is a good credit score?",
    "How to start a YouTube channel",
    "What are the signs of depression?",
    "What is a good skincare routine?",
    "How to make a good first impression",
    "What is sustainable living?",
    "How to build a personal brand",
    "How to improve your concentration",
    "What is the best time to exercise?",
    "How to get rid of acne",
    "What is the ketogenic diet?",
    "How to improve your relationship",
    "What is social media marketing?",
    "What is a phishing attack?",
    "How to grow a vegetable garden",
    "What is the best way to meditate?",
    "How to improve your writing skills",
    "What are the top tourist attractions in the USA?",
    "What is the best way to lose belly fat?",
    "What are the causes of climate change?",
    "How to train your dog",
    "How to create a successful business plan",
    "What is the best workout routine for beginners?",
    "How to build a mobile app",
    "What is the best way to prepare for a job interview?",
    "What is the meaning of a dream about flying?",
    "How to organize your home",
    "What is a healthy breakfast?",
    "How to improve your credit score",
    "What is a good way to study for exams?",
    "How to become a millionaire",
    "What is a smart home?",
    "What is the meaning of success?",
    "How to deal with loneliness",
    "How does the internet work?",
    "What are the symptoms of COVID-19?",
    "How to write a cover letter",
    "What is the best way to take care of plants?",
    "How to get rid of a headache",
    "What are the benefits of yoga?",
    "What is an NFT?",
    "How to create an effective marketing strategy",
    "How does cryptocurrency mining work?",
    "What are the best online learning platforms?",
    "How to stop procrastinating",
    "What is a good hobby to start?",
    "How to be more productive",
    "What is the best way to learn to play guitar?",
    "What is a healthy body fat percentage?",
    "How to find a good therapist",
    "What is digital marketing?",
    "How to become a better listener",
    "What is the best way to study languages?",
    "What are the effects of sugar on the body?",
    "How to plan a road trip",
    "What is mindfulness meditation?",
    "How to get rid of stress",
    "What is a healthy diet for a teenager?",
    "How to create a YouTube thumbnail",
    "What are the benefits of reading books?",
    "How to do a plank exercise",
    "How to write a book",
    "What is the best way to do cardio?",
    "How to stay motivated",
    "What are the benefits of drinking water?",
    "How to plan a vacation on a budget",
    "What is a digital nomad lifestyle?",
    "How to maintain mental health",
    "What is the most expensive car in the world?",
    "How to improve your focus",
    "What are the top social media platforms in 2024?",
    "How to reduce your carbon footprint",
    "What is deep learning?",
    "What is the importance of networking?",
    "How to stay fit at home",
    "What are the symptoms of a panic attack?",
    "How to use Google Analytics",
    "What is the meaning of life according to philosophy?",
    "How to teach a dog to sit",
    "What are the benefits of journaling?",
    "How to build a website with WordPress",
    "How to reduce food waste",
    "What is the best way to lose weight?",
    "How to get over a breakup",
    "What are the top job skills in 2024?",
    "How to deal with a difficult coworker",
    "What is an ideal work-life balance?",
    "How to manage anxiety",
    "What are the top healthy snacks?",
    "How to prevent hair loss",
    "What is time management?",
    "How to get rid of belly fat fast",
    "What are the best websites for learning new skills?",
    "What is positive thinking?",
    "How to make a good impression in an interview",
    "What is an influencer?",
    "How to build self-confidence",
    "What are the symptoms of high blood pressure?",
    "How to plan a wedding",
    "What is a growth mindset?",
    "What is the best exercise for building muscle?",
    "What is the best way to save for retirement?",
    "How to teach a child to read",
    "What is the best way to learn to code?",
    "How to write a business proposal",
    "How to increase your followers on Instagram",
    "What is the ketogenic diet?",
    "What is a healthy amount of sleep?",
    "How to deal with stress at work",
    "What is the best way to meditate?",
    "How to keep your home clean and organized",
    "What is a balanced diet?",
    "What are the benefits of exercise?",
    "How to create a financial plan",
    "What is the best career for introverts?",
    "How to deal with rejection",
    "How to make a website with HTML and CSS",
    "What is the best skincare routine for oily skin?",
    "How to create a vision board",
    "How to overcome procrastination",
    "What is a good career?",
    "What is the best book for personal development?",
    "How to be a better communicator",
    "What are the benefits of laughter?",
    "What is the meaning of true friendship?",
    "How to learn public speaking",
    "What is a sustainable diet?",
    "How to be more creative",
    "What is the best online course platform?",
    "What is the best way to learn photography?",
    "What is a minimalistic lifestyle?",
    "How to break a bad habit",
    "What is a growth mindset?",
    "What is a good side hustle?",
    "How to start a podcast",
    "How to make a healthy smoothie",
    "What is the most important skill for success?",
    "How to organize your digital files",
    "What is the best way to improve communication skills?",
    "What is a good workout routine for beginners?"]
        # List of search queries 

def main():
    """
    Documented by TABNINE Ai
    This function is the main entry point for the program. It performs the following tasks:
    1. Selects a random search query from a predefined list.
    2. Constructs a Bing search URL using the selected query.
    3. Copies the Bing search URL to the clipboard.
    4. Opens a new browser tab.
    5. Pastes the Bing search URL into the new tab and presses Enter to initiate the search.
    6. Waits for 5 seconds before proceeding to the next iteration.

    Parameters:
    None

    Returns:
    None
    """
    # Use random.choice() to pick a random item from the list
    r = random.choice(sq)

    url = f"https://www.bing.com/search?q={r}&cvid=82484d919090408c8f9c2742d420e897&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQLhhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQRRg8MgYICBBFGEHSAQc0NTBqMGoxqAIAsAIA&FORM=ANAB01&PC=HCTS&adlt=strict&toWww=1&redig=398A84E54280498486653D75EBA7A6F0"

    pyperclip.copy(url)
    print("[INFO]: Copied Bing search URL to clipboard.")
    time.sleep(1)

    print("[INFO]: Opening new tab.")
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)

    print("[INFO]: Pasting URL and pressing Enter.")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(5)

def getter():
    global ammount
    if ammount > 0:
        main()
        ammount -= 1  # Decrease ammount by 1
        getter()  # Recursive call to continue the process
    else:
        print("[INFO]: Finished")
        exit()

# Start the process
getter()

    
  

    





