#ifndef DBMODELS_H
#define DBMODELS_H

#endif // DBMODELS_H

#include <QString>
#include <QDate>


struct Strahovka
{
    int id;
    QString garage_id;
    QString auto_mark;
    QString gos_auto_nomer;
    QString num_strah_svet;
    QDate data_vidachi;
    QString srok_strahovki;
    QDate zastrah_po;
    QString note;
};


struct Voditeli
{
    int id;
    QDate working_from;
    QString full_name;
    QString a_k;
    QDate date_of_birth;
    QString v_u_number;
    QDate expire_date;
    QString category;
    QString med_nomer;
    QDate med_expire;
    QString med_category;
    QString note;
    QString d_category;
    QString phone;
    int med_leg;
    int blood;
    int gazeli;
    int soc;
    int score;
    int maz;
    int bus;
    int razryad;
    int klass;
};


struct Tehosmotr
{
    int id;
    int garage_num;
    QDate prohojdenie_tex_osmotra;
    QDate expire_date;
    int razresheno_na_dostup;
    int raznica;
    QString spisanie;
};
