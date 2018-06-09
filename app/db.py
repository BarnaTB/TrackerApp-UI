import psycopg2


class Mydb:
    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname='tracker_db' user='user_1' password='database' host='localhost' port='5432'")
        self.cur = self.conn.cursor()

    def close_conn(self):
        self.cur.close()

    def get_dbname(self):
        return self.dbname

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_conn(self):
        return self.conn

    def create_request_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS requests (id INT, requesttype TEXT, category TEXT, details TEXT);")

    def add_request(self, id, requesttype, category, details):
        self.cur.execute("INSERT INTO requests (requesttype, category, details) VALUES ({}, {}, {});",
                         (requesttype, category, details))
        self.close_conn()

    def get_all_requests(self):
        self.connect()
        self.cur.execute("SELECT * FROM requests")
        _requests = self.cur.fetchall()
        self.close_conn()
        return _requests

    def get_single_request(self, requestid):
        self.cur.execute(
            "SELECT * FROM requests WHERE  id = {};".format(requestid))
        request = self.cur.fetchone()
        self.close_conn()
        return request

    def modify_request(self, requestid, requesttype, category, details):
        self.requestid = requestid
        self.requesttype = requesttype
        self.category = category
        self.details = details
        # self.cur.execute("SELECT * FROM requests WHERE id = {};".format(requestid))
        self.cur.execute("UPDATE requests SET requesttype = {} category = {}, details = {} WHERE id == {};".format(
            self.requestype, self.category, self.details, self.requestid))
        self.close_conn()


class Userdb:
    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname='tracker_db' user='user_1' password='database' host='localhost' port='5432'")
        self.cur = self.conn.cursor()

    def close_conn(self):
        self.cur.close()

    def create_user_table(self):
        # self.connect()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS users (user_id INT, email TEXT, password TEXT);")
        self.close_conn()

    def add_user(self, user_id, email, confirmPassword):
        # self.create_user_table()
        # self.connect()
        self.cur.execute("INSERT INTO users(userid, email, Password) VALUES ({}, {}, {});".format(
            user_id, email, confirmPassword))
        self.close_conn()
