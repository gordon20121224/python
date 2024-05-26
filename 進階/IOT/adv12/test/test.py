import whisper

model = whisper.load_model("base")
result = model.transcribe("adv12/test/錄製.m4a")
print(result["text"])
