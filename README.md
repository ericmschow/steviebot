# steviebot
Twitter bot that posts random Steven Wilson lyrics. See it in action [here](https://twitter.com/StevenWilsonBo1).

Created because I've been focused on Javascript for the past year or so, and I wanted to brush up on my Python.

To use:
* `pip3 install` these modules: `bs4`, `python-dotenv`, `python-twitter`
* Save album lyrics .html pages from DarkLyrics.com to the lyrics directory. `Mkdir lyrics` if necessary.
* `python3 parser.py` to process html files into main directory. Needs to be from DarkLyrics, for the html parser to work correctly.
* Follow the setup instructions on [Python-Twitter's documentation](http://python-twitter.readthedocs.io/en/latest/getting_started.html), saving the values to a file named SECRETS.ENV.
* `python3 main.py` to publish a tweet containing a random Steven Wilson lyric, or whatever artist you chose to download.

