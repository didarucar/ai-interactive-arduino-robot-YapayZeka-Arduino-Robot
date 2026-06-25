 #include <LedControl.h>
 LedControl lc=LedControl(12,11,10,1);
  byte gulenYuz[8]={B00111100, B01000010, B10100101, B10000001, B10100101, B10011001, B01000010, B00111100};
  byte normalYuz[8]={B00111100, B01000010, B10100101, B10000001, B10111101, B10000001, B01000010, B00111100};
  byte gozlukluYuz[8]={B00111100, B01111110, B11111111, B11111111, B10000001, B10111101, B01000010, B00111100};
  byte uzgunYuz[8] = {B00111100,B01000010,B10100101,B10000001,B10011001,B10100101,B01000010,B00111100};
void setup() {
  lc.shutdown(0,false);
  lc.setIntensity(0,8);
  lc.clearDisplay(0);
  Serial.begin(9600);
  
}
void loop() {
 if (Serial.available() > 0) {
    char gelenVeri = Serial.read(); 
    
    if (gelenVeri == 'M') {
      for (int i = 0; i < 8; i++) {
        lc.setRow(0, i, gozlukluYuz[i]); 
     } 
   }
    else if (gelenVeri == 'G') {
      for (int i = 0; i < 8; i++) {
        lc.setRow(0, i, gulenYuz[i]);
      }
    } 
    else if (gelenVeri == 'U') {
      for (int i = 0; i < 8; i++) {
        lc.setRow(0, i, uzgunYuz[i]);
      }
    } 
    else if (gelenVeri == 'N') {
      for (int i = 0; i < 8; i++) {
        lc.setRow(0, i, normalYuz[i]);
      }
    }
  } 
} 