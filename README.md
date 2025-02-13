# RSS to Discord Webhook

This script fetches an RSS feed and automatically sends new updates to a Discord webhook in an embedded message. It supports extracting and formatting descriptions as well as retrieving images from the feed.

## ⚙️ Features
- ✅ Periodically checks an RSS feed for new entries  
- ✅ Automatically sends new entries to a Discord webhook  
- ✅ Cleans and formats descriptions for better readability  
- ✅ Extracts images from the feed and includes them in the embed  

## 📅 Installation  
### **1. Install dependencies:**  
Ensure you have Python installed and install the required packages:
```bash
pip install feedparser requests
```
### **2. Configure the script:**  
- Set your RSS feed URL in `FEED_URL`  
- Add your Discord webhook URL in `WEBHOOK_URL`  
- Adjust the check interval if needed (`CHECK_INTERVAL` in seconds)  

### **3. Run the script:**  
```bash
python script.py
```

## ⚙️ Configuration  
Customizable variables in the script:
```python
FEED_URL = "https://example.com/rss"
WEBHOOK_URL = "https://discord.com/api/webhooks/..."
CHECK_INTERVAL = 5  # Interval in seconds
```

## 📝 How It Works
1. The script reads the RSS feed and stores the last processed entry.  
2. Every few seconds, it checks for new entries.  
3. If a new entry is found:
   - It extracts the title, link, and description.  
   - The description is cleaned and formatted.  
   - Any images from the entry are retrieved and added to the embed.  
   - The message is sent to Discord via the webhook.  

## 🔗 Example Discord Embed
Here’s how a generated message looks in Discord:

**[Post Title](https://example.com/article)**  
*Description of the post...*  

![Example](https://via.placeholder.com/400x200.png?text=Image+Preview)

## 🤝 Contributing  
Feel free to suggest improvements or new features via pull requests or issues! 🚀  

---

