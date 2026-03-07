#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
import sys
import time
#hhhhjj
VERSION = "1.2"
VERSION_URL = "https://raw.githubusercontent.com/nasimhf/monir/main/version.txt"
SCRIPT_URL = "https://raw.githubusercontent.com/nasimhf/monir/main/tool.py"

def check_update():
    """فحص التحديثات وتحميل النسخة الجديدة إذا وجدت"""
    try:
        print("🔍 فحص التحديثات...")
        r = requests.get(VERSION_URL, timeout=10)
        latest_version = r.text.strip()

        if latest_version != VERSION:
            print(f"🔄 يوجد تحديث جديد: {latest_version}")

            code = requests.get(SCRIPT_URL, timeout=10).text

            # حفظ نسخة جديدة مباشرة في نفس الملف
            file_name = os.path.basename(__file__)
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(code)

            print(f"✅ تم تحديث الأداة إلى الإصدار {latest_version}")
            print("♻️ إعادة تشغيل النسخة الجديدة...")
            time.sleep(1)

            # إعادة تشغيل النسخة الجديدة
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            print("✅ لديك أحدث إصدار")

    except Exception as e:
        print(f"⚠️ حدث خطأ أثناء التحديث: {e}")


def main_tool():
    """هنا ضع كل الأكواد الرئيسية للأداة التي تريدها"""
    print(f"🚀 الأداة تعمل الآن! الإصدار الحالي: {VERSION}")
    # مثال: ضع أي وظيفة تريد التحكم بها
    while True:
        choice = input("⚙️ اختر أمر (1: مثال، 2: خروج): ")
        if choice == "1":
            print("🔹 مثال على عمل الأداة")
        elif choice == "2":
            print("👋 وداعاً!")
            break
        else:
            print("❌ خيار غير صحيح")

if __name__ == "__main__":
    check_update()
    main_tool()
    import requests
import sys
import time

CHECK_URL = "https://raw.githubusercontent.com/nasimhf/Ahmad/main/karim"

def check_subscription():
    try:
        r = requests.get(CHECK_URL, timeout=10)
        data = r.text.strip()

        if "amin" in data:
            print("✅ الاشتراك مفعل")
            return True
        else:
            print("❌ انتهى الاشتراك")
            return False

    except Exception as e:
        print("⚠️ تعذر الاتصال بالخادم")
        return False


if not check_subscription():
    print("🔒 عليك تجديد الاشتراك")
    sys.exit()

print("🚀 مرحبا تم الاشتراك")
input("اضغط Enter للمتابعة...")
