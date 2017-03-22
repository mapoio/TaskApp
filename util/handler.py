from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from TaskApp import settings

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        # response.data['code'] = exc.status_code
        # response.data['error'] = exc.default_code
        if settings.TEST == False:
            return ErrorResponse(err_code=exc.status_code // 100,err_message=exc.default_code,message=exc.detail,status=exc.status_code)
    return response


class Error(Exception):
    def __init__(self, err_message='Internal Server Error',
                 message=u'服务器异常', status_code=status.HTTP_400_BAD_REQUEST):
        self.err_code = status_code // 100
        self.err_message = err_message
        self.message = message
        self.status_code = status_code

    def __unicode__(self):
        return u'[Error] %d: %s(%d)' % (self.err_code, self.err_message, self.status_code)

    def getResponse(self):
        return ErrorResponse(self.err_code, self.err_message, self.message, self.status_code)


def ErrorResponse(err_code=0, err_message='Internal Server Error',
                  message=u'服务器异常', status=status.HTTP_400_BAD_REQUEST, headers=None):
    err = {
        'error_code': err_code,
        'error': err_message,
        'message': message,
    }
    return Response(err, status, headers=headers)