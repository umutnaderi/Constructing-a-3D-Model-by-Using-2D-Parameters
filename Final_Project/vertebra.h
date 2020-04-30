#ifndef VERTEBRA_H
#define VERTEBRA_H

#pragma once
#include <edge.h>
#include <vertex.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <QtCore/qmath.h>
#define PI 3.14159265
using namespace std;

class Vertebrae {
public:
    vector <Edge> Vector_Edges;
    vector <Vertex> Vector_Vertex_Lateral;
    vector <Vertex> Vector_Vertex_Frontal;
    double rot_x;
    double rot_y;
    double rot_z;
    double rot_x_top;
    double rot_y_top;
    double rot_z_top;
    double rot_x_bottom;
    double rot_y_bottom;
    double rot_z_bottom;
    double cen_x;
    double cen_y;
    double cen_z;
    double cen_x_top;
    double cen_y_top;
    double cen_z_top;
    double cen_x_bottom;
    double cen_y_bottom;
    double cen_z_bottom;
    Vertebrae() {
        rot_x_top = 0.0; rot_x_bottom = 0.0; rot_y_top = 0.0; rot_y_bottom; rot_z_top = 0.0; rot_z_bottom = 0.0;
        rot_x = 0.0; rot_y = 0.0; rot_y = 0.0;
        Vertex vL1,vL2,vL3,vL4;
        Vertex vF1,vF2,vF3,vF4;

        Edge e1,e2,e3;
        int a1,a2,a3,a4;

        Vector_Edges.push_back(e1);
        Vector_Edges.push_back(e2);
        Vector_Edges.push_back(e3);
        //Vector_Edges.push_back(e4);

        Vector_Vertex_Lateral.push_back(vL1);
        Vector_Vertex_Lateral.push_back(vL2);
        Vector_Vertex_Lateral.push_back(vL3);
        Vector_Vertex_Lateral.push_back(vL4);

        Vector_Vertex_Frontal.push_back(vF1);
        Vector_Vertex_Frontal.push_back(vF2);
        Vector_Vertex_Frontal.push_back(vF3);
        Vector_Vertex_Frontal.push_back(vF4);

        width = 0;
        height = 0;
        length = 0;
        width_top = 0;
        height_top = 0;
        length_top = 0;
        width_bottom = 0;
        height_bottom = 0;
        length_bottom = 0;
    }

    int sqr(int x){
        return x*x;
    }

    void calcCenter(){
        int difXTop = getAvg(Vector_Vertex_Frontal.at(1).getx(),Vector_Vertex_Frontal.at(0).getx());
        int difZTop = getAvg(Vector_Vertex_Frontal.at(1).getz(),Vector_Vertex_Frontal.at(0).getz());
        int difXBot = getAvg(Vector_Vertex_Frontal.at(3).getx(),Vector_Vertex_Frontal.at(2).getx());
        int difZBot = getAvg(Vector_Vertex_Frontal.at(3).getz(),Vector_Vertex_Frontal.at(2).getz());
        int difYTop = getAvg(Vector_Vertex_Lateral.at(1).gety(),Vector_Vertex_Lateral.at(0).gety());
        int difYBot = getAvg(Vector_Vertex_Lateral.at(3).gety(),Vector_Vertex_Lateral.at(2).gety());
        cen_x = getAvg(difXTop,difXBot);
        cen_y = getAvg(difYTop,difYBot);
        cen_z = getAvg(difZTop,difZBot);
    }

    int getCenXTop(){
         int cen_x_top = getAvg(Vector_Vertex_Frontal.at(0).getx(),Vector_Vertex_Frontal.at(1).getx());
         cout << Vector_Vertex_Frontal.at(0).getx() << " " << Vector_Vertex_Frontal.at(1).getx() << endl;
         return cen_x_top;
    }

    int getCenXBottom(){
         int cen_x_bottom = getAvg(Vector_Vertex_Frontal.at(3).getx(),Vector_Vertex_Frontal.at(2).getx());
         return cen_x_bottom;
    }

    int getCenX(){
        int difXTop = getAvg(Vector_Vertex_Frontal.at(1).getx(),Vector_Vertex_Frontal.at(0).getx());
        int difXBot = getAvg(Vector_Vertex_Frontal.at(3).getx(),Vector_Vertex_Frontal.at(2).getx());
        cen_x = getAvg(difXTop,difXBot);
        return cen_x;
    }

    int getCenY(){
        int difYTop = getAvg(Vector_Vertex_Lateral.at(1).gety(),Vector_Vertex_Lateral.at(0).gety());
        int difYBot = getAvg(Vector_Vertex_Lateral.at(3).gety(),Vector_Vertex_Lateral.at(2).gety());
        cen_y = getAvg(difYTop,difYBot);
        return cen_y;
    }

