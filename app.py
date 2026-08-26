from flask import Flask, request, render_template_string

app = Flask(__name__)

# كود الـ HTML والـ CSS الخاص بواجهتك المخصصة بالكامل
html_content = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بوابة الوصول الموحدة</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: sans-serif; }
        body { background-color: #0d0d11; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .login-card { background-color: #121216; border: 1px solid #1e1e24; padding: 40px 30px; border-radius: 24px; width: 100%; max-width: 420px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.7); text-align: center; }
        .badge-container { display: inline-flex; align-items: center; gap: 6px; border: 1px solid #26262b; background-color: #18181d; padding: 6px 18px; border-radius: 20px; color: #a0a0a5; font-size: 12px; margin-bottom: 24px; }
        h2 { color: #ffffff; font-size: 26px; margin-bottom: 12px; font-weight: 600; }
        .description { color: #787880; font-size: 13px; margin-bottom: 35px; line-height: 1.5; }
        .form-group { margin-bottom: 22px; text-align: right; }
        .form-group label { display: block; color: #b0b0b5; font-size: 13px; margin-bottom: 8px; padding-right: 4px; }
        .input-control { width: 100%; padding: 16px 20px; background-color: #16161a; border: 1px solid #242429; border-radius: 14px; color: #ffffff; font-size: 14px; outline: none; text-align: right; }
        .input-control::placeholder { color: #4a4a50; }
        .btn-submit { width: 100%; padding: 15px; background-color: transparent; color: #e54b4b; font-size: 15px; font-weight: 500; border: 1px solid #e54b4b; border-radius: 25px; cursor: pointer; transition: all 0.2s; margin-top: 10px; }
        .btn-submit:hover { background-color: #e54b4b; color: #ffffff; }
        .divider { display: flex; align-items: center; color: #44444a; font-size: 12px; margin: 25px 0; }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background-color: #222226; }
        .divider span { padding: 0 12px; }
        .btn-alternative { width: 100%; padding: 14px; background-color: #16161a; border: 1px solid #242429; border-radius: 14px; color: #e1e1e6; font-size: 14px; cursor: pointer; margin-bottom: 12px; display: flex; align-items: center; justify-content: center; gap: 8px; }
        .footer-action { color: #787880; font-size: 13px; margin-top: 30px; }
        .footer-action a { color: #e54b4b; text-decoration: none; margin-right: 4px; }
    </style>
</head>
<body>
    <div class="login-card">
        <div class="badge-container"><span>🔒 الوصول إلى الحساب الإلكتروني</span></div>
        <h2>تسجيل الدخول</h2>
        <p class="description">أدخل بيانات الاعتماد الخاصة بك للوصول إلى لوحة التحكم الموحدة وإدارة خدماتك محلياً.</p>

        <form action="/login-check" method="POST">
            <div class="form-group">
                <label>البريد الإلكتروني أو اسم المستخدم</label>
                <input type="text" class="input-control" name="username" placeholder="user@example.com أو username" required>
            </div>
            <div class="form-group">
                <label>كلمة المرور</label>
                <input type="password" class="input-control" name="password" placeholder="••••••••" required>
            </div>
            <button type="submit" class="btn-submit">تسجيل الدخول</button>
        </form>

        <div class="divider"><span>أو كخيارات بديلة</span></div>
        <button type="button" class="btn-alternative">🔑 الدخول بواسطة مفتاح المرور الآمن</button>
        <button type="button" class="btn-alternative">🌐 المتابعة باستخدام الحساب الموحد</button>
        <div class="footer-action">ليس لديك حساب بعد؟ <a href="#">إنشاء حساب جديد</a></div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

@app.route('/login-check', methods=['POST'])
def login_check():
    username = request.form.get('username')
    password = request.form.get('password')

    # محاكاة فحص محلي آمن داخل السيرفر
    if username == "admin@example.com" and password == "123456":
        return "<h3>مرحباً بك! تم تسجيل الدخول بنجاح إلى لوحتك التجريبية المحلية.</h3>"
    else:
        return "<h3>خطأ: بيانات الاعتماد غير صحيحة. هذا الفحص يتم محلياً.</h3>"

if __name__ == '__main__':
    app.run()

