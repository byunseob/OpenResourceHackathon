[![Run on Ainize](https://ainize.ai/static/images/run_on_ainize_button.svg)](http://34.67.222.84/locust/form)

##locust helper

## Docker build
```
docker build -t byunseob/locust_helper3 .
```
## Docker run
```
docker run -p 80:80 -p8089:8089 -d byunseob/locust_helper3
```

## locust  초기화 API 호출
```
    curl --location --request POST "HOST/locust" \
      --header "Content-Type: application/json" \
      --data "{
        \"method\":\"get\",
        \"host\":\"http://www.mocky.io/v2/5deae5e13000006f6b2b0b27\",
        \"params\": {
            \"name\": \"byunseob\"
        }
    }"
```


## locust form 
```
    http://HOST/locust/form?host=HOST
```


