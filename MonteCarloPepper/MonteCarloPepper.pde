
float initx;
float inity;
float dirx,diry;
int speed = 55;

void setup() {
 background(10,10,10);
 size(500,500);
 initx = random(width);
 inity = random(height);
  
}


void draw(){

  
  dirx = random(1)-0.5;
  diry = random(1)-0.5;
  

  // make the bounds past the size of the canvas by a little bit. eventually it'll come back
  if(initx+dirx*speed<0 || initx+dirx*speed>width){
    initx = initx;
    inity = random(height);
  } else {
      initx+=dirx*speed;  
  }
  
    if(inity+diry*speed<0 || inity+diry*speed>height){
    inity = inity;
    initx = random(width);
  } else {
      inity+=diry*speed;  
  }
  
    noFill();
    strokeWeight(3);
    rect(0,0,width,height);
    
    // Draw dot here
    noStroke();
    fill(0,70+random(255-70),150);
    rect(initx,inity,16*random(1),16*random(1));
    
    
    // reset on mouse press
    if(mousePressed){
      fill(10,10,10);
      rect(0,0,width,height);

      rect(0,0,width,height);
      initx = mouseX;
      inity = mouseY;
      
    }
}
