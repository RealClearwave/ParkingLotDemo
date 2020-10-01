#include <HCSR04.h>

UltraSonicDistanceSensor distanceSensor1(11, 12);
UltraSonicDistanceSensor distanceSensor2(51, 50);
UltraSonicDistanceSensor distanceSensor3(2, 3);
UltraSonicDistanceSensor distanceSensor4(47, 46);
UltraSonicDistanceSensor distanceSensor5(49, 48);  
UltraSonicDistanceSensor distanceSensor6(53, 52);

bool parked[7] = {false,false,false,false,false,false,false};
void check_park(){
  if (distanceSensor1.measureDistanceCm() < 7) parked[1] = true; else parked[1] = false;
  if (distanceSensor2.measureDistanceCm() < 7) parked[2] = true; else parked[2] = false;
  if (distanceSensor3.measureDistanceCm() < 7) parked[3] = true; else parked[3] = false;
  if (distanceSensor4.measureDistanceCm() < 7) parked[4] = true; else parked[4] = false;
  if (distanceSensor5.measureDistanceCm() < 7) parked[5] = true; else parked[5] = false;
  if (distanceSensor6.measureDistanceCm() < 7) parked[6] = true; else parked[6] = false;
}

void setup () {
    Serial.begin(9600);  // We initialize serial connection so that we could print values from sensor.
}

void loop () {
    // Every 500 miliseconds, do a measurement using the sensor and print the distance in centimeters.
    check_park();
    for (int i=1;i<=6;i++)
      if (parked[i])
        Serial.println(i);
}
