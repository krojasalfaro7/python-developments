from bs4 import BeautifulSoup
import requests
import datetime

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

BCV_URL = "https://www.bcv.org.ve/"

def fetch_website_data(url, verify_ssl=False):
    response = requests.get(url, verify=verify_ssl)
    if response.status_code == 200:
        return response.content
    return None
 
def get_bcv_usd_ves_rate_from_website_content(website_content):
    soup = BeautifulSoup(website_content, 'html.parser')
    component = soup.find('div', attrs={'id': 'dolar'})
    if component:
        content = component.find_all('strong')
        tag = content[0] if content else None
        rate_usd_ves_text = tag.text if tag else None
        rate_usd_ves_text_process = rate_usd_ves_text.replace(' ', '').replace(',', '.')
        return float(rate_usd_ves_text_process)

def get_datetime_rate_from_website_content(website_content):
    soup = BeautifulSoup(website_content, 'html.parser')

    component = soup.find('div', attrs={'class': 'pull-right dinpro center'})
    if not component:
        return None

    component2 = component.find('span', attrs={'class': 'date-display-single'})
    if not component2:
        return None
    
    date_html_value = component2.attrs.get("content", None)
    if not date_html_value:
        return None
    
    date = datetime.datetime.strptime(date_html_value, "%Y-%m-%dT%H:%M:%S%z")
    return date


def get_usd_ves_bcv_rate():
    # USD/VES Rate
    website_content = fetch_website_data(BCV_URL)
    if website_content:
        usd_ves_rate = get_bcv_usd_ves_rate_from_website_content(website_content)
        return usd_ves_rate
    return None

def get_datetime_bcv_rate():
    # USD/VES Rate
    website_content = fetch_website_data(BCV_URL)
    if website_content:
        datetime_rate = get_datetime_rate_from_website_content(website_content)
        return datetime_rate
    return None

# Client
current_usd_ves_bcv_rate = get_usd_ves_bcv_rate()
current_datetime_bcv_rate = get_datetime_bcv_rate()
print(f"USD/VES Rate: {current_usd_ves_bcv_rate}. Date: {current_datetime_bcv_rate}")