# Peter Parker

This is a simple webcrawler made for work to collect urls visited from the target site in a log with their status codes and a time stamp.
The idea is simply to see if there are any 4XX or 5XX errors.

### Setup

First install a virtual environment. -- python -m venv "name of environment"

Then, use your terminal to activate it. ~ source venv/bin/activate

Once your virtual environment is activated, run pip install -r requirements.txt

### Commands
If you simply need a lot, all you have to type is scrapy crawl spiderman. This will save a log. Which has the timestamp TheDailyBugle-YYYYMMDD.HHMM.log.

That can be changed in the settings.py file.

If you want the output the results to JSON simply type scrapy crawl spiderman -o filename.json.

### Ideas
Will add in a way to check nginx version in each request and log it for 4XX / 5XX errors.