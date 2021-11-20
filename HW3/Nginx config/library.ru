server {
	listen 80;

	server_name library.ru;

	location / {
		root /home/mary/Backend/HW3/public;
	}

	location ~ \.(gif|jpg|png)$ {
 		root /home/mary/Backend/HW3/public/images;

	}

	location ~ \.pdf$ {
                root /home/mary/Backend/HW3/public;
	}

	location ~ ^/api/ {
		proxy_pass http://127.0.0.1:8000;
	}
}
