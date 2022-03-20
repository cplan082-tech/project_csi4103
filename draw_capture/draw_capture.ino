const int shoulder_pin = A0;
const int elbow_pin = A1;
const int pen_down_pin = 3; 
const int ledPin =  13; //https://www.arduino.cc/en/Tutorial/BuiltInExamples/Button


void setup() {
  pinMode(shoulder_pin, INPUT);
  pinMode(elbow_pin, INPUT);
  pinMode(pen_down_pin, INPUT);
  pinMode(ledPin, OUTPUT); //https://www.arduino.cc/en/Tutorial/BuiltInExamples/Button
  Serial.begin(9600);

}


void loop() {
  if(digitalRead(pen_down_pin) == HIGH){
    digitalWrite(ledPin, HIGH); // visual indication (if statment has been reached)
    Serial.println(analogRead(shoulder_pin));
    Serial.println(analogRead(elbow_pin));
  }
  else{
    digitalWrite(ledPin, LOW);
  }

}
