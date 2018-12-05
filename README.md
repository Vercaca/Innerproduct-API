# Innerproduct-API
Inner Product API with Http request
- Client: POST vector x and y
- Admin: GET statistics of responses

## Prequisites

- flask=='0.11.1'



## Testing
### Step 1: Open API
```
python index.py
```

### [Client] Test Clients (with 5 correct responses and 1 wrong response)
```
python test_clients.py
```

### [Admin] Check States (with 5 correct responses and 1 wrong response)
```
http://127.0.0.1:5000/info/
```
