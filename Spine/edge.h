#ifndef EDGE_H
#define EDGE_H

class Edge{
    double x;
    double y;
    double z;
public:
     Edge() { x = 0; y = 0; z = 0; }
        double getx(){return x;}
        double gety(){return y;}
        double getz(){return z;}

        void setx(double x){this->x = x;}
        void sety(double y){this->y = y;}
        void seyz(double z){this->z = z;}
        ~Edge(){}




};

#endif // EDGE_H
