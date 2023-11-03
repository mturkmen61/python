print("Python {} {} bir dil".format("çok","güzel"))
metin="bugün {} güzel"
print(metin.format("çok"))
metin="{2} {1} {3} {0} {4}"
print(metin.format("güzel","çok","python","bir","dil"))




baslik= "{0:^25.25} {1:>7} {2:<12}"
govde= "{isim:^25.25} {nosu:0>7} {ort:<12.2f}"
print(baslik.format("Adı Soyadı","No","Ortalama"))
print(baslik.format("-" * 25, "-" * 7, "-" * 25))
print(govde.format(isim="Ali Hüsamettin Can Çetinkaya", nosu= "967", ort= 6.2615261287238761782))
