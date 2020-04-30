#ifndef VERTEX_H
#define VERTEX_H

class Vertex{
    double x;
    double y;
    double z;
public:
     Vertex() { x = 0; y = 0; z = 0;}
        double getx(){return x;}
        double gety(){return y;}
        double getz(){return z;}

        void setx(double x){this->x = x;}
        void sety(double y){this->y = y;}
        void setz(double z){this->z = z;}

        ~Vertex(){}




};

#endif // VERTEX_H
