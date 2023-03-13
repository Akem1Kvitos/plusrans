#include "databaseservice.h"
#include <QSqlQuery>

DatabaseService::DatabaseService()
{

}

int DatabaseService::connect(DBCredentials creds)
{
    this->m_db = QSqlDatabase::addDatabase("QMYSQL");
    m_db.setHostName(creds.host);
    m_db.setDatabaseName(creds.dbname);
    m_db.setUserName(creds.user);
    m_db.setPassword(creds.password);
    bool ok = m_db.open();
    return ok ? 0 : 1;
}

QList<Strahovka> DatabaseService::select_from_srtahovki()
{
    QSqlQuery query;
    query.exec("select * from strahovki;");

    auto response = QList<Strahovka> {};

    while (query.next())
    {
        Strahovka s;
        s.id = query.value(0).toInt();
        s.garage_id = query.value(1).toString();
        s.auto_mark = query.value(2).toString();
        s.gos_auto_nomer = query.value(3).toString();
        s.num_strah_svet = query.value(4).toString();
        s.data_vidachi = query.value(5).toDate();
        s.srok_strahovki = query.value(6).toString();
        s.zastrah_po = query.value(7).toDate();
        s.note = query.value(8).toString();
    }

    return response;
}

int DatabaseService::select_from_voditeli()
{

}

int DatabaseService::select_from_tehosmotri()
{

}

int DatabaseService::insert_into_strahovki()
{

}

int DatabaseService::insert_into_voditeli()
{

}

int DatabaseService::insert_into_tehosmotri()
{

}

int DatabaseService::update_strahovki()
{

}
int DatabaseService::update_voditeli()
{

}
int DatabaseService::update_tehosmotri()
{

}
