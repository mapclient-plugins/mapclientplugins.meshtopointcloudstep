# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configurationwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from cmlibs.widgets.logspinbox import LogSpinBox

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        if not Configuration.objectName():
            Configuration.setObjectName(u"Configuration")
        Configuration.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Configuration)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutCoordinate = QHBoxLayout()
        self.horizontalLayoutCoordinate.setObjectName(u"horizontalLayoutCoordinate")
        self.labelCoordinateField = QLabel(Configuration)
        self.labelCoordinateField.setObjectName(u"labelCoordinateField")
        self.labelCoordinateField.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayoutCoordinate.addWidget(self.labelCoordinateField)

        self.comboBoxCoordinateField = QComboBox(Configuration)
        self.comboBoxCoordinateField.setObjectName(u"comboBoxCoordinateField")

        self.horizontalLayoutCoordinate.addWidget(self.comboBoxCoordinateField)


        self.verticalLayout.addLayout(self.horizontalLayoutCoordinate)

        self.horizontalLayoutSamplingDensity = QHBoxLayout()
        self.horizontalLayoutSamplingDensity.setObjectName(u"horizontalLayoutSamplingDensity")
        self.labelSamplingDensity = QLabel(Configuration)
        self.labelSamplingDensity.setObjectName(u"labelSamplingDensity")

        self.horizontalLayoutSamplingDensity.addWidget(self.labelSamplingDensity)

        self.doubleSpinBoxSamplingDensity = LogSpinBox(Configuration)
        self.doubleSpinBoxSamplingDensity.setObjectName(u"doubleSpinBoxSamplingDensity")
        self.doubleSpinBoxSamplingDensity.setDecimals(6)
        self.doubleSpinBoxSamplingDensity.setMinimum(0.000001000000000)
        self.doubleSpinBoxSamplingDensity.setMaximum(10000.000000000000000)
        self.doubleSpinBoxSamplingDensity.setSingleStep(1.000000000000000)
        self.doubleSpinBoxSamplingDensity.setValue(1.000000000000000)

        self.horizontalLayoutSamplingDensity.addWidget(self.doubleSpinBoxSamplingDensity)


        self.verticalLayout.addLayout(self.horizontalLayoutSamplingDensity)

        self.horizontalLayoutSampling1 = QHBoxLayout()
        self.horizontalLayoutSampling1.setObjectName(u"horizontalLayoutSampling1")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutSampling1.addItem(self.horizontalSpacer)

        self.pushButtonSample = QPushButton(Configuration)
        self.pushButtonSample.setObjectName(u"pushButtonSample")

        self.horizontalLayoutSampling1.addWidget(self.pushButtonSample)

        self.horizontalSpacerSampling2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutSampling1.addItem(self.horizontalSpacerSampling2)


        self.verticalLayout.addLayout(self.horizontalLayoutSampling1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Configuration)

        QMetaObject.connectSlotsByName(Configuration)
    # setupUi

    def retranslateUi(self, Configuration):
        Configuration.setWindowTitle(QCoreApplication.translate("Configuration", u"Configuration", None))
        self.labelCoordinateField.setText(QCoreApplication.translate("Configuration", u"Coordinate Field:", None))
        self.labelSamplingDensity.setText(QCoreApplication.translate("Configuration", u"Sampling Density:", None))
        self.pushButtonSample.setText(QCoreApplication.translate("Configuration", u"Sample", None))
    # retranslateUi

