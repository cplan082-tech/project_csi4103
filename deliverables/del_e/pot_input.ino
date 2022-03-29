const int shoulder_pin = A0; // Any analog pin can be used  
const int elbow_pin = A1; // Any analog pin can be used

void setup() {
  // put your setup code here, to run once:
  pinMode(shoulder_pin, INPUT);
  pinMode(elbow_pin, INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(shoulder_pin); // Send value of Shoulder Pot
  Serial.println(elbow_pin); // Send value of Elbow Pot
  delay(1000);
}
