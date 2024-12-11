import requests
import time


def main():

    topstories = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()[:30]

    for story_id in topstories:
        time.sleep(1)
        story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json").json()
        if story.get("title") and story.get("url"):
            print({"title": story["title"], "link": story["url"]})
        else:
            print("None")


if __name__ == "__main__":
    main()
