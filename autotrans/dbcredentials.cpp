#include "dbcredentials.h"

DBCredentials::DBCredentials(QString ip, QString user, QString pass, QString dbname)
{
    this->host = ip + ":3306";
    this->user = user;
    this->password = pass;
    this->dbname = dbname;
}
