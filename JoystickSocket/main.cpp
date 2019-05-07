#include "mainwindow.h"
#include <QApplication>
#include <QProcess>
#include <QDebug>
#include <QTextStream>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    QProcess p;
    QString ba;
    QString exec = "python3";
    QStringList params;
    params << "client.py";
    p.start(exec, params);

    while(p.waitForFinished(-1)) {

        //p.waitForFinished(-1);// sets current thread to sleep and waits for pingProcess end

        QString output(p.readAllStandardOutput());
        QTextStream out(stdout);
        out << output;

    }



    return a.exec();
}
