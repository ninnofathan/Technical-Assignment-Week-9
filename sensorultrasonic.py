from gpiozero import DistanceSensor # Import DistanceSensor(HC-SR04) dari gpiozero library.
import time

ultrasonic = DistanceSensor(echo=21,trigger=20) # Menetapkan pin untuk echo dan trigger sebagai parameters untuk Ultrasonic Sensor

def hcr() :
  sensor = round(ultrasonic.distance * 100,3)
  print(f"{sensor} cm")
  time.sleep(0.2)
  return sensor