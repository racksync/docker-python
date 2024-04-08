# python-docker

### Local development environment for Python using Docker.

1. Prerequisites
```
sudo python3 -m pip install Flask
```
or 
```
sudo python3 -m pip install -r requirements.txt
```

2. Run the application
```
python3 app.py
```

### Dockerize

1. Build the image
```
docker build -t python-docker .
```

2. Run the container
```
docker run -d --name --restart unless-stopped python-app -p 8080:8080 python-docker
```

3. Access the application
```
http://localhost:8080/quote
```

4. Push Docker Image
```
```