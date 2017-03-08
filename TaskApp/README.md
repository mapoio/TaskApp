# 用户API接口文档

此文档用于API接口的调试，说明。
后台程序启用了虚拟的EMAIL处理，在部署代码到服务器上时应当关闭这一项  
引用的模块为```djoser```、```djangorestframework-jwt```  
```python3
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
```

## 接口概览  
```
/me/
/register/
/login/ (token based djangorestframework-jwt)
/logout/ (token based djangorestframework-jwt)
/activate/
/username/
/password/
/password/reset/
/password/reset/confirm/
```

## 用户注册
### 接口地址：
```
/api/v1/auth/user/register/
```

### 接口接受方法：
```
POST
```
### POST方法  
#### 传入参数：
```json
{
    "email": "",
    "username": "",
    "password": ""
}
```
#### 必须传入的参数：
```
{
    "username",
    "password"
}
```

#### 接口返回参数  
##### 如果参数全部正确  
状态码：```HTTP_201_CREATED```  
```
{
    "email": "user@example.com",
    "username": "username",
    "id": 1
}
```
##### 如果密码或者用户名为空  
状态码：```400```
```
{
    "username": [
        "该字段不能为空。"
    ],
    "password": [
        "该字段不能为空。"
    ]
}
```
##### 如果已经存在该用户了  
状态码：```400```
```
{
    "username": [
        "已存在一位使用该名字的用户。"
    ]
}
```

## 用户激活  
> 注册后，服务器将会发送一个包含uid和token的链接给用户。  

### 接口地址：  
```
/api/v1/auth/user/activate/
```

### 接口接受方法：
```
POST
```
### POST方法  
#### 传入参数：
```json
{
    "uid": "",
    "token": "",
}
```
#### 必须传入的参数：
```
{
  "uid",
  "token"
}
```

#### 接口返回参数  
##### 如果参数全部正确  
状态码：```HTTP_204_NO_CONTENT```  

##### 如果```uid```或者```token```为空  
状态码：```400```
```
{
    "uid": [
        "该字段不能为空。"
    ],
    "token": [
        "该字段不能为空。"
    ]
}
```

## 用户登陆  
> 登陆是直接获取用户的token来进行以后的资源获取凭证  

### 接口地址：  
```
/api/v1/auth/user/login/
```

### 接口接受方法：
```
POST
```
### POST方法  
#### 传入参数：
```json
{
    "username": "",  
    "password": "",  
}
```
#### 必须传入的参数：
```
{
  	"username",  
    "password"  
}
```

#### 接口返回参数  
##### 如果参数全部正确  
状态码：```201```  
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6IjUxMjI5OTAzNkBxcS5jb20iLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNDg4OTcxNzQzLCJvcmlnX2lhdCI6MTQ4ODk2ODE0M30.uRjzzWDU-jcZ0r1DB3we-YOswNmIWrQjNoq2iaqMehg"
}
```

##### 如果```username```或者```password```为空  
状态码：```400```
```
{
    "username": [
        "该字段不能为空。"
    ],
    "password": [
        "该字段不能为空。"
    ]
}
```

##### 如果```username```或者```password```错误  
状态码：```400```
```
{
    "non_field_errors": [
        "Unable to login with provided credentials."
    ]
}
```

## 用户重置用户名  

### 接口地址：  
```
/api/v1/auth/user/username/
```

### 接口接受方法：
```
POST
```
### POST方法  
#### 传入参数：
```json
{
    "current_password": "",
    "new_username": ""
}
```
#### 必须传入的参数：
```
{
    "current_password",
    "new_username"
}
```

#### 接口返回参数  
##### 如果参数全部正确  
状态码：```HTTP_204_NO_CONTENT```  

##### 如果```new_username```或者```password```不正确  
状态码：```400```
```
{
    "current_password": [
        "Invalid password."
    ],
    "new_username": [
        "已存在一位使用该名字的用户。"
    ]
}
```

## 用户修改密码  

### 接口地址：  
```
/api/v1/auth/user/password/
```

### 接口接受方法：
```
POST
```
### POST方法  
#### 传入参数：
```json
{
    "new_password": "",
    "current_password": ""
}
```
#### 必须传入的参数：
```
{
    "new_password": "",
    "current_password": ""
}
```

#### 接口返回参数  
##### 如果参数全部正确  
状态码：```HTTP_204_NO_CONTENT```  

##### 如果```new_password```或者```password```不正确  
状态码：```400```
```
{
    "current_password": [
        "Invalid password."
    ],
    "new_password": [
        "密码不能为空。"
    ]
}
```

## 用户使用电子邮件重置密码  

### 接口地址：  
```
/api/v1/auth/user/password/reset/
```

### 接口接受方法：
```
POST
```
### POST方法  
#### 传入参数：
```json
{
    "email": ""
}
```
#### 必须传入的参数：
```
{
    "email": ""
}
```

#### 接口返回参数  
##### 如果参数全部正确  
状态码：```HTTP_204_NO_CONTENT```  

##### 如果```new_password```或者```password```不正确  
状态码：```400```
```
{
    "eamil": [
        "电子邮件不正确。"
    ]
}
```

## 用户电子邮件重置密码激活  
> 注册后，服务器将会发送一个包含uid和token的链接给用户。  

### 接口地址：  
```
/api/v1/auth/password/reset/confirm/
```

### 接口接受方法：
```
POST
```
### POST方法  
#### 传入参数：
```json
{
    "uid": "",
    "token": "",
    "new_password": ""
}
```
#### 必须传入的参数：
```
{
    "uid": "",
    "token": "",
    "new_password": ""
}
```

#### 接口返回参数  
##### 如果参数全部正确  
状态码：```HTTP_204_NO_CONTENT```  

##### 如果```uid```或者```token```或者```new_password```为空  
状态码：```400```
```
{
    "uid": [
        "该字段不能为空。"
    ],
    "token": [
        "该字段不能为空。"
    ],
    "new_password": [
        "该字段不能为空。"
    ]
}
```
