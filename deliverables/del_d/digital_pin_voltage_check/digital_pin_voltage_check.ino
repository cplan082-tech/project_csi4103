const int analgo_read_pin = A3;

void setup() {
  pinMode(analgo_read_pin, INPUT);
  Serial.begin(9600);

}

void loop() {
  Serial.println(analogRead(analgo_read_pin));
  delay(1000);

}
