#include <iostream>

// İkincil güvenlik kontrollerini simüle eden fonksiyonlar
bool checkHardwareIntegrity() { return true; } 
bool checkOperatorPresence() { return true; }  

int main() {
    // Sistemin kendi kendine (hatalı) gönderdiği aktivasyon sinyali
    bool systemTrigger = true; 

    std::cout << "SafeRay-Guard Sistemi Baslatiliyor..." << std::endl;

    // Eğer sistem sinyal gönderirse ama operatör orada değilse aktivasyonu engelle
    if (systemTrigger && checkHardwareIntegrity() && checkOperatorPresence()) {
        std::cout << "[GUVENLI] Radyasyon Aktivasyonu Onaylandi." << std::endl;
    } else {
        std::cout << "[ENGELLENDI] Hatali Aktivasyon Algilandi! Sistem Guvenli Modda." << std::endl;
    }

    return 0;
}
