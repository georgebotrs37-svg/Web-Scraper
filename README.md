
🔍 Simple Web Page Data Extractor

A lightweight Python tool that extracts the page title and all links from a given URL using "requests" and "BeautifulSoup".

---

🚀 Features

- Fetches HTML content from any public URL
- Extracts:
  - 📌 Page title
  - 🔗 All hyperlinks ("<a href="">")
- Basic error handling for:
  - HTTP errors
  - Connection issues
  - Unexpected exceptions

---

🛠 Requirements

- Python 3.x
- requests
- beautifulsoup4

Install dependencies:

pip install requests beautifulsoup4

---

📂 Project Structure

.
├── main.py
└── README.md

---

▶️ Usage

Modify the URL inside the script:

url = 'http://example.com'

Then run:

python main.py

---

📌 Example Output

بيانات الصفحة:
العنوان: Example Domain
الروابط:
https://www.iana.org/domains/example

---

⚠️ Notes

- Make sure the target website allows scraping.
- Some websites may block automated requests.
- For large-scale scraping, consider:
  - Adding headers (User-Agent)
  - Using session handling
  - Implementing rate limiting

---

🔐 Disclaimer

This tool is intended for educational purposes only.
Always ensure you have permission before scraping any website.

---

💡 Future Improvements

- Export results to JSON or CSV
- Add command-line arguments support
- Implement concurrent requests
- Add proxy support
- Integrate logging system
- 
