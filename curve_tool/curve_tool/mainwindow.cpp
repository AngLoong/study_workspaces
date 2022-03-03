#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include "Python.h"
#include <iostream>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    Py_Initialize();
    if(!Py_IsInitialized()) {
       std::cout<<"python init fail" <<std::endl;
    }
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./script')");
    PyObject* pModule = PyImport_ImportModule("mrs_curve_fit");
    if(pModule == NULL) {
        std::cout<<"module not found"<< std::endl;
        return ;
    }
    PyObject* pFunc = PyObject_GetAttrString(pModule, "test");
    if(!pFunc || !PyCallable_Check(pFunc)) {
        std::cout<<"not found function "<<std::endl;
        return;
    }
    PyObject_CallObject(pFunc,NULL);
    Py_Finalize();
}

