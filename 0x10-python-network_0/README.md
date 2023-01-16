
# Python - Network #0

Python scripts interpretted on [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) using [Python 3.4.3](https://www.python.org/downloads/release/python-343/) and must conform to [PEP 8 (v1.7.x)](https://pep8.readthedocs.io/en/release-1.7.x/intro.html) style.

### Focus
Learn how to use `curl` to make a HTTP `GET` and `POST` request, as well as how to read the HTTP response. An algorithm to find the peak among a list of integers was also included in the project.

### Example Usages

[0-body_size.sh](0-body_size.sh)
```
0x10-python-network_0:$  ./0-body_size.sh 0.0.0.0:5000
10
0x10-python-network_0:$  
```
[1-body.sh](1-body.sh)
```
0x10-python-network_0:$  ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
0x10-python-network_0:$  
```
[2-delete.sh](2-delete.sh)
```
0x10-python-network_0:$  ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
0x10-python-network_0:$  
```
[3-methods.sh](3-methods.sh)
```
0x10-python-network_0:$  ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
0x10-python-network_0:$  
```
[4-header.sh](4-header.sh)
```
0x10-python-network_0:$  ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
0x10-python-network_0:$  
```
[5-post_params.sh](5-post_params.sh)
```
0x10-python-network_0:$  ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: hr@holbertonschool.com
    subject: I will always be here for PLD
0x10-python-network_0:$ 
```
[6-peak.py](6-peak.py)
```
0x10-python-network_0:$  cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 3, 1]))

0x10-python-network_0:$  ./6-main.py
6
3
2
None
2
4
0x10-python-network_0:$  wc -l 6-peak.txt 
2 6-peak.txt
0x10-python-network_0:$  
```
[100-status_code.sh](100-status_code.sh)
```
0x10-python-network_0:$  ./100-status_code.sh 0.0.0.0:5000 ; echo ""
200
0x10-python-network_0:$  
0x10-python-network_0:$  ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
404
0x10-python-network_0:$  
```
[101-post_json.sh](101-post_json.sh)
```
0x10-python-network_0:$  cat my_json_2
{
    "name": "John Doe",
    "age": 33,
}
0x10-python-network_0:$  ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
Not a valid JSON
0x10-python-network_0:$  
```
[102-catch_me.sh](102-catch_me.sh)
```
0x10-python-network_0:$  ./102-catch_me.sh ; echo ""
You got me!
0x10-python-network_0:$  
```
### Author
- [Alex Yu](https://github.com/AlexYu01)
### Acknowledgments
- [Holberton](https://www.holbertonschool.com/)
