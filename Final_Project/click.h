#ifndef CLICK_H
#define CLICK_H
#include "mainwindow.h"
#include <QObject>
#include <QWidget>
#include <QLabel>
#include <QMouseEvent>

class click : public QLabel
{
    Q_OBJECT


public:
    click(QWidget *parent = 0);
    ~click();

protected:
    void mouseMoveEvent(QMouseEvent *mouse_event);
    void mousePressEvent(QMouseEvent *mouse_event);
    //void paintEvent(QPaintEvent *);
signals:
    void sendMousePosition(QPoint&);
    void sendClickPosition(QPoint&);


};

#endif // CLICK_H
