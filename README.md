The URLs from each department page are scraped using `url_scraper.py` and are saved in a 1 column `.csv` called `courses.csv`. `course_scraper.py` is then used to go through each URL listed in `courses.csv` and writes each section to `coursedata.csv`.

Do not have new line at end of `courses.csv`
