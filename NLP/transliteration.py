from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def transliterate_text(text, src_lang, tgt_lang):
    return transliterate(text, src_lang, tgt_lang)

# Example Usage
hindi_text = "भाषा मॉडल"
print("Hindi:", hindi_text)
print("Transliterated (ITRANS):", transliterate_text(hindi_text, sanscript.DEVANAGARI, sanscript.ITRANS))
print("Transliterated (HK):", transliterate_text(hindi_text, sanscript.DEVANAGARI, sanscript.HK))
