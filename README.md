<h1 align="center">
  <b>Movie Download Automation</b>
</h1>

<p align="center">
  Movie Download Automation (movie_ls) is a Python package designed to scrape and aggregate movie links from various sources. It provides a simple interface to fetch movie streaming or download links programmatically.
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/movie_ls-v1.0.0-crimson" alt="movie_ls version"></a>
  <a href="https://github.com/minkxx/movie_download_automation/stargazers"><img src="https://img.shields.io/github/stars/minkxx/movie_download_automation?style=flat-square&color=yellow" alt="Stars"></a>
  <a href="https://github.com/minkxx/movie_download_automation/fork"><img src="https://img.shields.io/github/forks/minkxx/movie_download_automation?style=flat-square&color=orange" alt="Forks"></a>
  <a href="https://github.com/minkxx/movie_download_automation/"><img src="https://img.shields.io/github/repo-size/minkxx/movie_download_automation?style=flat-square&color=green" alt="Repo Size"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-v3.13.1-blue" alt="Python"></a>
  <a href="https://github.com/minkxx/movie_download_automation/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue" alt="License"></a>
</p>

## Features

- Supports multiple sources (customizable)
- Clean and well-documented codebase

## Installation

Install the latest version from [PyPI](https://pypi.org/project/movie-ls/) using pip:

```bash
pip install movie_ls
```

## Usage

Below is an example usage:

```python
from movie_ls.driver import SeleniumDriver
from movie_ls.web_page_extractor import WebPageExtractor
from movie_ls.parsers.hdhub4u_html_parser import HdHub4uHtmlParser
from movie_ls.services.mediator_page import HbLinksFromMediatorPage

BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
CHROME_DRIVER_PATH = r"drivers/chromedriver.exe"

def run_main():
    print("--------------------- Get Movie Links Automation ---------------------")
    download_query = input("Enter Movie/Web Series name : ")
    driver = SeleniumDriver(browser_path=BRAVE_PATH, driver_path=CHROME_DRIVER_PATH).get_driver()
    print("Extracting web page...")
    extractor = WebPageExtractor(driver)
    webpage_html = extractor.extract(f"https://hdhub4u.fail/?s={download_query.replace(' ', '%20')}")
    print("webpage extracted")
    print("Parsing webpage...")
    media_links = HdHub4uHtmlParser.parse_media_links(webpage_html)
    print(f"{len(media_links)} media links found")
    for index, m in enumerate(media_links):
        print(f"{index+1}. {m['caption']}")
        print()
    choice = int(input("Select a media link : "))
    media_link = media_links[choice-1]['page_url']
    print("Selected media link : ", media_link)
    print("Extracting download links page...")
    extractor = WebPageExtractor(driver)
    pack_links = HdHub4uHtmlParser.parse_download_links(extractor.extract(media_link))
    print(f"{len(pack_links)} packs found")
    for index, d in enumerate(pack_links):
        key, value = list(d.items())[0]
        print(f"{index+1}. {key}")
        print()
    choice = int(input("Select a download link : "))
    pack_link = list(pack_links[choice-1].items())[0][1]
    print("Selected page link : ", pack_link)
    print("Fetching all download link...")
    hb_extractor = HbLinksFromMediatorPage(driver, pack_link)
    download_links = hb_extractor.get_hubcloud_download_links()
    if not download_links:
        print("No mediator page found. We are still working for it.")
        return
    print(f"{len(download_links)} download links found")
    for i, (text, href) in enumerate(download_links, 1):
        print(f"{i}. {text}\n   URL: {href}\n")


if __name__ == "__main__":
    run_main()
```

## Dependencies

- `beautifulsoup4`
- `selenium`

All dependencies are automatically installed with `pip install movie_ls`.

## Repository

Find the source code, issues, and contribution guidelines on GitHub:  
[Movie Download Automation](https://github.com/minkxx/movie_download_automation)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

---

**Note:** This package is intended for educational and personal use. Please respect the terms of service of any websites you scrape.
