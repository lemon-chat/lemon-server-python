from lemon.application import app, mongo
import json
from flask import request
from flask import jsonify

from .models import User

@app.route('/login', methods=['POST'])
def login():
    if request.method != 'POST':
        return jsonify({ 'status': 'FailArguments' })
    obj = request.get_json()
    if 'userid' in obj:
        userid = obj['userid']
    else:
        return jsonify({ 'status': 'FailArguments' })
    if 'credential_type' in obj:
        credential_type = obj['credential_type']
    else:
        credential_type = "password"
    
    if 'credential' in obj:
        credential = obj['credential']
    else:
        return jsonify({ 'status': 'FailArguments' })

    # 开始检查用户信息
    if credential_type == 'password':
        user = User.objects.filter(userid=userid).first()
        if user is None:
            return jsonify({ 'status': 'FailNoUser' })
        if user.password != credential:
            return jsonify({ 'status': 'FailNoPassword' })
        else:
            return jsonify({ 'status': 'Success' })
    else:
        pass

