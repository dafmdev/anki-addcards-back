def cleaner(text_ipa):
    text_ipa = text_ipa.replace("r", "ɹ")
    if "/" not in text_ipa:
        text_ipa = "/" + text_ipa + "/"

    return text_ipa
