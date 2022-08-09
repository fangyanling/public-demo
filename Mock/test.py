import json

import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/v1/auth/admin/token',methods=['post','get'])
def get_token():
    print('请求方法：',request.method)
    if request.method == 'POST':
        username = request.get_json()['username']
        password = request.get_json()['password']
        if username == '15602384112' and password == 'test12345!':
            return jsonify({
                        "code": 0,
                            "info": "ok",
                           "data": {
                            "token": "eyJhbGciOiJzaGEyNTYiLCJ0eXAiOiJKV1QifQ.W3sibmJmIjoxNjQ5NDEwMTU0LCJpc3MiOiJkb2YiLCJ0emEiOiJDU1QiLCJleHAiOjE2NDk0OTY1NTQsImlhdCI6MTY0OTQxMDE1NCwic2lkIjoxfSx7InJhbmQiOiIxNjU4NjU5MjAwMzcwODMzMDczMTkzNDcyMTkxNTgyMDE4OTE1NjcxMDYzOTk1OTg1NTM1MjcwNzk3MDU5Nzc0IiwidWlkIjo2NjA1NTYsInR5cCI6ImEiLCJ0aW1lIjoxNjQ5NDEwMTU0fV0.MjgyNzdlYTgzYmQ1M2Y1ZjM1MTY4OTJmOGU5MzkzMjdhODQzODU1MzU2ZmM1OTM0Y2Y2ODAyYzdhNGNmNDc4MQ",
                                "uid": 660556,
                                   "needChangePwd": 'false'
                                  },
                                      "more": 'null'
            })
        else :
            return jsonify({
                "code":101,
                "msg":"用户名或密码错误"
            })
    else :
        return jsonify({
            "code":201,
            "msg":"请使用post请求"
        })

    


@app.route('/complex/v1/ol-dictionary/find',methods=['post','get'])
def find():
    print("请求方法",request.method)
    if request.method == 'GET':
        key = request.args.get('key')
        if key == 'courseType':
           return jsonify({"code":0,"message":"操作成功","data":[{"level":0,"name":"入门课","type":1,"value":"47,0","key":"courseType_rmk"},{"level":0,"name":"系统课","type":1,"value":"61,1","key":"courseType_xtk"},{"level":1,"name":"特训课","childDic":[{"level":0,"name":"闯关特训营","type":1,"value":"81,1","key":"courseType_txk_txy"},{"level":0,"name":"考级特训营","type":1,"value":"82,2","key":"courseType_txk_kj"},{"level":0,"name":"闯关练习","type":1,"value":"83,4","key":"courseType_txk_lx"},{"level":0,"name":"竞赛特训营","type":1,"value":"84,3","key":"courseType_txk_js"}],"type":2,"value":"67,3","key":"courseType_txk"}]})
        else:
            return jsonify({
            "code": 202,
            "msg": "传参请带key=courseType"
        })
    else:
        return jsonify({
            "code": 201,
            "msg": "请使用get请求"
        })


@app.route('/v1/web/course/schedule',methods=['post','get'])
def scheduler():
    print("请求方法", request.method)
    if request.method == 'GET':
        return jsonify({"message": "OK","msg": "success","success": 'true',"traceId": "ac16008d16506108747183239d0001"})
    else:
        return jsonify({
            "code": 201,
            "msg": "请使用get请求"
        })


