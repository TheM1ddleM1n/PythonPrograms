"""Web scraper — grabs headlines from BBC News and Hacker News.
"""
import html
import re
import urllib.request


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode("utf-8", errors="ignore")


def scrape_bbc(limit=10):
    # BBC publishes a proper RSS feed so this is clean and reliable
    content = fetch("https://feeds.bbci.co.uk/news/rss.xml")
    titles = re.findall(r"<title><!\[CDATA\[(.*?)\]\]></title>", content)
    links = re.findall(r"<link>(https://www\.bbc\.co\.uk/news/.*?)</link>", content)

    titles = [t for t in titles if t != "BBC News"][:limit]
    links = links[:limit]
    return list(zip(titles, links))


def scrape_hackernews(limit=10):
    # Hacker News has a proper JSON API, so again no scraping trickery needed
    top_ids_raw = fetch("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = re.findall(r"\d+", top_ids_raw)[:limit]

    stories = []
    for sid in story_ids:
        try:
            data = fetch(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
            title_match = re.search(r'"title":"(.*?)"', data)
            url_match = re.search(r'"url":"(.*?)"', data)
            if title_match:
                title = html.unescape(title_match.group(1))
                link = url_match.group(1) if url_match else f"https://news.ycombinator.com/item?id={sid}"
                stories.append((title, link))
        except Exception:
            continue

    return stories


def display(source, headlines):
    print(f"\n 📰 {source}")
    print("  " + "=" * 50)
    if not headlines:
        print("  Nothing came back — check your connection!")
        return
    for i, (title, link) in enumerate(headlines, 1):
        print(f"\n  {i}. {title}")
        print(f"     🔗 {link}")


def main():
    print("\n📰 WEB SCRAPER")
    print("=" * 40)
    print("  Pulls headlines from BBC and Hacker News.\n")

    while True:
        print("1. BBC News")
        print("2. Hacker News")
        print("3. Both")
        print("4. Exit")

        choice = input("\nPick: ").strip()

        if choice == "4":
            print("\n👋 Stay informed!")
            break

        if choice not in ("1", "2", "3"):
            print("  1-4 only!")
            continue

        print("\nFetching...")
        try:
            if choice in ("1", "3"):
                display("BBC News", scrape_bbc())
            if choice in ("2", "3"):
                display("Hacker News", scrape_hackernews())
        except Exception as e:
            print(f"  ⚠️ Failed to fetch: {e}")

        print()


if __name__ == "__main__":
    main()
