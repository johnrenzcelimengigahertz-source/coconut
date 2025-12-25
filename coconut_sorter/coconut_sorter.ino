// ===============================
// COCONUT SORTER - ARDUINO SIDE
// ===============================

// ----- PIN DEFINITIONS -----
#define SENSOR_1 2        // Object detection sensor
#define SENSOR_2 3        // Coconut verification sensor

#define REJECT_EXTEND 8   // Reject cylinder extend
#define REJECT_RETRACT 9  // Reject cylinder retract
#define SMASH_PIN 10      // Smash actuator

// ----- TIMING -----
#define DEBOUNCE_DELAY 300
#define SMASH_TIME 1200
#define REJECT_TIME 700

void setup() {
  pinMode(SENSOR_1, INPUT);
  pinMode(SENSOR_2, INPUT);

  pinMode(REJECT_EXTEND, OUTPUT);
  pinMode(REJECT_RETRACT, OUTPUT);
  pinMode(SMASH_PIN, OUTPUT);

  digitalWrite(REJECT_EXTEND, LOW);
  digitalWrite(REJECT_RETRACT, LOW);
  digitalWrite(SMASH_PIN, LOW);

  Serial.begin(9600);
}

// ======================================================
// MAIN LOOP
// ======================================================
void loop() {

  // -------- PHASE 1: OBJECT DETECTED --------
  if (digitalRead(SENSOR_1) == HIGH) {
    Serial.println("OBJECT_DETECTED");
    delay(DEBOUNCE_DELAY);

    // Wait for Raspberry Pi decision
    while (!Serial.available());

    String decision = Serial.readStringUntil('\n');
    decision.trim();

    if (decision == "NONCOCONUT") {
      rejectObject();
    }
    // If coconut, do nothing and let it move forward
  }

  // -------- PHASE 2: COCONUT AT SMASH POINT --------
  if (digitalRead(SENSOR_2) == HIGH) {
    Serial.println("COCONUT_AT_SENSOR2");
    delay(DEBOUNCE_DELAY);

    while (!Serial.available());

    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command.startsWith("SMASH")) {
      smashCoconut();
    }
  }
}

// ======================================================
// ACTUATORS
// ======================================================
void rejectObject() {
  digitalWrite(REJECT_EXTEND, HIGH);
  delay(REJECT_TIME);
  digitalWrite(REJECT_EXTEND, LOW);

  digitalWrite(REJECT_RETRACT, HIGH);
  delay(REJECT_TIME);
  digitalWrite(REJECT_RETRACT, LOW);
}

void smashCoconut() {
  digitalWrite(SMASH_PIN, HIGH);
  delay(SMASH_TIME);
  digitalWrite(SMASH_PIN, LOW);
}
