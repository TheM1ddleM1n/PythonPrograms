import html
import json
import urllib.request
import xml.etree.ElementTree as ET


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode("utf-8", errors="ignore")


def scrape_bbc(limit=10):
    content = fetch("https://feeds.bbci.co.uk/news/rss.xml")
    root = ET.fromstring(content)
    channel = root.find("channel")

    results = []
    for item in channel.findall("item")[:limit]:
        title = item.findtext("title", "").strip()
        link = item.findtext("link", "").strip()
        if title and link:
            results.append((title, link))

    return results


def scrape_hackernews(limit=10):
    raw = fetch("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = json.loads(raw)[:limit]

    stories = []
    for sid in story_ids:
        try:
            data = fetch(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
            item = json.loads(data)
            title = html.unescape(item.get("title", "")).strip()
            link = item.get("url") or f"https://news.ycombinator.com/item?id={sid}"
            if title:
                stories.append((title, link))
        except Exception:
            continue

    return stories


def display(source, headlines):
    print(f"\n 📰 {source}")
    print("  " + "=" * 50)
    if not headlines:
        print("Nothing came back — please check your connection")
        return
    for i, (title, link) in enumerate(headlines, 1):
        print(f"\n  {i}. {title}")
        print(f"🔗 {link}")


def main():
    print("\n📰 WEB SCRAPER")
    print("=" * 40)
    print("Pulls headlines from BBC and Hacker News.\n")

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
            print("1-4 only!")
            continue

        print("\nPlease wait while fetching takes place...")
        try:
            if choice in ("1", "3"):
                display("BBC News", scrape_bbc())
            if choice in ("2", "3"):
                display("Hacker News", scrape_hackernews())
        except Exception as e:
            print(f"⚠️ Failed to fetch: {e}")

        print()


if __name__ == "__main__":
    main()
