#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
import sys
import time

# ================== إعدادات النسخة ==================
VERSION = "1.0"
VERSION_URL = "https://raw.githubusercontent.com/nasimhf/monir/main/version.txt"
SCRIPT_URL = "https://raw.githubusercontent.com/nasimhf/monir/main/tool.py"

# ================== دالة فحص التحديث ==================
def check_update():
    """فحص التحديثات وتحميل النسخة الجديدة إذا وجدت"""
    try:
        print("🔍 فحص التحديثات...")
        r = requests.get(VERSION_URL, timeout=10)
        latest_version = r.text.strip()

        if latest_version != VERSION:
            print(f"🔄 يوجد تحديث جديد: {latest_version}")
            
            # تحميل نسخة الأداة الجديدة
            code = requests.get(SCRIPT_URL, timeout=10).text

            # حفظ النسخة الجديدة مباشرة في نفس الملف
            file_name = os.path.basename(__file__)
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(code)

            print(f"✅ تم تحديث الأداة إلى الإصدار {latest_version}")
            print("♻️ إعادة تشغيل النسخة الجديدة...")
            time.sleep(1)

            # إعادة تشغيل النسخة الجديدة تلقائيًا
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            print("✅ لديك أحدث إصدار")

    except Exception as e:
        print(f"⚠️ حدث خطأ أثناء التحديث: {e}")

# ================== دالة الأداة الرئيسية ==================
def main_tool():
    """هنا ضع جميع الوظائف الرئيسية للأداة"""
    print(f"\n🚀 الأداة تعمل الآن! الإصدار الحالي: {VERSION}\n")
    
    while True:
        print("⚙️ القائمة الرئيسية:")
        print("1️⃣ مثال على وظيفة")
        print("2️⃣ خروج")
        choice = input("اختر رقم: ").strip()
        
        if choice == "1":
            print("🔹 تنفيذ مثال على الأداة...")
            # هنا ضع الكود الذي تريد تنفيذه
            time.sleep(1)
            print("✅ تم التنفيذ")
        elif choice == "2":
            print("👋 وداعًا!")
            break
        else:
            print("❌ خيار غير صحيح، حاول مرة أخرى.\n")

# ================== نقطة البداية ==================
if __name__ == "__main__":
    check_update()   # أولاً: تحقق من التحديث
    main_tool()      # ثم شغّل الأداة
