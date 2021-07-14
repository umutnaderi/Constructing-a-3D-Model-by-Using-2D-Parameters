#ifndef MAINLABEL_H
#define MAINLABEL_H

#include <QLabel>
#include <QMouseEvent>
#include <QDebug>

class mainLabel : public QLabel
{
    Q_OBJECT
public:
    explicit mainLabel(QWidget *parent = 0);

    void mousePressEvent(QMouseEvent *ev);
    void mouseMoveEvent(QMouseEvent *ev);
    void leaveEvent(QEvent *);

    int x,y;

signals:
    void Mouse_Pressed();
    void Mouse_Pos();
    void Mouse_Left();
};

#endif // MAINLABEL_H
