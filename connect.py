import json
from sqlalchemy import create_engine


def task():
    with open('/home/deuex-solutions/Desktop/code/demo/config.json') as config:
        data = json.load(config)
    user = data["username"]
    password = data["password"]
    db = data["database"]
    port = data['host']


    engine = create_engine("mysql+pymysql://" + user + ":" + password + "@localhost:" + port + "/" + db + "?charset=utf8mb4")
