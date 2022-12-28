from kafka import KafkaProducer   
import sys       
from data import get_page, scrape_daily_search


BROKER = 'localhost:9092' 
TOPIC = 'trends' 

try:                                                                                                                    
    producer = KafkaProducer(bootstrap_servers=BROKER)                                                                         
except Exception as e:                                                                                                  
    print(f"ERROR --> {e}")                                                                                             
    sys.exit(1)                                                                                                        
    

def main():
	GEO = "TR"
	URL = f"https://trends.google.com/trends/trendingsearches/daily?geo={GEO}"
	result = get_page(URL)
	json_data = scrape_daily_search(result)
	return json_data

while True:
	data = main()
	producer.send(TOPIC, data.encode("utf-8"))
	producer.flush()
	print("Done Sending......")
    
