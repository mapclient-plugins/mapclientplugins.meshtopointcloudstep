# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statisticswidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Statistics(object):
    def setupUi(self, Statistics):
        if not Statistics.objectName():
            Statistics.setObjectName(u"Statistics")
        Statistics.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Statistics)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(Statistics)
        self.labelTitle.setObjectName(u"labelTitle")

        self.verticalLayout.addWidget(self.labelTitle)

        self.frame = QFrame(Statistics)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelComponent1 = QLabel(self.frame)
        self.labelComponent1.setObjectName(u"labelComponent1")

        self.gridLayout.addWidget(self.labelComponent1, 0, 0, 1, 1)

        self.lineEditComponent1Min = QLineEdit(self.frame)
        self.lineEditComponent1Min.setObjectName(u"lineEditComponent1Min")
        self.lineEditComponent1Min.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditComponent1Min, 0, 1, 1, 1)

        self.lineEditComponent1Max = QLineEdit(self.frame)
        self.lineEditComponent1Max.setObjectName(u"lineEditComponent1Max")
        self.lineEditComponent1Max.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditComponent1Max, 0, 2, 1, 1)

        self.labelComponent2 = QLabel(self.frame)
        self.labelComponent2.setObjectName(u"labelComponent2")

        self.gridLayout.addWidget(self.labelComponent2, 1, 0, 1, 1)

        self.lineEditComponent2Min = QLineEdit(self.frame)
        self.lineEditComponent2Min.setObjectName(u"lineEditComponent2Min")
        self.lineEditComponent2Min.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditComponent2Min, 1, 1, 1, 1)

        self.lineEditComponent2Max = QLineEdit(self.frame)
        self.lineEditComponent2Max.setObjectName(u"lineEditComponent2Max")
        self.lineEditComponent2Max.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditComponent2Max, 1, 2, 1, 1)

        self.labelComponent3 = QLabel(self.frame)
        self.labelComponent3.setObjectName(u"labelComponent3")

        self.gridLayout.addWidget(self.labelComponent3, 2, 0, 1, 1)

        self.lineEditComponent3Min = QLineEdit(self.frame)
        self.lineEditComponent3Min.setObjectName(u"lineEditComponent3Min")
        self.lineEditComponent3Min.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditComponent3Min, 2, 1, 1, 1)

        self.lineEditComponent3Max = QLineEdit(self.frame)
        self.lineEditComponent3Max.setObjectName(u"lineEditComponent3Max")
        self.lineEditComponent3Max.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditComponent3Max, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 118, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

#if QT_CONFIG(shortcut)
        self.labelComponent3.setBuddy(self.lineEditComponent3Min)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Statistics)

        QMetaObject.connectSlotsByName(Statistics)
    # setupUi

    def retranslateUi(self, Statistics):
        Statistics.setWindowTitle(QCoreApplication.translate("Statistics", u"Statistics", None))
        self.labelTitle.setText(QCoreApplication.translate("Statistics", u"Mesh bounds", None))
        self.labelComponent1.setText(QCoreApplication.translate("Statistics", u"Component 1:", None))
#if QT_CONFIG(tooltip)
        self.lineEditComponent1Min.setToolTip(QCoreApplication.translate("Statistics", u"Minimum value for compoent 1", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEditComponent1Max.setToolTip(QCoreApplication.translate("Statistics", u"Maximum value for component 1", None))
#endif // QT_CONFIG(tooltip)
        self.labelComponent2.setText(QCoreApplication.translate("Statistics", u"Component 2:", None))
#if QT_CONFIG(tooltip)
        self.lineEditComponent2Min.setToolTip(QCoreApplication.translate("Statistics", u"Minimum value for compoent 2", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEditComponent2Max.setToolTip(QCoreApplication.translate("Statistics", u"Maximum value for component 2", None))
#endif // QT_CONFIG(tooltip)
        self.labelComponent3.setText(QCoreApplication.translate("Statistics", u"Component 3:", None))
#if QT_CONFIG(tooltip)
        self.lineEditComponent3Min.setToolTip(QCoreApplication.translate("Statistics", u"Minimum value for compoent 3", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEditComponent3Max.setToolTip(QCoreApplication.translate("Statistics", u"Maximum value for component 3", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

