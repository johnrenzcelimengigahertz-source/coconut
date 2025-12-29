#define SENSOR_PIN 2
#define SOLENOID_PIN 8

void setup() {
  Serial.begin(9600);
  pinMode(SENSOR_PIN, INPUT);
  pinMode(SOLENOID_PIN, OUTPUT);
  digitalWrite(SOLENOID_PIN, LOW);
}

void loop() {
  if (digitalRead(SENSOR_PIN) == HIGH) {
    Serial.println("DETECTED");
    delay(300);
  }

  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "TAP") {
      digitalWrite(SOLENOID_PIN, HIGH);
      delay(80); // light tap
      digitalWrite(SOLENOID_PIN, LOW);
    }
  }
}
