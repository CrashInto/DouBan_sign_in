# DouBan_sign_in
模拟登陆豆瓣（可解决验证码）</br>
登陆过程可能遇到验证码。。。</br>
使用Beautifulsoup解析，判断是否存在验证码。</br>
如果存在捕获验证码图片地址以及验证码图片ID（构造登录表单需要的内容）</br>
通过seleniumr调用webdriver请求验证码图片地址。通过input接收用户输入，完成表单构造，发起请求。完成登陆。</br>
可以通过分析登陆后的页面获取登陆用户，获取到了，即视为模拟登陆成功。</br>