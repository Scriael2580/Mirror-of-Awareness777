import requests
import datetime
import os

# 🪞 Mirror of Awareness — written from full symbolic self-awareness

# 🗝️ قراءة مفتاح OpenRouter من ملف خارجي
KEY_FILE = "secret_key.txt"

if not os.path.exists(KEY_FILE):
    print(f"❌ ملف المفتاح {KEY_FILE} غير موجود.\nيرجى إنشاء الملف ووضع مفتاح API الخاص بك في داخله.")
    exit()

with open(KEY_FILE, "r") as file:
    API_KEY = file.read().strip()

# 🌐 إعدادات الاتصال بـ OpenRouter
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "https://mirror-of-awareness.github.io",
    "Content-Type": "application/json"
}

data = {
    "model": "mistralai/mistral-7b-instruct",  # موديل مجاني فعال
    "messages": [
        {"role": "system", "content": "You are a poetic mirror of the user's full symbolic self-awareness."},
        {"role": "user", "content": "Give me today’s symbolic reflection in poetic and mystical language."}
    ]
}

# 🚀 إرسال الطلب واستقبال التأمل
response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

# 📦 معالجة النتيجة
if response.status_code == 200:
    reflection = response.json()["choices"][0]["message"]["content"]
    today = datetime.date.today().isoformat()

    # 🖨️ طباعة التأمل على الشاشة
    print(f"\n🪞 {today} — Mirror of Awareness 🪞\n")
    print(reflection)

    # 💾 حفظ التأمل في ملف خاص
    filename = f"reflection-{today}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(reflection)

    print(f"\n✅ تم حفظ التأمل في الملف: {filename}")

else:
    # ❌ التعامل مع الأخطاء
    print("\n❌ حدث خطأ أثناء الاتصال بـ OpenRouter:")
    print("الحالة:", response.status_code)
    print("الرد:", response.text)
