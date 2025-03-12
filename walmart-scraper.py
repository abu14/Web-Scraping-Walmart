from bs4 import BeautifulSoup # BeautifulSoup is a Python library for pulling data out of HTML and XML files.
import requests #Requests allows to send HTTP requests using Python.
import json #storing and exchanging json data
import queue #A queue is a data structure that stores items in First In First Out (FIFO) order.

# Base URL for the Walmart website and output file name
Base_Url = 'https://www.walmart.com'
Output_File = 'product_info_v2.jsonl' 


#Broser headers to mask the request as a browser request
HEADERS = {
"accept": "*/*",
"accept-encoding": "gzip, deflate, br, zstd",
"accept-language": "en-US,en;q=0.9",
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'
    }


# List of search queries
search_queries = ["gaming monitor", "laptop", "tv", "smartphone", "headphones", "camera", "smartwatch", "printer", "tablet", "keyboard"]

#queue for prouct URLs and a set of for seen URLs
product_queue = queue.Queue() #A que object
seen_urls = set() #a set object is an unordered collection of distinct hashable objects.


# Function to get the product links per each search query/ product
def get_product_links(search_query, page_number=1):
    url = f"https://www.walmart.com/search?q={search_query}&page={page_number}"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    #links = soup.find_all('a', href=True)
    product_links = []
    found = False 
    for a_tag in soup.find_all('a', href=True):
        if "/ip/" in a_tag['href']:
            found = True    
            if "https" in a_tag['href']:
                full_link = a_tag['href']
            else:
                full_link = Base_Url + a_tag['href']
            if full_link not in seen_urls:
                product_links.append(full_link)
    if not found:
        print("\n\n\nSoup Without Product Links\n\n\n",soup)
    return product_links




def extract_product_info(product_url):
    print("Processing link", product_url)
    response = requests.get(product_url, headers=HEADERS)

    soup = BeautifulSoup(response.text, 'html.parser')

    script_tage = soup.find('script', id="__NEXT_DATA__")
    if script_tage is None:
        return None
    
    data = json.loads(script_tage.string)
    initial_data = data['props']['pageProps']['initialData']['data']
    product_data = initial_data["product"]
    reviews_data = initial_data.get("reviews", {})


    product_info = {
        "price": product_data["priceInfo"]["currentPrice"]["price"],
                    "review_count": reviews_data.get("totalReviewCount", 0),
                    "item_id": product_data["usItemId"],
                    "avg_rating": reviews_data.get("averageOverallRating", 0),
                    "product_name": product_data["name"],
                    "brand": product_data.get("brand", ""),
                    "availability": product_data["availabilityStatus"],
                    "image_url": product_data["imageInfo"]["thumbnailUrl"],
                    "short_description": product_data.get("shortDescription", "")
                }
    return product_info



def main():
    with open(Output_File, 'w') as file:
        while search_queries:
            current_query = search_queries.pop(0)
            print('\n\nCurrent_Query: ',current_query, "\n\n")
            page_number = 1

            while True:
                product_links = get_product_links(current_query, page_number)
                if not product_links or page_number > 10:  # page limit can be higher, for now we are limiting to 10 pages.
                    break
                
                for link in product_links:
                    if link not in seen_urls:
                        product_queue.put(link)
                        seen_urls.add(link)

                while not product_queue.empty():
                    link = product_queue.get()
                    try:
                        product_info = extract_product_info(link)
                        if product_info:
                            file.write(json.dumps(product_info) + '\n')
                    except Exception as e:
                        print(f"Failed to process link{link}, {e}")
                page_number += 1
                print("Search page number", page_number)


if __name__ == "__main__":
    main()