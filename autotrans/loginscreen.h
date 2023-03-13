#ifndef LOGINSCREEN_H
#define LOGINSCREEN_H

#include <QDialog>
#include <QMessageBox>
#include "databaseservice.h"
#include "dbcredentials.h"

namespace Ui {
class loginscreen;
}

class loginscreen : public QDialog
{
    Q_OBJECT

public:
    explicit loginscreen(QWidget *parent = nullptr);
    ~loginscreen();
    void setDbService(DatabaseService *db_service);

private slots:
    void on_pushButton_clicked();

private:
    Ui::loginscreen *ui;
    DatabaseService *db_service;
};

#endif // LOGINSCREEN_H
