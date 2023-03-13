#ifndef DBCREDENTIALS_H
#define DBCREDENTIALS_H

#include <QString>

class DBCredentials
{
public:
    DBCredentials(QString ip, QString user, QString pass, QString dbname);
    QString host;
    QString password;
    QString user;
    QString dbname;
};

#endif // DBCREDENTIALS_H
