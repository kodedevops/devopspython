# Project Setup

```
python3 -m venv venv
source venv/bin/activate

-- Approach1
touch requirements.txt
Flask>=3.0.0
pip install -r requirements.txt
pip list

-- Approach2
pip install Flask
pip freeze > requirements.txt
pip list

```

### DOCKER

```
-- while checking locally
docker build -t devopspython .
docker run -p 5000:5000 devopspython



-- whileing pushing to dockerhub
docker login
docker buildx create --use
docker buildx inspect --bootstrap

docker buildx build --platform linux/amd64,linux/arm64 -t santoshmondal/devopspython:latest --push .
docker buildx build --platform linux/amd64,linux/arm64 -t santoshmondal/devopspython:1.0.0 --push .

docker run -p 5000:5000 santoshmondal/devopspython

```
