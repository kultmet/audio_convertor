# audio_convertor
## This servise converts wave-audio to mp3-audio

Hi, my friend!!!!

## How to start? 
### "Like This" - © Alexander Nevsky

Clone project from GitHub
```
git clone https://github.com/kultmet/audio_convertor.git
```

Create .env file and fill enviroments

```
# to terminal

touch .env
echo "DB_NAME=postgres" >> .env
echo "DB_USER=postgres" >> .env
echo "DB_USER=postgres" >> .env
echo "DB_PASSWORD=password" >> .env
echo "DB_HOST=localhost" >> .env
echo "DB_PORT=5432" >> .env
echo "FFMPEG_PATH=/usr/bin/ffmpeg" >> .env

# and push ENTER
```

Deploying the project with <code>docker-compose</code>

```
docker-compose up -d
```
## Query examples:

Test the service <a href="http://localhost/docs">here</a>

Servise has the ability to make requests to endpoints:

<code>/users/</code>
    methods:
        POST - Creates user.
            request:
                body:
                    username
            response:
                status_code: 201
                body:
                    {
                      id,
                      token
                    }

```
# request example
/users/ 
{
  "username": "vasia"
}
```

```
# response example

{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "token": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```



<code>/audio/</code>
    methods:
        POST - Creates audio.
            request:
                parameters:
                    user_id
                    user_token
                body:
                    wav_file
            response:
                status_code: 201
                body: 
                    url (string)

```
# request example
curl -X 'POST' \
  'http://localhost/audio/?user_id=4d391741-1db7-4ff5-952b-70e50226e7a6&user_token=f99f4826-8bf0-44bf-b386-aaffc10058a1' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'wav_file=@sample-6s.wav;type=audio/wav'

```

```
# response example
"http://localhost/record?id=9a238062-86c6-4603-87e8-c0a7548d20a1&user=4d391741-1db7-4ff5-952b-70e50226e7a6"
```

<code>/record</code>
    methods:
        GET - Download mp3-audio file.
            request:
                parameters:
                    id (audio id)
                    user (user id)   
            response:
                status_code: 200
                body:
                    MP3-audio file
    
```
# request example

http://localhost/record?id=9a238062-86c6-4603-87e8-c0a7548d20a1&user=4d391741-1db7-4ff5-952b-70e50226e7a6
```

```
# response example

MP3-audio file
```

## Development plan

Write tests

# Thanks for viewing