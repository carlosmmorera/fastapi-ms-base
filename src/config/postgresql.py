class ConfigPostgreSQL():
    url: str = ''
    db_name: str = ''
    user: str = ''
    pwd: str = ''
    host: str = ''
    port: int = 8080

    def __init__(self, url: str = '', db_name: str = '', user: str = '', pwd: str = '', 
                 host: str = '', port: int = 8080):
        self.url = url
        self.db_name = db_name
        self.user = user
        self.pwd = pwd
        self.host = host
        self.port = port