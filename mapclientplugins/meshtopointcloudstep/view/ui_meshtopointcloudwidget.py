# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meshtopointcloudwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)

from cmlibs.widgets.basesceneviewerwidget import BaseSceneviewerWidget

class Ui_MeshToPointCloud(object):
    def setupUi(self, MeshToPointCloud):
        if not MeshToPointCloud.objectName():
            MeshToPointCloud.setObjectName(u"MeshToPointCloud")
        MeshToPointCloud.resize(800, 600)
        self.centralwidget = QWidget(MeshToPointCloud)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetZinc = BaseSceneviewerWidget(self.centralwidget)
        self.widgetZinc.setObjectName(u"widgetZinc")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widgetZinc.sizePolicy().hasHeightForWidth())
        self.widgetZinc.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.widgetZinc)

        MeshToPointCloud.setCentralWidget(self.centralwidget)

        self.retranslateUi(MeshToPointCloud)

        QMetaObject.connectSlotsByName(MeshToPointCloud)
    # setupUi

    def retranslateUi(self, MeshToPointCloud):
        MeshToPointCloud.setWindowTitle(QCoreApplication.translate("MeshToPointCloud", u"Mesh to Point Cloud", None))
    # retranslateUi

