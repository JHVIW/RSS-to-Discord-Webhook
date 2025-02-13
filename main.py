import feedparser, requests, time, re
from html import unescape

FEED_URL = ""
WEBHOOK_URL = ""
CHECK_INTERVAL = 5

def clean_html(text):
    text = unescape(text)
    text = re.sub(r'<br\s*/?>', '\n', text)  
    text = re.sub(r'<ul.*?>', '', text)  
    text = re.sub(r'<li>', '• ', text)  
    text = re.sub(r'</li>', '', text)  
    text = re.sub(r'<.*?>', '', text)  
    return text.strip()

def extract_image(entry):
    if "enclosure" in entry and isinstance(entry.enclosure, dict):
        return entry.enclosure.get("url", None)
    
    match = re.search(r'<img src="(https://[^"]+)"', entry.get("description", ""))
    return match.group(1) if match else None

def format_description(description):
    description = clean_html(description)
    sections = re.split(r'\[ ([A-Z]+) \]', description)
    
    if len(sections) < 3:
        return description

    formatted_text = ""
    for i in range(1, len(sections), 2):
        section_title = sections[i].strip()
        section_content = sections[i + 1].strip()
        formatted_text += f"**{section_title}**\n{section_content}\n"

    return formatted_text.strip()

def send_to_discord(title, url, description, image_url=None):
    embed = {
        "title": title,
        "url": url,
        "description": format_description(description),
        "color": 7506394
    }
    if image_url:
        embed["image"] = {"url": image_url}
    
    payload = {"embeds": [embed]}
    requests.post(WEBHOOK_URL, json=payload)

def main():
    feed = feedparser.parse(FEED_URL)
    last_entry_id = feed.entries[0].get("id") or feed.entries[0].get("link") if feed.entries else None

    if feed.entries:
        latest_entry = feed.entries[0]
        image_url = extract_image(latest_entry)
        send_to_discord(latest_entry.get("title", "No title"), latest_entry.get("link", ""), latest_entry.get("description", ""), image_url)

    while True:
        feed = feedparser.parse(FEED_URL)
        
        if feed.entries:
            new_entries = []
            for entry in feed.entries:
                entry_id = entry.get("id") or entry.get("link")
                if last_entry_id and entry_id == last_entry_id:
                    break
                new_entries.append(entry)
            
            if new_entries:
                for entry in reversed(new_entries):
                    image_url = extract_image(entry)
                    send_to_discord(entry.get("title", "No title"), entry.get("link", ""), entry.get("description", ""), image_url)
                
                last_entry_id = feed.entries[0].get("id") or feed.entries[0].get("link")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