    int getCenYTop(){
        int cen_y_top = getAvg(Vector_Vertex_Lateral.at(1).gety(),Vector_Vertex_Lateral.at(0).gety());
        return cen_y_top;
    }

    int getCenYBottom(){
        int cen_y_bottom = getAvg(Vector_Vertex_Lateral.at(3).gety(),Vector_Vertex_Lateral.at(2).gety());
        return cen_y_bottom;
    }

    int getCenZ(){
        int difZTop = getAvg(Vector_Vertex_Frontal.at(1).getz(),Vector_Vertex_Frontal.at(0).getz());
        int difZBot = getAvg(Vector_Vertex_Frontal.at(3).getz(),Vector_Vertex_Frontal.at(2).getz());
        cen_z = getAvg(difZTop,difZBot);
        return cen_z;
    }

    int getCenZTop(){
        int cen_z_top = getAvg(Vector_Vertex_Frontal.at(1).getz(),Vector_Vertex_Frontal.at(0).getz());
        return cen_z_top;
    }

    int getCenZBottom(){
        int cen_z_bottom = getAvg(Vector_Vertex_Frontal.at(3).getz(),Vector_Vertex_Frontal.at(2).getz());
        return cen_z_bottom;
    }

    float getAvg(float x, float y){
        return (x + y)/2;
    }

    float getFrontalRotationTop(){
       float edge1 = atan( ( (double) ( Vector_Vertex_Frontal.at(1).getz() - Vector_Vertex_Frontal.at(0).getz() ) / ( Vector_Vertex_Frontal.at(1).getx() - Vector_Vertex_Frontal.at(0).getx() )) ) * 180 / PI;
       rot_y_top = edge1;
       return rot_y_top;
    }

    float getFrontalRotationBottom(){
       float edge2 = atan( ( (double) ( Vector_Vertex_Frontal.at(3).getz() - Vector_Vertex_Frontal.at(2).getz() ) / ( Vector_Vertex_Frontal.at(3).getx() - Vector_Vertex_Frontal.at(2).getx() )) ) * 180 / PI;
       rot_y_bottom = edge2;
       return rot_y_bottom;
    }

    float getLateralRotationTop(){
        float edge1 = atan( ( (double) ( Vector_Vertex_Lateral.at(1).getz() - Vector_Vertex_Lateral.at(0).getz() ) / ( Vector_Vertex_Lateral.at(1).gety() - Vector_Vertex_Lateral.at(0).gety() )) ) * 180 / PI;
        rot_x_top = edge1;
        return rot_x_top;
    }

    float getLateralRotationBottom(){
        float edge2 = atan( ( (double) ( Vector_Vertex_Lateral.at(3).getz() - Vector_Vertex_Lateral.at(2).getz() ) / ( Vector_Vertex_Lateral.at(3).gety() - Vector_Vertex_Lateral.at(2).gety() )) ) * 180 / PI;
        rot_x_bottom = edge2;
        return rot_x_bottom;
    }

    float getWidthTop(){
        float instance1 = sqrt(sqr(abs(Vector_Vertex_Lateral.at(0).gety() - Vector_Vertex_Lateral.at(1).gety())) + sqr(abs(Vector_Vertex_Lateral.at(0).getz() - Vector_Vertex_Lateral.at(1).getz())));
        width_top = instance1;
        return width_top;
    }

    float getWidthBottom(){
        float instance2 = sqrt(sqr(abs(Vector_Vertex_Lateral.at(2).gety() - Vector_Vertex_Lateral.at(3).gety())) + sqr(abs(Vector_Vertex_Lateral.at(2).getz() - Vector_Vertex_Lateral.at(3).getz())));
        width_bottom = instance2;
        return width_bottom;
    }

    float getLengthTop(){
        float length = sqrt(sqr(abs(Vector_Vertex_Frontal.at(0).getx() - Vector_Vertex_Frontal.at(1).getx())) + sqr(abs(Vector_Vertex_Frontal.at(0).getz() - Vector_Vertex_Frontal.at(1).getz())));
        length_top = length;
        return length_top;
    }

    float getLengthBottom(){
        float length = sqrt(sqr(abs(Vector_Vertex_Frontal.at(2).getx() - Vector_Vertex_Frontal.at(3).getx())) + sqr(abs(Vector_Vertex_Frontal.at(2).getz() - Vector_Vertex_Frontal.at(3).getz())));
        length_bottom = length;
        return length_bottom;

    }

    float getHeight(){
        float height = getCenZTop() - getCenZBottom();
        return height;
    }



private:
    double width;
    double height;
    double length;
    double width_top;
    double height_top;
    double length_top;
    double width_bottom;
    double height_bottom;
    double length_bottom;



    class position {
        position() { x = 0; y = 0; z = 0; }
        ~position();
        double x;
        double y;
        double z;

    };

};








#endif // VERTEBRA_H
