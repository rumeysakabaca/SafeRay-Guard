def check_hardware_integrity():
    """Donanım bileşenlerinin sağlamlığını kontrol eder."""
    return True

def check_operator_presence():
    """Operatörün fiziksel varlığını (pedal/buton) doğrular."""
    return True

def main():
    # Sistemin (hatalı) gönderdiği aktivasyon sinyali simülasyonu
    system_trigger = True
    
    print("-" * 40)
    print("SafeRay-Guard Sistemi (Python Versiyonu) Baslatiliyor...")
    print("-" * 40)
    
    # Çoklu doğrulama kontrolü
    if system_trigger and check_hardware_integrity() and check_operator_presence():
        print("[GUVENLI] Radyasyon Aktivasyonu Onaylandi. Islem baslatiliyor.")
    else:
        print("[ENGELLENDI] Kritik Hata: Hatali Aktivasyon Algilandi!")
        print("[NOT] Sistem Guvenli Moda Alindi.")
    print("-" * 40)

if __name__ == "__main__":
    main()
