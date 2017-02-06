# HW_scraper
Python based web scraper for homework aggregation
It grabs homework assignments from my class's site and inserts it into my planner application's internal SQL database
Code can be configured to automatically run in the background, to do so the user should take the contents of the .crontab file supplied in the repo
and paste it into a file ~/.crontab (or create one if necessary)
There are instructions in the file on its finer configuration points

Tested on macOS 10.12.3 (Sierra)
