# How to run
### For QuestionA and QuestionB 
I wrote input test files for them. You can add new tests and run
```
python3 QuestionA.py
python3 QuestionB.py
```
Then the test results will be printed out.
- Example:
```
test1: (1.0, 5.0) (2.0, 6.0) - True
test2: (1.0, 5.0) (6.0, 8.0) - False
test3: (2.0, 7.1) (6.65, 9.0) - True
test4: (-3.0, 0.0) (-18.0, 16.0) - True
test5: (2.0, 10.0) (88.0, 15.0) - False
test6: (2.0, 8.0) (11.0, 7.0) - True
test7: (6.0, 14.0) (14.0, 47.0) - True
test8: (1.0, 5.0) (0.3, 5.0) - True
test9: (2.0, 2.0) (1.0, 10.0) - True
test10: (8.6, 8.6) (8.6, 8.6) - True
test11: The number of variable is not correct
test12: (0.0, 0.0) (2.0, 1.0) - False
test13: The number of variable is not correct
test14: The number of variable is not correct
test15: (99.0, 2.0) (-6.0, 1.0) - False
test16: Input should be integers
test17: (-18.2, 2238.0) (12.0, -76.0) - True
```

### For QuestionC
1. Start the server
 ```
python3 central_server.py
 ```
2. Enter capacity(integer) and ttl(optional) follow the instruction
- Example:
```
Please enter the cache capacity: 3
Please enter the ttl in seconds (default = None): 5
```
3. Start the client
 ```
python3 client.py
 ```
4. Enter any key string that you want to send to the server
 - Example:
 ```
 Enter request key: 2
 ```
5. The the value returned by server will be printed for client and on server side you can also see the current cache each time client send a request.
- Example:
```
# client
 [x] Requesting 2
 [.] Got '88'
 [x] Requesting 3
 [.] Got '21'

# server
 [.] 2
Current cache: [88]
 [.] 3
Current cache: [88, 21]
```
