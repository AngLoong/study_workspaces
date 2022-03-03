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

void CallPythonFunc(void)
{
    Py_Initialize();
    if(!Py_IsInitialized()) {
       std::cout<<"python init fail" <<std::endl;
    }
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./script')");
    PyRun_SimpleString("sys.path.append('./')");
    PyObject* pModule = PyImport_ImportModule("py_function");
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
    //Py_Finalize();会造成二次调用该函数时冲突，三次调用闪退的问题
    std::cout<<"python call finished"<<std::endl;

}

void MainWindow::on_pushButton_clicked()
{
    /***
    Py_Initialize();
    if(!Py_IsInitialized()) {
       std::cout<<"python init fail" <<std::endl;
    }
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./script')");
    PyRun_SimpleString("sys.path.append('./')");
    PyObject* pModule = PyImport_ImportModule("py_function");
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
    std::cout<<"python call finished"<<std::endl;
    ***/
    CallPythonFunc();
}

