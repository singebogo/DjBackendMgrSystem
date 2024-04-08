# -*-coding:utf-8-*-
'''
    
'''
# 这使用直写式缓存——每次写入缓存的数据也会被写入到数据库。如果数据不在缓存中，会话仅使用数据库进行读取。
# 为了持久化缓存数据，设置 SESSION_ENGINE 为 "django.contrib.sessions.backends.cached_db"
# 在大部分情况下，cached_db 后端将足够快，但如果你需要最后一点的性能，并且愿意不时地删除会话数据，那么 cache 后端适合你。
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"