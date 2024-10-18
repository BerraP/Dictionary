meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "PART-TİME": "Yarı zamanlı çalışma",
            "BYE": "Görüşürüz",
            }

kelime = input("Kelime giriniz")
if kelime in meme_dict.keys():
    print(meme_dict[kelime]),
else:
    print("Bizim sözlüğümüzde böyle profesyonlerce kelimeler yok")
