import requests
from bs4 import BeautifulSoup

def extract_page_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "لا يوجد عنوان"
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return {
            'title': title,
            'links': links
        }
    except requests.RequestException as e:
        print(f"خطأ في طلب HTTP: {e}")
        return None
    except Exception as e:
        print(f"خطأ غير معروف: {e}")
        return None

url = 'http://example.com'
page_data = extract_page_data(url)
if page_data:
    print("بيانات الصفحة:")
    print(f"العنوان: {page_data['title']}")
    print("الروابط:")
    for link in page_data['links']:
        print(link)