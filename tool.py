#!/usr/bin/env python3

import requests
import os
import sys
#ahmad
VERSION = "1.2"

VERSION_URL = "https://raw.githubusercontent.com/username/project/main/version.txt"
SCRIPT_URL = "https://raw.githubusercontent.com/username/project/main/tool.py"


def check_update():
    try:
        print("🔍 فحص التحديثات...")

        r = requests.get(VERSION_URL, timeout=10)
        latest_version = r.text.strip()

        if latest_version != VERSION:
            print("🔄 يوجد تحديث جديد:", latest_version)

            code = requests.get(SCRIPT_URL).text

            with open(os.path.basename(__file__), "w", encoding="utf-8") as f:
                f.write(code)

            print("✅ تم تحديث الأداة")
            print("♻️hh أعد تشغيل البرنامج")
            sys.exit()

        else:
            print("✅ لديك أحدث إصدار")

    except:
        print("⚠️ تعذر التحقق من التحديث")


check_update()


print("🚀 مرحبا بك في الأداة")

name = input("ادخل اسمك: ")

print("اهلا", name)
