## Project Structure:

```
flask-template
│   .gitignore
│   app.py
│   gunicorn.conf.py
│   README.md
│   start.sh
│   
├───src
│   └───api
│       ├───models
│       │       __init__.py
│       │       
│       ├───routes
│       │   │   ping.py
│       │       __init__.py
│       │  
│       └───schemas
│               __init__.py
│               
├───test
│   │   test_ping_api.py
```