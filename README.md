# 🛒 **Product Info Scraper**

![GitHub contributors](https://img.shields.io/github/contributors/abu14/Web-Scraping-Walmart)
![GitHub forks](https://img.shields.io/github/forks/abu14/Web-Scraping-Walmart?style=social)
![GitHub stars](https://img.shields.io/github/stars/abu14/Web-Scraping-Walmart?style=social)
![GitHub issues](https://img.shields.io/github/issues/abu14/Web-Scraping-Walmart)
![GitHub license](https://img.shields.io/github/license/abu14/Web-Scraping-Walmart)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/abenezer-tesfaye-191579214/)

This Python script is designed to efficiently scrape product information from **Walmart's** website using the ***BeautifulSoup and Requests*** libraries. It automates the process of collecting data on various products based on from a list of search queries, such as ***"gaming monitor," "laptop," and "smartphone."*** The script sends **HTTP requests** to Walmart to retrieve HTML content and then parses this content to extract relevant product links. For each product, it gathers detailed information, including price, review count, average rating, product name, brand, availability status, and a thumbnail image URL. All extracted data is saved in a JSON Lines format, allowing for easy storage and processing. This approach not only streamlines data collection but also ensures that users can access up-to-date product information efficiently. If need be it's also possible to store the final output on to a database. 

> Also, for large-scale scraping projects, it might be necessary to use other tools such as **Bright Data**. Since websites like Walmart will likely block you when you make too many requests from the same IP, tools like **Bright Data** provide proxies to mask your location. 


### ✨ **Features** 
  * Scrapes Product Links
  * Extracts Product Info
  * Handles Multiple Pages
  * Save Output


### 📦 **Requirements**
  * Python --> 3.12.3
  * Beautifulsoup4 --? 4.13.3
  * Requests --> 2.32.3



### ⚙️ **Usage**


1. Clone the repo:
   ```bash 
    git clone https://github.com/abu14/Web-Scraping-Walmart.git
    cd Web-Scraping-Walmart
   ```

2. Install dependencies:
   ```bash
    pip install beautifulsoup4 requests
   ```

3. Run the script:
   ```bash
    python walmart-scraper.py
   ```


### 📝 **License**

This project is licensed under the MIT License.  See [LICENSE](./LICENSE) file for more details.


<!-- CONTACT -->
### **Contact**

##### Abenezer Tesfaye

⭐️ Email - tesfayeabenezer64@gmail.com
 
Project Link: [Github Repo](https://github.com/abu14/Web-Scraping-Walmart)

