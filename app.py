import requests
from bs4 import BeautifulSoup

# URL = "https://www.amazon.com/Seagate-BarraCuda-Internal-2-5-Inch-ST5000LM000/dp/B01M0AADIX/ref=sr_1_3?qid=1562249332&s=gateway&sr=8-3"
URL = "https://www.amazon.de/Tamron-A036SF-28-75-RXD-Autofokus-Videoaufnahmen/dp/B07CSXTGJJ/ref=pd_sbs_421_4/259-6327764-8346542?_encoding=UTF8&pd_rd_i=B07CSXTGJJ&pd_rd_r=a9c69fbd-9e66-11e9-923c-6fe6f43132ff&pd_rd_w=JMIfY&pd_rd_wg=xZXfy&pf_rd_p=74d946ea-18de-4443-bed6-d8837f922070&pf_rd_r=GVKM8FYTPE89JDK6WGSM&psc=1&refRID=GVKM8FYTPE89JDK6WGSM"
# URL = "https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7&qid=1561393494&s=gateway&sr=8-3"

headers = { "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' }

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()

print(title.strip())
