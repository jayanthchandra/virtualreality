import SimpleOpenNI.*;
import processing.opengl.*;
SimpleOpenNI kinect;

void setup()
{
  kinect=new SimpleOpenNI(this);
  size(1024,768,OPENGL);
  kinect.enableDepth();
}

void draw()
{
  background(0);
  kinect.update();
  translate(width/2,height/2,-1000);
  rotateX(radians(180));
  PVector[] position=kinect.depthMapRealWorld();
 float angle=map(mouseX,0,1024,0,360);
 rotateY(radians(angle));
  for(int i=0;i<position.length;i+=10)
  {
    stroke(255);
    PVector pos=position[i];
    point(pos.x,pos.y,pos.z);
  }
}
  
