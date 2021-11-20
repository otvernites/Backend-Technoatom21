# NGINX

Run NGINX
```
sudo service nginx start
```
Stop NGINX
```
sudo service nginx stop
```
Reboot NGINX
```
sudo service nginx restart
```
Examples:
```
http://localhost/
http://library.ru/
http://library.ru/document.pdf
http://library.ru/cat.jpg
```
___

# GUNICORN

Run GUNICORN
```
gunicorn --workers 4 server:app
```
Stop GUNICORN
```
sudo fuser -k 8000/tcp 
```
Examples:
```
http://library.ru:8000
```
___

# Configuring proxying on GUNICORN

Examples:
```
http://library.ru/api/
http://localhost/api/hello/
```
___

# Site load measurement
## 5%-10% failed

Static test
```
wrk -t6 -c50000 -d3s --timeout 2s http://localhost/
```
Dynamic test
```
wrk -t6 -c5000 -d3s --timeout 2s http://localhost:8000/ 
```
Proxy test
```
wrk -t8 -c5000 -d8s --timeout 2s http://localhost/api/
```