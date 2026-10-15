// Declare an array reference for Balloon objects
Balloon[] b;

class Balloon {
  // Attributes with explicit data types
  int x;
  int y;
  int r;

  // Constructor with 'this' keyword
  Balloon(int x, int y, int r) {
    this.x = x;
    this.y = y;
    this.r = r;
  }

  void show() {
    stroke(40);
    strokeWeight(2);
    line(this.x, this.y, this.x, this.y + 100);
    fill(255, 120, 100);
    ellipse(this.x, this.y, this.r, this.r);
  }

  void move() {
    this.y = this.y - 3;
    // Reset position when balloon leaves the screen
    if (this.y < -this.r - 100) {
      this.y = height + 50;
    }
  }
}

void setup() {
  size(600, 600);
  
  // Allocate fixed-size array of 5 elements
  b = new Balloon[5];
  
  // Initialize objects with type-casted random coordinates
  for (int i = 0; i < b.length; i = i + 1) {
    int rx = (int) random(80, 520);
    int ry = (int) random(400, 650);
    int rr = (int) random(40, 70);
    b[i] = new Balloon(rx, ry, rr);
  }
}

void draw() {
  background(240);
  
  // Loop through array of objects
  for (int i = 0; i < b.length; i = i + 1) {
    b[i].show();
    b[i].move();
  }
}
