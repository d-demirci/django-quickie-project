from userena.forms import SignupForm
from captcha.fields import CaptchaField


class CaptchaSignupForm(SignupForm):
    captcha = CaptchaField()
