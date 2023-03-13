QT       += core gui sql

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    databaseservice.cpp \
    dbcredentials.cpp \
    loginscreen.cpp \
    main.cpp \
    mainwindow.cpp

HEADERS += \
    databaseservice.h \
    dbcredentials.h \
    dbmodels.h \
    loginscreen.h \
    mainwindow.h

FORMS += \
    loginscreen.ui \
    mainwindow.ui


# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

INCLUDEPATH += $$PWD/.
DEPENDPATH += $$PWD/.
