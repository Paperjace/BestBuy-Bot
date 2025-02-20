# RTX Best Buy Bot

## Features
- Automatically logs into Best Buy account
- Refreshes link until "Add to Cart" button is available
- Automate entire checkout process

## Prerequisites
- Sign up for a Best Buy account
- Add all billing/shipping info to your account (must only have one card on the account)
- Download and install [Python](https://www.python.org/)

## Dependencies
- Selenium
	- `pip install selenium`
- Setuptools
  - `pip install setuptools`
- undetected_chromedriver
  - `pip install undetected_chromedriver`
- plyer
  - `pip install plyer`
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/)

## Running the Bot
1. Rename ex.info.py to info.py
2. Edit the info.py file with your Best Buy account email and password and cvv for the card on the account
3. Navigate to your project directory and run the bot.py script from your preferred environment
4. Feel free to change the Best Buy links in the bot.py file to any item on bestbuy.com
	- **NOTE:** From testing it appears that it depends on the price of the item wheter or not the cvv number is asked for. If you plan to use this bot for something cheaper you may need to remove/comment the segment of code detecting and filling in the cvv field.


