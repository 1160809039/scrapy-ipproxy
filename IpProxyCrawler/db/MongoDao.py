#!/usr/bin/python

# @File : MongoDao.py
# @Author: 邵泽铭
# @Date : 10/10/18
# @Desc :


from db.MongoConnect import mongo



class MongoDao:
    @staticmethod
    def selectAll():
        return mongo.find()

    @staticmethod
    def selectByIp(ip,port,httpType):
        return mongo.find({"ip":ip,"port":port,"httpType":httpType})

    @staticmethod
    def insert(ipproxy):
        return mongo.insert_one(ipproxy)

    @staticmethod
    def delete(ip,port,httpType):
        return mongo.delete_many({"ip":ip,"port":port,"httpType":httpType})

    @staticmethod
    def deleteById(id):
        return mongo.delete_many({"_id": id})

    @staticmethod
    def selectByName(spiderName):
        return mongo.find({"spider":spiderName})