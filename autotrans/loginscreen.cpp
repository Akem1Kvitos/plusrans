#include "loginscreen.h"
#include "ui_loginscreen.h"

loginscreen::loginscreen(QWidget *parent):
    QDialog(parent),
    ui(new Ui::loginscreen)
{
    ui->setupUi(this);
    this->ui->ipInput->setText("");
    this->ui->userInput->setText("");
    this->ui->passwdInput->setText("");
    this->ui->dbnameInput->setText("");

    this->ui->passwdInput->setEchoMode(QLineEdit::Password);
}

void loginscreen::setDbService(DatabaseService *db_service)
{
    this->db_service = db_service;
}

loginscreen::~loginscreen()
{
    delete ui;
}

void loginscreen::on_pushButton_clicked()
{
    QString ip; QString user; QString pass; QString dbname;

    ip = this->ui->ipInput->text();
    user = this->ui->userInput->text();
    pass = this->ui->passwdInput->text();
    dbname = this->ui->dbnameInput->text();

    DBCredentials creds(ip, user, pass, dbname);
    int res = this->db_service->connect(creds);
    if (res == 0)
    {
        QMessageBox box(this);
        box.setWindowTitle("Успех");
        box.addButton(QMessageBox::Ok);
        box.setText("Вы успешно подключились");
        box.exec();
    }
    else
    {
        QMessageBox box(this);
        box.setWindowTitle("Неудача");
        box.addButton(QMessageBox::Ok);
        box.setText("Вы не смогли подключиться");
        box.exec();
    }

}

