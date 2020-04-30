#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <QMainWindow>

using namespace cv;
using namespace std;

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:

    void on_actLateral_triggered();
    void on_actlFront_triggered();
    void showMousePosition(QPoint& pos);
    void updateImagePoint(QPoint& pos);


    void on_btnBack_clicked();

    void on_btnNext_clicked();

    void createOutput();

    void on_btnDone_clicked();

    void on_btnReset_clicked();

private:
    void keyPressEvent(QKeyEvent *);
    Ui::MainWindow *ui;
    void updateImage();
    cv::Mat displayImage;
    vector<QPoint> pointSequence;
    cv::Mat defaultImage;
};

#endif // MAINWINDOW_H
