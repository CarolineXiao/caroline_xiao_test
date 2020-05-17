from datetime import datetime, timedelta
import time

class LRUCache:

    class Item:
        def __init__(self, val, expires):
            self.val = val
            self.expires = expires

    class LinkedNode:
        def __init__(self, key, item):
            self.key = key
            self.item = item
            self.next = None


    # set the cache capacity
    def __init__(self, capacity, ttl=None):
        self.__size = capacity
        if ttl:
            self.__ttl = timedelta(seconds=ttl)
        else:
            self.__ttl = None
        dummy = self.LinkedNode(0, None)
        self.__head = dummy
        self.__tail = dummy
        self.__key2pre = {}

    # get the value of the key if the key exists, otherwise return -1
    def get(self, key):
        # find the key
        if key in self.__key2pre:
            now = datetime.now()
            expire_time = self.__key2pre[key].next.item.expires
            if expire_time and expire_time < now:
                self.__move_to_end(key, self.__key2pre[key].next.item)
                pre = self.__key2pre[key]
                node = pre.next
                self.__tail = pre
                self.__tail.next = None
                del self.__key2pre[node.key]
                return "Not Found"
            else:
                value = self.__key2pre[key].next.item.val
                expires = None
                if self.__ttl:
                    expires = datetime.now() + self.__ttl
                item = self.Item(value, expires)
                self.__move_to_end(key, item)
                return value
        else:
            return "Not Found"

    # set or insert value into cache
    def set(self, key, value):
        now = datetime.now()
        expires = None

        if self.__ttl:
            expires = now + self.__ttl
        item = self.Item(value, expires)

        if key not in self.__key2pre:
            node = self.LinkedNode(key, item)
            self.__tail.next = node
            self.__key2pre[key] = self.__tail
            self.__tail = node

            if len(self.__key2pre) > self.__size:
                head_node = self.__head.next
                self.__head.next = head_node.next
                if head_node.next != None:
                    self.__key2pre[head_node.next.key] = self.__head
                del self.__key2pre[head_node.key]
                head_node.next = None

        else:
            self.__move_to_end(key, item)

    def __move_to_end(self, key, item):
        prev = self.__key2pre[key]
        cur = prev.next
        cur.item = item

        if cur == self.__tail:
            return

        prev.next = cur.next
        if cur.next != None:
            self.__key2pre[cur.next.key] = prev
        self.__tail.next = cur
        self.__key2pre[key] = self.__tail
        self.__tail = cur
        cur.next = None

    def printCache(self):
        ptr = self.__head.next
        cache = []
        while ptr:
            cache.append(ptr.item.val)
            ptr = ptr.next
        print(cache)
