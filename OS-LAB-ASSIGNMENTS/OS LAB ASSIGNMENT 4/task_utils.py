
import time
import logging

def process_task(name):
    logger = logging.getLogger()
    # Configure logger inside process if not inheriting (safety check)
    if not logger.handlers:
        logging.basicConfig(filename='system_log.txt', level=logging.INFO,
                            format='%(asctime)s - %(processName)s - %(message)s')
    
    logger.info(f"{name} started")
    # Simulate work
    time.sleep(1) 
    logger.info(f"{name} terminated")
