# SafeRay-Guard: X-Ray Güvenlik Protokolü Simülasyonu

Bu proje, Siemens SIREMOBIL Compact L cihazında raporlanan (FDA MAUDE Rapor No: 24742181) "beklenmedik radyasyon aktivasyonu" hatasını önlemek amacıyla geliştirilmiş bir güvenlik katmanı simülasyonudur.

## Problemin Tanımı
Cihazın cerrahi müdahale sırasında operatör komutu olmaksızın kendi kendine aktive olması, ciddi bir radyasyon güvenliği krizidir. Bu proje, bu hatayı yazılımsal bir "ikincil onay" mekanizmasıyla engellemeyi hedefler.

## 15 Günlük Geliştirme Planı
- **1-3. Gün:** FDA ve benzeri vaka analizlerinin yapılması.
- **4-7. Gün:** Sistemin mantıksal akış şemasının tasarlanması.
- **8-12. Gün:** C++ tabanlı güvenlik algoritmasının kodlanması ve simülasyonu.
- **13-15. Gün:** Test raporlarının oluşturulması ve dokümantasyon.

## Teknik Çözüm
Sistem, radyasyon aktivasyonu için sadece ana işlemciden gelen sinyale değil; aynı zamanda operatörün fiziksel varlığını doğrulayan ikincil bir sensör/pedal verisine ihtiyaç duyar.
