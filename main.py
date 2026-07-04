from gtts import gTTS

# النص الذي تريد تحويله لصوت
text = "مرحباً، تم تشغيل النظام بنجاح!"

# إنشاء الصوت
tts = gTTS(text=text, lang='ar')

# حفظ الملف
tts.save("output.mp3")
print("تم إنشاء الملف بنجاح!")
