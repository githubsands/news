from bs4 import BeautifulSoup
import os
import twitter
import urllib.request
import argparse
import sys
import yaml

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-s', action='store', dest='site',
                    help='the site URL to be parsed')

    parser.add_argument('-k', action='store', dest='key',
                    help='twitter consumer key')

    parser.add_argument('-t', action='twitter_user', dest='twitter_user',
                    help='twitter user to scrape')

    args=parser.parse_args()

    # just scrape a site
    if args.twitter_user is None:
        if args.key is None:
            sys.exit("No key given")
        if args.site is None:
            sys.exit("No site URL given")

        with urllib.request.urlopen(url) as response:
            html=response.read()

        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        print(text)
        sys.exit("Scraped job complete")

    # scrape a site from a tweet
    if args.key is None:
        sys.exit("No key given")

    if args.twitter_user is None:
        sys.exit("No twitter user given")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(BASE_DIR + '/config.yaml') as file:
        cfg = yaml.full_load(file)

    api = twitter.Api(consumer_key=cfg.consumer_key,
        consumer_secret=cfg.consumer_secret,
        access_token_key=cfg.access_token,
        access_token_secret=cfg.access_token_secret)

    statuses = api.GetUserTimeLine(screen_name=args.twitter_user)
    print([s.text for s in statuses])

    #
    # soup = BeautifulSoup(html, 'html.parser')
    # text = soup.get_text()
    # print(text)

if __name__ == "__main__":
    main()
