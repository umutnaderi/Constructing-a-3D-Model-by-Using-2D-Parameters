#include "mainlabel.h"

mainLabel::mainLabel(QWidget *parent) :
    QLabel(parent)
{
}

void mainLabel::mousePressEvent(QMouseEvent *ev)
{
    emit Mouse_Pressed();
}

void mainLabel::mouseMoveEvent(QMouseEvent *ev){
    this->x = ev->x();
    this->y = ev->y();
    emit Mouse_Pos();
}

void mainLabel::leaveEvent(QEvent *)
{
    emit Mouse_Left();
}

