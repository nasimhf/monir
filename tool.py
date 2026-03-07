#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
import sys
import time
#hkjkkk
VERSION = "1.3"
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

