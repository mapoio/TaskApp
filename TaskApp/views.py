from djoser.views import RegistrationView
from djoser import utils
from TaskApp import settings

class CustomRegistrationView(RegistrationView):
    '''
    这是用于DEBUG时没有设置邮件服务器，将会通过控制台打印邮件内容，来进行测试
    实际过程中不会调用，注意，在激活地址中是由前台来控制的，参数是直接在最后两个字段，
    由前端调用，用来激活
    '''

    def send_activation_email(self, user):
        email_factory = utils.UserActivationEmailFactory.from_request(self.request, user=user)
        email = email_factory.create()
        if settings.EMAIL_BACKEND:
            print(email.body)
        email.send()

    def send_confirmation_email(self, user):
        email_factory = utils.UserConfirmationEmailFactory.from_request(self.request, user=user)
        email = email_factory.create()
        if settings.EMAIL_BACKEND:
            print(email.body)
        email.send()