# printer-status-py

Display Printer Status (Flask app)  

- display residual ink quantity
- send residual ink quantity mail using Gmail API and Windows Task Scheduler
- enable Apache2.4 hosting (See: Apache_conf/httpd_vhosts.conf) 

Ruby + Sinatra version:  
[thinkAmi/PrinterStatus: Display printer status and mail](https://github.com/thinkAmi/PrinterStatus)

　  
## Getting Started

```
>cd path\to\dir

path\to\dir>git clone https://github.com/thinkAmi/printer-status-py.git

path\to\dir>virtualenv -p c:\python35-32\python.exe env
path\to\dir>env\Scripts\activate

(env)path\to\dir>pip install -r requirements.txt

(env)path\to\dir>python main.py
```

if you want to use Apache hosting, add `mod_wsgi` module and append `httpd-vhosts.conf` file.

　  
## Tested environment

- Windows10 x64
- Python 3.5.1 32bit
- Flask 0.11
- google-api-python-client 1.5.1
- PySNMP 4.3.2
- Highcharts
- Apache 2.4.10
- mod_wsgi 4.5.2

　  
## License
MIT

　  
## Related Blog posts (written in Japanese)

[Python3 + Flask + PySNMP + Highcharts + Apache2.4で、PX-105のインク残量を取得・表示し、Gmailでインク残量を送信する - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/06/14/233606)