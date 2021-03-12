import redis
import time

redis_host = "localhost"
redis_port = 6379
redis_password = ""

def hello_redis():
    """Example Hello Redis Program"""
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        r.set('ip_address', '0.0.0.0')
        r.set('timestamp', int(time.time()))
        r.set('user_agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)')
        r.set('last_page_visited1', 'account')
        r.set('last_page_visited', 'account', 86400)
    except Exception as e:
        print(e)
if __name__ == "__main__":
    hello_redis()