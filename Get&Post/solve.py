#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
要求用 post 提交答案

手动拿 header, 然后 POST 提交
GET /task/4/solve?answer=restful&_token=tIkctE5pgqIENuUBbn92lN4yOyyPRIHYEutg4l6c HTTP/1.1
Host: www.qlcoder.com
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36
Referer: http://www.qlcoder.com/task/7527
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en,zh;q=0.8,zh-CN;q=0.6
Cookie: tn=0; gr_user_id=002c9d88-76c8-4999-9334-d923db3d65e2; fs=1; tn=4; uuid=589597c7bfc28; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6ImZHQlJEcVRLVVlGUnN6VWJPMENYNVE9PSIsInZhbHVlIjoiTEVZbVFabmxPcWFhNkpMeDBLZ0lqdz09IiwibWFjIjoiMTgxZWNlNDMyYTY3YmQ5ODAyYWFlOWUwNDU3NGNiMzU0ODczZDgzOWFlNjIzYjk4Nzk5NzRhZDNlOTljNzgxMSJ9; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1486178107,1486198835; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1486202082; XSRF-TOKEN=eyJpdiI6InF6aWJBbG95eUxtY1VoQUphRStsSUE9PSIsInZhbHVlIjoid1dCVkdJRkpXRGRcLzBreWJRNjNlanh2cTcxWVpsNkpES2d5RFwvSUhSR2RWYmlDWlpYd3hla1hnclg0ZnRabGFWQXVHU1ZNbUlZYm11dzV0OUNlajRuQT09IiwibWFjIjoiNDFmNTEzZjY1ZGM3YWEwYzc3YWNmNTkyNzg0MWRmNmQ1NzQ1YjJjM2M0MDg5YzQ0NjY2NTg1ZTFmMDM0NjA4NiJ9; laravel_session=eyJpdiI6IjErZVF1SGZmRmxPRVwvNkd5aEMxaWZRPT0iLCJ2YWx1ZSI6IjIyWTI3QkRqNDZtSW9Bd2JUZnJjN2J0ZDVBbXFHdE9IVDgyOEZwaXlEMGhZZ2VCdVdaeTdFREkzczF1aXh6dmNxMzdSQ2FIMWFEeVNDMGlxeHNtYzZRPT0iLCJtYWMiOiJlM2UwY2I4ZjA3ZTFlMTU5YWRiNzA3N2JjMWJiYTMyYzA0OWMzYjhiMWU4ZjIzZGViOGI1NjI0ZTljMmYyMWM4In0%3D; gr_session_id_80dfd8ec4495dedb=f77b0c5d-e077-4810-95b0-859fbaadd854
"""
import requests

__author__ = '__L1n__w@tch'

if __name__ == "__main__":
    right_answer = "restful"
    s = requests.session()

    header = {
        "Host": "www.qlcoder.com",
        "Cookie": "tn=0; gr_user_id=002c9d88-76c8-4999-9334-d923db3d65e2; fs=1; tn=4; uuid=589597c7bfc28; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6ImZHQlJEcVRLVVlGUnN6VWJPMENYNVE9PSIsInZhbHVlIjoiTEVZbVFabmxPcWFhNkpMeDBLZ0lqdz09IiwibWFjIjoiMTgxZWNlNDMyYTY3YmQ5ODAyYWFlOWUwNDU3NGNiMzU0ODczZDgzOWFlNjIzYjk4Nzk5NzRhZDNlOTljNzgxMSJ9; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1486178107,1486198835; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1486202082; XSRF-TOKEN=eyJpdiI6InF6aWJBbG95eUxtY1VoQUphRStsSUE9PSIsInZhbHVlIjoid1dCVkdJRkpXRGRcLzBreWJRNjNlanh2cTcxWVpsNkpES2d5RFwvSUhSR2RWYmlDWlpYd3hla1hnclg0ZnRabGFWQXVHU1ZNbUlZYm11dzV0OUNlajRuQT09IiwibWFjIjoiNDFmNTEzZjY1ZGM3YWEwYzc3YWNmNTkyNzg0MWRmNmQ1NzQ1YjJjM2M0MDg5YzQ0NjY2NTg1ZTFmMDM0NjA4NiJ9; laravel_session=eyJpdiI6IjErZVF1SGZmRmxPRVwvNkd5aEMxaWZRPT0iLCJ2YWx1ZSI6IjIyWTI3QkRqNDZtSW9Bd2JUZnJjN2J0ZDVBbXFHdE9IVDgyOEZwaXlEMGhZZ2VCdVdaeTdFREkzczF1aXh6dmNxMzdSQ2FIMWFEeVNDMGlxeHNtYzZRPT0iLCJtYWMiOiJlM2UwY2I4ZjA3ZTFlMTU5YWRiNzA3N2JjMWJiYTMyYzA0OWMzYjhiMWU4ZjIzZGViOGI1NjI0ZTljMmYyMWM4In0%3D; gr_session_id_80dfd8ec4495dedb=f77b0c5d-e077-4810-95b0-859fbaadd854"
    }

    post_data = {
        "answer": right_answer,
        "_token": "tIkctE5pgqIENuUBbn92lN4yOyyPRIHYEutg4l6c"
    }

    response = s.post("http://www.qlcoder.com/task/4/solve", data=post_data, headers=header)
    print(response.text)
