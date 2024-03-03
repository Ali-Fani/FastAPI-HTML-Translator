## An api writen in fastapi that gets html and targeted language and translates its content and returns an html file

## Usage:
- copy the .env.example file to .env
- add apikey to .env file
- build the docker image `docker build -t fastapi-translator .`
- run the docker container `docker run -p 8000:8000 fastapi-translator`

## Endpoints:
`/docs` - fastapi documentation

`/translate` - post request with html and targeted language as json body