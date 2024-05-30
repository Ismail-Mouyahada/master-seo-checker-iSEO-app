from time import time

RATE_LIMIT = 5  # 5 seconds between requests
last_request_time = 0

def check_rate_limit():
    global last_request_time
    current_time = time()
    if current_time - last_request_time < RATE_LIMIT:
        return False
    last_request_time = current_time
    return True
