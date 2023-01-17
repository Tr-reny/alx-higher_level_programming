# Python - Network #1

Python scripts interpretted on [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) using [Python 3.4.3](https://www.python.org/downloads/release/python-343/) and must conform to [PEP 8 (v1.7.x)](https://pep8.readthedocs.io/en/release-1.7.x/intro.html) style.

### Focus
Learn how to fetch internet resources with the Python `urllib` and `Request` library. How to decode the responses in order to manipulate the data.

### Example Usages

[0-hbtn_status.py](0-hbtn_status.py)
```
0x11-python-network_1:$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
0x11-python-network_1:$ 
```
[1-hbtn_header.py](1-hbtn_header.py)
```
0x11-python-network_1:$ ./1-hbtn_header.py https://intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
0x11-python-network_1:$ 
0x11-python-network_1:$ ./1-hbtn_header.py https://intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
0x11-python-network_1:$ 
```
[2-post_email.py](2-post_email.py)
```
0x11-python-network_1:$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
0x11-python-network_1:$
```
[3-error_code.py](3-error_code.py)
```
0x11-python-network_1:$ ./3-error_code.py http://0.0.0.0:5000
Index
0x11-python-network_1:$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
0x11-python-network_1:$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
0x11-python-network_1:$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
0x11-python-network_1:$ 
```
[4-hbtn_status.py](4-hbtn_status.py)
```
0x11-python-network_1:$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
0x11-python-network_1:$ 
```
[5-hbtn_header.py](5-hbtn_header.py)
```
0x11-python-network_1:$ ./5-hbtn_header.py https://intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
0x11-python-network_1:$ 
0x11-python-network_1:$ ./5-hbtn_header.py https://intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
0x11-python-network_1:$ 
```
[6-post_email.py](6-post_email.py)
```
0x11-python-network_1:$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
0x11-python-network_1:$ 
```
[7-error_code.py](7-error_code.py)
```
0x11-python-network_1:$ ./7-error_code.py http://0.0.0.0:5000
Index
0x11-python-network_1:$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
0x11-python-network_1:$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
0x11-python-network_1:$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
0x11-python-network_1:$ 
```
### Author
- [Alex Yu](https://github.com/AlexYu01)
### Acknowledgments
- [Holberton](https://www.holbertonschool.com/)
