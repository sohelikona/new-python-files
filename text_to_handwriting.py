import pywhatkit as pw

text = """Jhony Jhony, yes papa, eating sugar no papa, telling lie no papa. Open your mouth, ha ha ha. Baa baa black sheep, have you any wool, yse sir yes sir three bags ful."""


pw.text_to_handwriting(text, "poem.png", [0,0,0])
print("end")