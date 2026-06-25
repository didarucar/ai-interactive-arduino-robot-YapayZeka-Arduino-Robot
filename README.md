
# AI-Powered Interactive Robot with Arduino LED Matrix

This project connects a Python-based AI object detection system with an Arduino-controlled LED matrix to create an interactive robot that changes its emotions based on the objects or colors it sees through the camera.

## 🚀 Features
* **YOLOv8 Computer Vision:** Utilizes a lightweight YOLOv8 classification model to process real-time camera frames.
* **Color & Object Interaction:** * 🟢 **Green / Fruits:** Robot smiles (Happy Mode)
  * 🔴 **Red / Danger:** Robot frowns (Sad Mode)
  * 😎 **Human Face / Person:** Robot wears sunglasses (Cool Mode)
* **Serial Communication:** Python communicates with Arduino over Serial (`pyserial`) at 9600 baud rate.

## 🛠️ Tech Stack & Components
* **Software:** Python 3.x, OpenCV, Ultralytics (YOLOv8), PySerial, Arduino IDE
* **Hardware:** Arduino Uno/Nano, 8x8 LED Matrix (MAX7219)

## 📸 Project Preview:
<img width="1200" height="1600" alt="WhatsApp Image 2026-06-25 at 19 22 59" src="https://github.com/user-attachments/assets/5abda6c8-f252-449c-9b3a-1753b761bfbe" />
<img width="1200" height="1600" alt="WhatsApp Image 2026-06-25 at 19 22 29 (2)" src="https://github.com/user-attachments/assets/e909332e-fcec-4353-a7b0-c185c1700cc6" />
<img width="1200" height="1600" alt="WhatsApp Image 2026-06-25 at 19 22 29 (1)" src="https://github.com/user-attachments/assets/89767ad9-4200-43a8-968e-8630fa4caaa6" />
<img width="1200" height="1600" alt="WhatsApp Image 2026-06-25 at 19 22 29" src="https://github.com/user-attachments/assets/eec52e95-bb13-4339-852e-887671d7eac5" />

# 🤖 Arduino LED Matrisli Yapay Zeka Destekli İnteraktif Robot

Bu proje, Python tabanlı bir yapay zeka nesne algılama sistemi ile Arduino kontrollü bir LED matrisi birbirine bağlar. Kamera aracılığıyla gördüğü nesnelere veya renklere göre duygularını değiştiren etkileşimli bir robot oluşturur.

## 🚀 Özellikler
* **YOLOv8 Bilgisayarlı Görü:** Gerçek zamanlı kamera görüntülerini işlemek için hafif bir YOLOv8 sınıflandırma modeli kullanır.
* **Renk ve Nesne Etkileşimi:** 
  * 🟢 **Yeşil / Meyveler:** Robot gülümser (Mutlu Mod)
  * 🔴 **Kırmızı / Tehlike:** Robot kaşlarını çatar (Üzgün Mod)
  * 😎 **İnsan Yüzü / Kişi:** Robot güneş gözlüğü takar (Havalı Mod)
* **Seri Haberleşme:** Python, Arduino ile 9600 baud hızında Seri port (`pyserial`) üzerinden haberleşir.

## 🛠️ Kullanılan Teknolojiler ve Bileşenler
* **Yazılım:** Python 3.x, OpenCV, Ultralytics (YOLOv8), PySerial, Arduino IDE
* **Donanım:** Arduino Uno/Nano, 8x8 LED Matris (MAX7219)
