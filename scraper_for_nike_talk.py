import requests
import logging
from bs4 import BeautifulSoup
from botUtils import parse_number_with_suffix

def scrape_nike_talk_page(url, order_list):
    
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all the elements containing forum topics
        topics = soup.find_all('div', class_='structItem')
        
        for element in topics:
            # Find the <div> element containing the topic title
            title_div = element.find('div', class_='structItem-title')

            # Check if title_div exists
            if title_div:
                # Find the <a> element within the title <div>
                title_element = title_div.find('a')
                
                # Check if title_element exists
                if title_element:
                    # Extract the text content (topic title)
                    topic_title = title_element.text.strip()
                    
                    # Find the <dl> element containing the views
                    views_dl = element.find('dl', class_='pairs pairs--justified structItem-minor')
                    
                    # Check if views_dl exists
                    if views_dl:
                        # Find the <dd> element within views_dl
                        views_dd = views_dl.find('dd')
                        
                        # Check if views_dd exists
                        if views_dd:
                            # Extract the text content (number of views)
                            views = views_dd.text.strip()
                            int_views = parse_number_with_suffix(views)
                            instanceDict = {int_views : topic_title}
                            order_list.append(instanceDict)
                        else:
                            logging.debug("No <dd> element found within the views <dl>")
                    else:
                        logging.debug("No views <dl> found for the topic")
                else:
                    logging.debug("No <a> element found within the title <div>")
            else:
                logging.debug("No title <div> found for the topic")
        return order_list    
    else:
        logging.debug("Failed to retrieve the webpage")
        return None