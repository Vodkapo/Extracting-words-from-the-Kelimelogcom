import requests
from bs4 import BeautifulSoup

harf = input("Harf : ")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.163 Safari/537.36 "
}
request = requests.get("http://kelimelog.com/oxford-english-"+harf+"-harfi-ile-baslayan-kelimeler/", headers=header) 
tumVeriler = BeautifulSoup(request.content, "html.parser")

id = 1
f = open("words_"+harf+".txt", "w")
d = "A1"
'''türkçe kelimeler için "color:0000ff"'''
'''ingilizce kelimeler için "color:#ff0000"'''
for x, y in zip(tumVeriler.find("div", {"class" : "entry-content"}).find_all("span", {"style":"color:#0000ff"}), tumVeriler.find("div", {"class" : "entry-content"}).find_all("span", {"style":"color:#ff0000"})):
  a = (x.get_text())
  b = (y.get_text())
  bulb = b.find(" ")
  try:
    if bulb == -1: 
      request2 = requests.get("https://sozluk.turkceokunusu.com/"+b+"-okunusu/")
      tumVeriler2 = BeautifulSoup(request2.content, "html.parser")
      for z in tumVeriler2.find("div", {"class" : "box success aligncenter"}).find_all("h2"):
        c = (z.get_text())     
        f.write("WordsModel(\nid: "+str(id)+","+"\nselected:false,\nenglish:\""+b+"\",\nturkish:\""+a+"\",\nlvl:\""+d+"\",\npronunciation:\""+c+"\"),\n")
        #print("WordsModel(\nid: "+str(id)+","+"\nselected:false,\nenglish:\""+b+"\",\nturkish:\""+a+"\",\nlvl:\""+d+"\",\npronunciation:\""+c+"\"),\n")
        if (a == "uzakta, uzağa, uzak") or (a == "allah’a ısmarlaladık!, hoşçakal!") or (a == "kesmek, azaltmak") or (
                a == "dvd") or (a == "göz") or (a == "gelecek") or (a == "spor salonu") or (
                a == "eş (erkek), koca") or (a == "onun, kendi, onunki") or (
                a == "yalnız, sadece; biraz önce; tam olarak") or (a == "bilmek; tanımak") or (a == "öğle yemeği") or (
                a == "benim") or (a == "hemşire") or (a == "kendi, kendisinin") or (a == "koymak") or (
                a == "oldukça, epey") or (a == "koşmak; yönetmek; akmak") or (a == "yüzme") or (a == "tür, cins") or (
                a == "ziyaretçi") or (a == "yanlış, hatalı") or (a == "kendi"):
          d = "A2"
        if (a == "berbat, kötü") or (a == "düğme, buton") or (a == "bisiklete binmek") or (a == "kurutmak") or (
                a == "aşırı, aşırı boyutta, son derece, oldukça") or (a == "gelecek, istikbal") or (
                a == "adam, herif") or (a == "yaralamak, acımak, incitmek") or (a == "kendi, kendisi, kendisini") or (
                a == "atlamak, zıplamak") or (a == "bilgi") or (a == "şanslı, talihli") or (
                a == "kendimi, kendime, kendim, bizzat kendim") or (a == "sert kabuklu yemiş, fındık, ceviz") or (
                a == "sahip, mal sahibi") or (a == "itmek, zorlamak") or (a == "sessizce") or (a == "koşu") or (
                a == "yöntem; düzen, düzenek") or (a == "karakteristik, tipik") or (a == "ses, söz, ifade") or (
                a == "vay be!") or (a == "seninki, sizin ki"):
          d = "B1"
        if (a == "farkında, haberdar") or (a == "geçerek, geçip giderek, yakınından geçerek") or (
                a == "kesik, kesinti") or (a == "vazife, görev, nöbet, sorumluluk") or (a == "ekstra") or (
                a == "daha ileri, öteye") or (a == "suçlu, kusurlu") or (
                a == "acele etmek, hızlandırmak, çabuk olmak") or (
                a == "bilgi teknolojisi, bilgiyi depolamak ve göndermek için bilgisayar ve diğer elektronik aletlerin kullanımı") or (
                a == "yargılamak, değerlendirmek, karara varmak") or (a == "vuruş, çalma") or (a == "lüks, konfor") or (
                a == "gizem, esrar, sır") or (a == "nükleer") or (a == "dışarda, açık havada") or (
                a == "itiş kakış, itme, itekleme") or (a == "alıntı yapmak, aktarmak") or (
                a == "yönetmek, hükmetmek") or (a == "semptom, bulgu, belirti") or (a == "lastik") or (
                a == "oy vermek, oy kullanmak") or (a == "hata, kusur") or (a == "genç"):
          d = "B2"
        if (a == "sakar; uygunsuz") or (a == "-den hariç") or (a == "çekici, sevimli") or (
                a == "dinamik, hareketli") or (a == "aşırılık") or (a == "ayrıca, bundan başka, üstelik") or (
                a == "prensip, kılavuz, talimat") or (a == "varsayım") or (a == "resmen bildirmek; dağıtmak") or (
                a == "haklı göstermek, aklamak, haklı çıkarmak, savunmak, doğrulamak") or (a == "takım, donanım") or (
                a == "lirik şiir") or (a == "efsane, söylence") or (a == "besin, gıda, beslenme") or (
                a == "oksijen") or (a == "bulmaca") or (a == "anket, soru kâğıdı, soruşturma") or (
                a == "acele etmek, koşturmak") or (a == "sempati, sevgi, ilgi, acıma, merhamet") or (a == "tünel") or (
                a == "oy kullanma") or (a == "hata, kusur") or (a == "fakat, ama, ancak"):
          d = "C1"
    if bulb != -1:
      b2 = b.replace(" ", "-")
      request2 = requests.get("https://sozluk.turkceokunusu.com/"+b2+"-okunusu/")
      tumVeriler2 = BeautifulSoup(request2.content, "html.parser")
      for z in tumVeriler2.find("div", {"class" : "box success aligncenter"}).find_all("h2"):
        c = (z.get_text())     
        f.write("WordsModel(\nid: "+str(id)+","+"\nselected:false,\nenglish:\""+b+"\",\nturkish:\""+a+"\",\nlvl:\""+d+"\",\npronunciation:\""+c+"\"),\n")
        #print("WordsModel(\nid: "+str(id)+","+"\nselected:false,\nenglish:\""+b+"\",\nturkish:",""+a+"\",\nlvl:\""+d+"\",\npronunciation:\""+c+"\"),\n")
        if (a == "uzakta, uzağa, uzak") or (a == "allah’a ısmarlaladık!, hoşçakal!") or (a == "kesmek, azaltmak") or (
                a == "dvd") or (a == "göz") or (a == "gelecek") or (a == "spor salonu") or (
                a == "eş (erkek), koca") or (a == "onun, kendi, onunki") or (
                a == "yalnız, sadece; biraz önce; tam olarak") or (a == "bilmek; tanımak") or (a == "öğle yemeği") or (
                a == "benim") or (a == "hemşire") or (a == "kendi, kendisinin") or (a == "koymak") or (
                a == "oldukça, epey") or (a == "koşmak; yönetmek; akmak") or (a == "yüzme") or (a == "tür, cins") or (
                a == "ziyaretçi") or (a == "yanlış, hatalı") or (a == "kendi"):
          d = "A2"
        if (a == "berbat, kötü") or (a == "düğme, buton") or (a == "bisiklete binmek") or (a == "kurutmak") or (
                a == "aşırı, aşırı boyutta, son derece, oldukça") or (a == "gelecek, istikbal") or (
                a == "adam, herif") or (a == "yaralamak, acımak, incitmek") or (a == "kendi, kendisi, kendisini") or (
                a == "atlamak, zıplamak") or (a == "bilgi") or (a == "şanslı, talihli") or (
                a == "kendimi, kendime, kendim, bizzat kendim") or (a == "sert kabuklu yemiş, fındık, ceviz") or (
                a == "sahip, mal sahibi") or (a == "itmek, zorlamak") or (a == "sessizce") or (a == "koşu") or (
                a == "yöntem; düzen, düzenek") or (a == "karakteristik, tipik") or (a == "ses, söz, ifade") or (
                a == "vay be!") or (a == "seninki, sizin ki"):
          d = "B1"
        if (a == "farkında, haberdar") or (a == "geçerek, geçip giderek, yakınından geçerek") or (
                a == "kesik, kesinti") or (a == "vazife, görev, nöbet, sorumluluk") or (a == "ekstra") or (
                a == "daha ileri, öteye") or (a == "suçlu, kusurlu") or (
                a == "acele etmek, hızlandırmak, çabuk olmak") or (
                a == "bilgi teknolojisi, bilgiyi depolamak ve göndermek için bilgisayar ve diğer elektronik aletlerin kullanımı") or (
                a == "yargılamak, değerlendirmek, karara varmak") or (a == "vuruş, çalma") or (a == "lüks, konfor") or (
                a == "gizem, esrar, sır") or (a == "nükleer") or (a == "dışarda, açık havada") or (
                a == "itiş kakış, itme, itekleme") or (a == "alıntı yapmak, aktarmak") or (
                a == "yönetmek, hükmetmek") or (a == "semptom, bulgu, belirti") or (a == "lastik") or (
                a == "oy vermek, oy kullanmak") or (a == "hata, kusur") or (a == "genç"):
          d = "B2"
        if (a == "sakar; uygunsuz") or (a == "-den hariç") or (a == "çekici, sevimli") or (
                a == "dinamik, hareketli") or (a == "aşırılık") or (a == "ayrıca, bundan başka, üstelik") or (
                a == "prensip, kılavuz, talimat") or (a == "varsayım") or (a == "resmen bildirmek; dağıtmak") or (
                a == "haklı göstermek, aklamak, haklı çıkarmak, savunmak, doğrulamak") or (a == "takım, donanım") or (
                a == "lirik şiir") or (a == "efsane, söylence") or (a == "besin, gıda, beslenme") or (
                a == "oksijen") or (a == "bulmaca") or (a == "anket, soru kâğıdı, soruşturma") or (
                a == "acele etmek, koşturmak") or (a == "sempati, sevgi, ilgi, acıma, merhamet") or (a == "tünel") or (
                a == "oy kullanma") or (a == "hata, kusur") or (a == "fakat, ama, ancak"):
          d = "C1"
  except:
    f.write("WordsModel(\nid: "+str(id)+","+"\nselected:false,\nenglish:\""+b+"\",\nturkish:\""+a+"\",\nlvl:\""+d+"\",\npronunciation:\"\"),\n")
    #print("WordsModel(\nid: "+str(id)+","+"\nselected:false,\nenglish:\""+b+"\",\nturkish","\""+a+"\",\nlvl:\""+d+"\",\npronunciation:\"\"),\n")
  id += 1
f.close()