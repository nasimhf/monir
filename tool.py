import requests
import os
import sys
#hakim
VERSION = "1.1"

VERSION_URL = "https://raw.githubusercontent.com/USERNAME/mytool/main/version.txt"
SCRIPT_URL = "https://raw.githubusercontent.com/USERNAME/mytool/main/tool.py"


def check_update():
    try:
        print("🔍 فحص التحديثات...")

        r = requests.get(VERSION_URL, timeout=10)
        latest_version = r.text.strip()

        if latest_version != VERSION:
            print("🔄 يوجد تحديث جديد:", latest_version)

            code = requests.get(SCRIPT_URL).text

            file_name = os.path.basename(__file__)

            # حفظ نسخة جديدة
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(code)

            print("✅ تم تحديث الأداة")
            print("♻️  hhhسيتم إعادة تشغيل الأداة")

            os.execv(sys.executable, ["python"] + sys.argv)

        else:
            print("✅ لديك أحدث إصدار")

    except Exception as e:
        print("⚠️ تعذر التحقق من التحديث")
