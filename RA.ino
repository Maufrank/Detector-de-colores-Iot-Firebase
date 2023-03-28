#include <Servo.h>
#include "Ticker.h";
const int rojo = A2;
const int verde = A1;
const int azul = A0;
int pinServo = 3;
Servo servo;
String opcion, secA, secB, estadoServo;
int op, separador, svmMove, rojol, verdel, azull;
int NA = -1;
int antRojo = 0;
int antVerde = 0;
int antAzul = 0;
String estado = "m";

void principal(){
	rojol = analogRead(rojo)/4;
	verdel = analogRead(verde)/4;
	azull = analogRead(azul)/4;
	opcion = Serial.readString();
	separador = opcion.indexOf(':');
	secA = opcion.substring(0, separador);
	op = secA.toInt();
	secB = opcion.substring(separador+1);
	svmMove = secB.toInt();
	switch (op){
		case 1:
			if(secB == "m"){
				estado = "m";
			}
			else{
				estado = "a";
			}
		case 2:
			Serial.println(estadoServo);
			break;
		case 3:
			color(NA, NA, NA, secB);
			break;
	}
}

Ticker tiempo1(principal, 1000);
Ticker tiempo2(lectura, 1000);

void setup(){
	Serial.begin(9600);
	servo.attach(pinServo);
	tiempo1.start();
	tiempo2.start();
}

void loop(){
	tiempo1.update();
	tiempo2.update();
}


void color(int rojo, int verde, int azul, String col){
	if((rojo > 100 && rojo < 200 && verde > 50 && verde < 100 && azul > 50 && azul < 100) || col == "rojo"){
		servo.write(0);
		estadoServo = "rojo";
		Serial.println("Rojo:"+String(rojol)+"|Verde:"+String(verdel)+"|Azul:"+String(azull)+"|color:rojo");
	}else if((rojo > 50 && rojo < 100 && verde > 100 && verde < 200 && azul > 50 && azul < 100) || col == "verde"){
		servo.write(180);
		estadoServo = "verde";
		Serial.println("Rojo:"+String(rojol)+"|Verde:"+String(verdel)+"|Azul:"+String(azull)+"|color:verde");
	}else if((rojo > 50 && rojo < 100 && verde > 50 && verde < 100 && azul > 100 && azul < 200) ||col == "azul"){
		servo.write(120);
		estadoServo = "azul";
		Serial.println("Rojo:"+String(rojol)+"|Verde:"+String(verdel)+"|Azul:"+String(azull)+"|color:azul");
	}else if((rojo > 0 && rojo < 50 && verde > 0 && verde < 50 && azul > 0 && azul < 50) || col == "blanco"){
		servo.write(60);
		estadoServo = "blanco";
		Serial.println("Rojo:"+String(rojol)+"|Verde:"+String(verdel)+"|Azul:"+String(azull)+"|color:blanco");
	}else if((rojo > 100 && rojo < 200 && verde > 100 && verde < 200 && azul > 50 && azul < 100) || col == "naranja" ){
		servo.write(90);
		estadoServo = "naranja";
		Serial.println("Rojo:"+String(rojol)+"|Verde:"+String(verdel)+"|Azul:"+String(azull)+"|color:naranja");
	}
}

void lectura(){
	if (estado == "a"){
	rojol = analogRead(rojo)/4;
	verdel = analogRead(verde)/4;
	azull = analogRead(azul)/4;
	if(rojol != antRojo && verdel != antVerde && azull != antAzul){
		color(rojol, verdel, azull, "0");
		antRojo = rojol;
		antVerde = verdel;
		antAzul = azull;
	}
	}
}
