#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    DatabaseService *db_service = new DatabaseService();
    loginscreen *logindialog = new loginscreen(this);
    logindialog->show();
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_refreshButton_clicked()
{

}

