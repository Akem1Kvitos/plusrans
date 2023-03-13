#ifndef DATABASESERVICE_H
#define DATABASESERVICE_H

#include <QList>
#include <QSqlDatabase>
#include "dbmodels.h"
#include "dbcredentials.h"


class DatabaseService
{
public:
    DatabaseService();

    int connect(DBCredentials creds);

    QList<Strahovka> select_from_srtahovki();
    int select_from_voditeli();
    int select_from_tehosmotri();

    int insert_into_strahovki();
    int insert_into_voditeli();
    int insert_into_tehosmotri();

    int update_strahovki();
    int update_voditeli();
    int update_tehosmotri();

private:
    QSqlDatabase m_db;
};

#endif // DATABASESERVICE_H
