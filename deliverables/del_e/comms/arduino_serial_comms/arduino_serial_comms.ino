int pin_shoulder = A0;
int pin_elbow = A1;

// Reused from lab6vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
String inputString = ""; // initialisation of input string variable
bool stringComplete = false; // used to notify code when string transmission is complete
// reused from lab 6^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

void setup() {
  pinMode(pin_shoulder, INPUT);
  pinMode(pin_elbow, INPUT);
  Serial.begin(9600); // start serial communications
  while(!Serial){ // wait for reial communications between arduino and pi to be established
    ;
  }

}

void loop() {
  if(stringComplete){
    if(inputString.startsWith("Status")){
      Serial.println(analogRead(pin_shoulder));
      Serial.println(analogRead(pin_elbow));
      stringComplete = false;
    }
  }

}

// Reused from lab6vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
void serialEvent(){ // function that handles incoming transmissions
  while(Serial.available()){ // while transmission is taking place
    char inChar = (char)Serial.read(); // cast input byte string to character
    inputString += inChar; // append each incoming character to input string var
    if(inChar == '\n'){ // if new line character is encountered
      stringComplete = true; // flag code that incoming transmiossion is complete
    }
  }
}
// reused from lab 6^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
