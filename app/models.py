from flask import Flask, request, jsonify
from app.db import Mydb, Userdb
import uuid

db = Mydb()

class Request:
    def __init__(self, _id, requesttype, category, details):
        self._id = _id
        self.requesttype = requesttype
        self.category = category
        self.details = details

    def get_Id(self):
        return self._id

    def get_requesttype(self):
        return self.requesttype

    def get_category(self):
        return self.category

    def get_details(self):
        return self.details
    
    def get_db():
        return self.db

    def create_request(self, requestid, requesttype, category, details):
        _request = {
            'requestid': requestid,
            'requesttype': requesttype,
            'category': category,
            'details': details
        }

        db.add_request(_request['requestid'], _request['requesttype'], _request['category'], _request['details'])

        return Mydb.get_single_request(requestid)

    def fetch_all_requests(self):
        All_requests = []
        for _request in db.get_all_requests():
            All_requests.append(_request)
            
        return Allrequests

    def fetch_request_by_id(self, requestid):
        _request = db.get_single_request(requestid)
        req_dict = {}
        req_dict['req_id'] = _request[0]
        req_dict['requesttype'] = _request[1]
        req_dict['category'] = _request[2]

        return req_dict

    def change_request(self, requestid, requesttype, category, details):
        _request = {
            'id': requestid,
            'requesttype': requesttype,
            'category': category,
            'details': details
        }
        db.modify_request(_request['id'], _request['requesttype'], _request['category'], _request['details'])

        return db.get_single_request(_request['id'])

class User:
    def __init__(self, email, createPassword, confirmPassword):
        self.email = email
        self.createPassword = createPassword
        self.confirmPassword = confirmPassword
        self.db = Userdb()
    
    def get_email(self):
        return self.email

    def get_createPassword(self):
        return self.createPassword
    
    def get_confirmPassword(self):
        return self.confirmPassword
    
    def get_db():
        return self.db
    
    def add_user_table(self):
        return db.create_user_table()

    def create_user(self, email, confirmPassword):
        user_id = uuid.uuid1()
        User = {
            'userid': str(user_id),
            'email': email,
            'password': confirmPassword 
        }
        return self.db.add_user(user_id, email, confirmPassword)