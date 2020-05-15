from bs4 import BeautifulSoup
import urllib.request
import argparse

def main():

    parser=argparse.ArgumentParser()
    parser.add_argument('-s', action='store', dest='site',
                    help='the site to be parsed')

    args=parser.parse_args()
    url=args.site

    # html=''
    with urllib.request.urlopen(url) as response:
        html=response.read()

    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    print(text)

if __name__ == "__main__":
    main()
