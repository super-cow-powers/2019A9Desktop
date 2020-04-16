
// the setup routine runs once when you press reset:
void setup() {
  //Standard Baud
  Serial.begin(9600);
}

int periodB = 10; //milliseconds
unsigned long time_nowB = 0;

float output = -20;
char* out_types[] = {"mv","v","a","ma","hz"};
const int num_types = 5;
int current_type = 0;

char seroutput[20];
void loop() {

  if(millis() >= time_nowB + periodB){ //Output val every 10mS
    sprintf(seroutput, "%d.%d %s\n\r", (int)(output),(int)((abs(output)-abs((int)output))*100) , out_types[current_type]);
    time_nowB += periodB;
    Serial.print(seroutput);
    output = output + 0.01;
    
    if (output > 20){
      output = -20;
      current_type++;
    
    if (current_type == num_types){
      current_type = 0;
    }
    }
  }
  
}
