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
  if(digitalRead(pen_down_pin) == HIGH){ // Data captured only when button is pressed
    digitalWrite(ledPin, HIGH); // visual indication (button has been pressed)
    Serial.println(analogRead(shoulder_pin));
    Serial.println(analogRead(elbow_pin));
    //delay(1000); // Controls flow of captured datapoints
  }
  else{
    digitalWrite(ledPin, LOW);// visual indication (button has NOT been pressed)
  }

}