@app.route('/v1/web/class/getMgrList',methods=['post','get'])
def getMgrList():
    if request.method == 'POST':
        currentPage = request.json.get('currentPage')
        if currentPage >= 1:
           payload = {"currentPage":1,"total":1029,"pageSize":10,"missClassRange":'',"allotStatus":"","adminUserIdList":[],"departIdList":[]}
           response = {"code":0,"data":{"current":1,"pageSize":10,"total":1029,"totalPage":103,"records":[{"id":14546,"className":"L1_21122001_S4/S5_1班","courseId":1655,"childType":0,"pid":1357,"parentCourseName":"图形化编程","courseName":"L1","sectionId":29079,"sectionName":"第1讲_餐厅奇遇记","headmasterId":27,"startTime":"2121-12-20 08:00:00","cycleTimeJoin":"6,4","cycleTimeJoinName":"周六,周四","week":"周六","headmasterName":"豌豆编程班主任","headmasterNickName":"豌豆编程班主任-糖糖老师","closeStatus":0,"learnerNum":2,"classCount":2,"finishClassRate":"100.0","startSetionNum":0,"totalSection":56,"absentNumber":0,"finishNumber":2},{"id":14538,"className":"L1_21122001_S6/S7_1班","courseId":1655,"childType":0,"pid":1357,"parentCourseName":"图形化编程","courseName":"L1","sectionId":29079,"sectionName":"第1讲_餐厅奇遇记","headmasterId":27,"startTime":"2121-12-20 08:00:00","cycleTimeJoin":"6,4","cycleTimeJoinName":"周六,周四","week":"周六","headmasterName":"豌豆编程班主任","headmasterNickName":"豌豆编程班主任-糖糖老师","closeStatus":0,"learnerNum":1,"classCount":2,"finishClassRate":"100.0","startSetionNum":0,"totalSection":56,"absentNumber":0,"finishNumber":1},{"id":15314,"className":"L1N_22091901_S4/S5_1班","courseId":1833,"childType":0,"pid":1832,"parentCourseName":"图形化编程","courseName":"L1N","sectionId":32214,"sectionName":"第1讲_餐厅奇遇记","headmasterId":37,"startTime":"2022-09-24 08:00:00","cycleTimeJoin":"6,4","cycleTimeJoinName":"周六,周四","week":"周六","headmasterName":"豌豆编程班主任-叶子老师","headmasterNickName":"叶子老师","closeStatus":0,"learnerNum":1,"classCount":8,"finishClassRate":"100.0","startSetionNum":0,"totalSection":56,"absentNumber":0,"finishNumber":1},{"id":15264,"className":"L1VK_22090301_S3/S4/S5_1班","courseId":1744,"childType":0,"pid":1743,"parentCourseName":"图形化编程课","courseName":"L1VK","sectionId":29946,"sectionName":"第1讲_保卫豌豆小镇","headmasterId":32,"startTime":"2022-09-03 08:00:00","cycleTimeJoin":"6,4","cycleTimeJoinName":"周六,周四","week":"周六","headmasterName":"豌豆编程班主任-鳄鱼老师","headmasterNickName":"豌豆编程班主任-鳄鱼老师","closeStatus":0,"learnerNum":1,"classCount":200,"finishClassRate":"0.0","startSetionNum":0,"totalSection":60,"absentNumber":0,"finishNumber":0},{"id":15163,"className":"L1（VK专用）_22082701_S3/S4/S5_1班","courseId":1744,"childType":0,"pid":1743,"parentCourseName":"图形化编程课","courseName":"L1VK","sectionId":29946,"sectionName":"第1讲_保卫豌豆小镇","headmasterId":31,"startTime":"2022-08-27 08:00:00","cycleTimeJoin":"6,4","cycleTimeJoinName":"周六,周四","week":"周六","headmasterName":"豌豆编程班主任-悠悠老师","headmasterNickName":"悠悠老师","closeStatus":0,"learnerNum":1,"classCount":200,"finishClassRate":"0.0","startSetionNum":0,"totalSection":60,"absentNumber":0,"finishNumber":0},{"id":14981,"className":"L1·基础_22081301_S4/S5_1班","courseId":1452,"childType":0,"pid":1451,"parentCourseName":"测试_图形化编程","courseName":"L1·基础","sectionId":27415,"sectionName":"第1讲_保卫豌豆小镇","headmasterId":47,"startTime":"2022-08-13 08:00:00","cycleTimeJoin":"6,4","cycleTimeJoinName":"周六,周四","week":"周六","headmasterName":"方燕玲-老师","headmasterNickName":"燕玲","closeStatus":1,"learnerNum":0,"classCount":3,"finishClassRate":"","startSetionNum":0,"totalSection":59,"absentNumber":0,"finishNumber":0},{"id":15870,"className":"L1·基础_22070901_S4/S5_1班","courseId":1452,"childType":0,"pid":1451,"parentCourseName":"测试_图形化编程","courseName":"L1·基础","sectionId":27415,"sectionName":"第1讲_保卫豌豆小镇","headmasterId":47,"startTime":"2022-07-09 08:00:00","cycleTimeJoin":"6,4","cycleTimeJoinName":"周六,周四","week":"周六","headmasterName":"方燕玲-老师","headmasterNickName":"燕玲","closeStatus":0,"learnerNum":0,"classCount":3,"finishClassRate":"","startSetionNum":0,"totalSection":59,"absentNumber":0,"finishNumber":0},{"id":15317,"className":"L1VK_22070901_S3/S4/S5_1班","courseId":1744,"childType":0,"pid":1743,"parentCourseName":"图形化编程课","courseName":"L1VK","sectionId":29946,"sectionName":"第1讲_保卫豌豆小镇","headmasterId":31,"startTime":"2022-07-09 08:00:00","cycleTimeJoin":"6,4","cycleTimeJoinName":"周六,周四","week":"周六","headmasterName":"豌豆编程班主任-悠悠老师","headmasterNickName":"悠悠老师","closeStatus":0,"learnerNum":1,"classCount":200,"finishClassRate":"0.0","startSetionNum":0,"totalSection":60,"absentNumber":0,"finishNumber":0},{"id":15863,"className":"L1·基础_22070201_S4/S5_1班","courseId":1452,"childType":0,"pid":1451,"parentCourseName":"测试_图形化编程","courseName":"L1·基础","sectionId":27415,"sectionName":"第1讲_保卫豌豆小镇","headmasterId":47,"startTime":"2022-07-02 08:00:00","cycleTimeJoin":"6,4","cycleTimeJoinName":"周六,周四","week":"周六","headmasterName":"方燕玲-老师","headmasterNickName":"燕玲","closeStatus":0,"learnerNum":0,"classCount":3,"finishClassRate":"","startSetionNum":0,"totalSection":59,"absentNumber":0,"finishNumber":0},{"id":15876,"className":"L1·基础_22061801_S4/S5_1班","courseId":1452,"childType":0,"pid":1451,"parentCourseName":"测试_图形化编程","courseName":"L1·基础","sectionId":27415,"sectionName":"第1讲_保卫豌豆小镇","headmasterId":47,"startTime":"2022-06-18 00:00:00","cycleTimeJoin":"6,4","cycleTimeJoinName":"周六,周四","week":"周六","headmasterName":"方燕玲-老师","headmasterNickName":"燕玲","closeStatus":0,"learnerNum":1,"classCount":3,"finishClassRate":"0.0","startSetionNum":0,"totalSection":59,"absentNumber":0,"finishNumber":0}]},"count":"","message":"OK","msg":"success","traceId":"ac16019c16506186781906505d0001","success":'true'}

           return json.dumps(response)
        else:
            return jsonify({
            "code": 202,
            "msg": "请输入传参"
        })
    else:
        return jsonify({
            "code": 201,
            "msg": "请使用post请求"
        })


if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5052',debug=True)