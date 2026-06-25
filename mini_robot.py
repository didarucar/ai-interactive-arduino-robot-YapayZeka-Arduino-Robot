import cv2
import ultralytics
from ultralytics import YOLO
import serial
import time


PORT = 'COM6' 
BAUD_RATE = 9600


try:
    arduino = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print(">> Arduino'ya başarıyla bağlanıldı.")
except Exception as e:
    arduino = None
    print(f"HATA: Arduino'ya bağlanılamadı! Portu kontrol et: {e}")

print(">> Arduino uyandırılıyor, lütfen bekleyin...")
try:
    time.sleep(2)
    print(">> Arduino hazır! Yapay zeka motoru (PyTorch) belleğe yükleniyor...")
    print(">> UYARI: Bu işlem bilgisayarınıza bağlı olarak 30-40 saniye sürebilir, lütfen kapatmayın!")
except KeyboardInterrupt:
    print(">> İşlem kullanıcı tarafından yarıda kesildi!")


model = ultralytics.YOLO('yolov8n-cls.pt')


cap = cv2.VideoCapture(0, cv2.CAP_MSMF)


if not cap.isOpened():
    print(">> Kamera 0 kanalı yanıt vermedi, kanal 1 deneniyor...")
    cap = cv2.VideoCapture(1, cv2.CAP_MSMF)

durum = 'M' 

print("\n🚀 Sistem başlatıldı! Çıkmak için kamera ekranındayken 'q' tuşuna basınız.\n")


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Kameradan görüntü alınamıyor!")
        break

    
    results = model(frame, device='cpu', verbose=False)
    if results[0].probs is not None:
        top1_id = results[0].probs.top1  
        sinif_adi = results[0].names[top1_id].lower()  
        
        print(f"YOLO Şu An Ne Göruyor: {sinif_adi}")

       
        if "cep telefonu" in sinif_adi or "ipod" in sinif_adi:
            durum = 'G' 
            print(">> TELEFON ALGILANDI -> GÜLEN YÜZ GÖNDERİLİYOR")
            
        elif "bardak" in sinif_adi or "cam bardak" in sinif_adi:
            durum = 'U' 
            print(">> BARDAK ALGILANDI -> ÜZGÜN YÜZ GÖNDERİLİYOR")
            
        elif "sunglasses" in sinif_adi:
            durum = 'M'  
            print(">> İĞNE/KIYAFET ALGILANDI -> GÖZLÜKLÜ YÜZ GÖNDERİLİYOR")
            
        else:
            durum = 'N' 
    
    
    
       
        cv2.putText(frame, f"Yapay Zeka: {sinif_adi}", (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    
    cv2.imshow('YOLOv8 Yapay Zeka Denetimi', frame)

    
    if arduino is not None:
        try:
            arduino.write(durum.encode())
        except Exception as e:
            print(f"Veri gönderilirken port hatası oluştu: {e}")

   
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
if arduino is not None:
    arduino.close()
print(">> Sistem güvenli bir şekilde kapatıldı.")