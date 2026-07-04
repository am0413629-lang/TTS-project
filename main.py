from gtts import gTTS
import os

# النص اللي إنت عايزه ينطق
text = "مرحباً بك في عالم البرمجة، هذا أول صوت لي من داخل المصنع!"

# تحويل النص لصوت (باللغة العربية)
tts = gTTS(text=text, lang='ar')

# حفظ الملف
tts.save("output.mp3")

print("تم تحويل النص إلى ملف صوتي بنجاح! الملف اسمه output.mp3")
