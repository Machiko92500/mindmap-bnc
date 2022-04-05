## How to RUN the server 

* Run the script run.sh who will build and run the app 

```
    ./run.sh
```

* The app will be accessible through 127.0.0.1:5000

## How to run unit test 

For now, there is no unittest (let's discuss it during the interview)

* Run test (where there is no one for now) using this command :
```
    python -m tox
```

## Specifications

### Create a mind map

```bash
$ curl -X POST http://localhost:5000/create -H 'content-type: application/json' -d '{"id": "my-map"}'
```

### Add a leaf (path) to the map

```bash
$ curl -X POST  http://localhost:5000/add -H 'content-type: application/json' -d '{"path": "i/like/potatoes", "text": "Yumi"}'
```

### Read a leaf (path) of the map

```bash
curl -X GET http://localhost:5000/read -H 'content-type: application/json'
```

### Pretty print the whole tree of the mind map

```bash
$ curl -X GET http://localhost:5000/pretty -H 'content-type: application/json'
```