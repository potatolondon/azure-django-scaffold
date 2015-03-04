import redis


print "Enter Redis host: ",
redis_host = raw_input()

print "Enter Redis Password: ",
redis_pw = raw_input()

print "Enter Redis DB: ",
redis_db = raw_input()


r = redis.StrictRedis(host=redis_host, port=6379, db=redis_db, password=redis_pw)
r.flushdb()
