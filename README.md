# DecisionTree For Classification ( Sınıflandırma için Karar Ağacı )

Üniversitede 2018 yılı bahar yarıyılı itibariyle dönem projem için <br>
herhangi bir kütüphane kullanmadan geliştirdiğim karar ağacı algoritması. <br>

Bu kod http://chem-eng.utoronto.ca/~datamining/dmc/datasets/weather_nominal.csv adresindeki <br>
verseti üzerinde test edilmiş ve gerekli hesaplamaları doğru yaptığı görülmüştür.

<h2>AÇIKLAMA</h2>

**a)	Yazılımın Agaç Gösterimi** <BR>
 
![](img/Ekran%20Alıntısı.JPG)
<BR>

**b)	Yukarıda verilen ağaçtaki düğümlerin açıklamaları**<BR>
•	**Decision Tree For Classification :** Projenin adı.<BR>
•	**Hesapla :** ID3 algoritması için gereken hesaplamaları yapan fonksiyonları bulunduran matematiksel hesapları yapan sınıf.<BR>
•	**Nitelik :** Oluşturulacak sınıflandırma ağacındaki her bir niteliği belirtecek ve nitelik için gerekli işlemleri halledebilecek yetkinlikte bir sınıf.<BR>
•	**Kenar :** Niteliğin içindeki kenarları ifade edecek sınıf.<BR>
<BR>

**c)	 Gelinen Aşama**

<BR>
•	Düğümü belirtecek nitelik nesnelerini oluşturacak ve verilen bir kolonu ihtiyacı karşılar şekilde (en azından şuan kestirebilinen ihtiyaçları)  yazılan nitelik sınıfı yazıldı.<BR>
•	Düğümün kenarlarını ifade edecek bir kenar sınıfı yazıldı.<BR>
•	Belirlediğimiz veri yapılarını işeyip ID3 algoritmasına ait hesapları yapabilecek bir hesapla sınıfı yazıldı.<BR>
•	Hesapla sınıfındaki “genelEntropiHesapla” fonksiyonu test edildi ve onaylandı.<BR>
•	Hesapla sınıfındaki “ağırlıklıEntropiHesapla” fonksiyonu test edildi ve onaylandı.<BR>
•	Ağaç modeli başarıyla oluşturuldu.<BR>
•	Tahmin başarı ile yapıldı.<BR>

<BR>

**d)	Hedefler**<BR>
•	Tkinder kütüphanesiyle basit bir arayüz tasarlanıp, kullanıcı dostu bir uygulama haline getirilecek.<BR>


