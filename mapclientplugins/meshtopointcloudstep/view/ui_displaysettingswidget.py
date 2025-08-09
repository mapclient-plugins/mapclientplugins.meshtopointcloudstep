# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'displaysettingswidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_DisplaySettings(object):
    def setupUi(self, DisplaySettings):
        if not DisplaySettings.objectName():
            DisplaySettings.setObjectName(u"DisplaySettings")
        DisplaySettings.resize(400, 300)
        self.formLayout = QFormLayout(DisplaySettings)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBoxSurfacesVisibility = QCheckBox(DisplaySettings)
        self.checkBoxSurfacesVisibility.setObjectName(u"checkBoxSurfacesVisibility")
        self.checkBoxSurfacesVisibility.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.checkBoxSurfacesVisibility)

        self.checkBoxPointsVisibility = QCheckBox(DisplaySettings)
        self.checkBoxPointsVisibility.setObjectName(u"checkBoxPointsVisibility")
        self.checkBoxPointsVisibility.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.checkBoxPointsVisibility)

        self.labelNodeSize = QLabel(DisplaySettings)
        self.labelNodeSize.setObjectName(u"labelNodeSize")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNodeSize.sizePolicy().hasHeightForWidth())
        self.labelNodeSize.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelNodeSize)

        self.spinBoxNodeSize = QDoubleSpinBox(DisplaySettings)
        self.spinBoxNodeSize.setObjectName(u"spinBoxNodeSize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBoxNodeSize.sizePolicy().hasHeightForWidth())
        self.spinBoxNodeSize.setSizePolicy(sizePolicy1)
        self.spinBoxNodeSize.setSingleStep(0.100000000000000)
        self.spinBoxNodeSize.setValue(1.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBoxNodeSize)


        self.retranslateUi(DisplaySettings)

        QMetaObject.connectSlotsByName(DisplaySettings)
    # setupUi

    def retranslateUi(self, DisplaySettings):
        DisplaySettings.setWindowTitle(QCoreApplication.translate("DisplaySettings", u"Display Settings", None))
        self.checkBoxSurfacesVisibility.setText(QCoreApplication.translate("DisplaySettings", u"Surfaces", None))
        self.checkBoxPointsVisibility.setText(QCoreApplication.translate("DisplaySettings", u"Points", None))
        self.labelNodeSize.setText(QCoreApplication.translate("DisplaySettings", u"Node Size:", None))
    # retranslateUi

