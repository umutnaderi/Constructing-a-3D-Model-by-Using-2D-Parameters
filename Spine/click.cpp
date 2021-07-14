#include "click.h"

#include <QPen>
#include <QPainter>

click::click(QWidget *parent): QLabel(parent){
    this->setMouseTracking(true);
}

click::~click(){}

void click::mouseMoveEvent(QMouseEvent *mouse_event){
    QPoint mouse_pos = mouse_event->pos();

    //if(mouse_pos.x() <= this->size().width() && mouse_pos.y() <= this->size.height()){
     //   if(mouse_pos.x() >= 0 && mouse_pos.y() >= 0){
            emit sendMousePosition(mouse_pos);
      //  }
    //}
}

void click::mousePressEvent(QMouseEvent *mouse_event){
    QPainter painter(this);
    QPen pointPen(Qt::red);
    pointPen.setWidth(4);
    QPoint mouse_pos = mouse_event->pos();
    if(mouse_event->button() == Qt::LeftButton){

        painter.setPen(pointPen);
        painter.drawPoint(mouse_pos);
        emit sendClickPosition(mouse_pos);
        //cout << mouse_pos.x() << endl;


    }
}

//void click::paintEvent(QPaintEvent *){

//}

