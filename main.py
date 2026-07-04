import asyncio
import edge_tts
from pydub import AudioSegment
import subprocess
import os

# الإعدادات
TEXT = "أهلاً بك في نظامنا الاحترافي. هذا النص يتم تحويله للغات متعددة وبنفس المدة الزمنية."
LANGUAGES = {
    "ar": "ar-SA-ZariyahNeural",
    "en": "en-US-ChristopherNeural"
}

async def generate_audio():
    files = {}
    # 1. توليد الملفات
    for lang, voice in LANGUAGES.items():
        filename = f"output_{lang}.mp3"
        print(f"جاري توليد: {filename}")
        communicate = edge_tts.Communicate(TEXT, voice)
        await communicate.save(filename)
        files[filename] = AudioSegment.from_mp3(filename).duration_seconds
    
    # 2. حساب المتوسط
    avg_duration = sum(files.values()) / len(files)
    print(f"المتوسط الحسابي للزمن هو: {avg_duration} ثانية.")

    # 3. الموازنة (Normalization)
    for filename, duration in files.items():
        if duration != avg_duration:
            tempo = duration / avg_duration
            output_final = f"final_{filename}"
            # تطبيق الفلتر للحفاظ على حدة الصوت
            cmd = ['ffmpeg', '-i', filename, '-filter:a', f"atempo={tempo}", '-vn', output_final, '-y']
            subprocess.run(cmd)
            print(f"تم ضبط {filename} ليصبح {avg_duration} ثانية.")
        else:
            os.rename(filename, f"final_{filename}")

asyncio.run(generate_audio())
