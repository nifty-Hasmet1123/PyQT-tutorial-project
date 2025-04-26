# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1145, 805)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_btn = QPushButton(Widget)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)
        self.add_btn.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout.addWidget(self.add_btn)

        self.spin_box = QSpinBox(Widget)
        self.spin_box.setObjectName(u"spin_box")
        sizePolicy.setHeightForWidth(self.spin_box.sizePolicy().hasHeightForWidth())
        self.spin_box.setSizePolicy(sizePolicy)
        self.spin_box.setMaximumSize(QSize(300, 16777215))
        self.spin_box.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.spin_box)

        self.minus_btn = QPushButton(Widget)
        self.minus_btn.setObjectName(u"minus_btn")
        sizePolicy.setHeightForWidth(self.minus_btn.sizePolicy().hasHeightForWidth())
        self.minus_btn.setSizePolicy(sizePolicy)
        self.minus_btn.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout.addWidget(self.minus_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.add_btn.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.minus_btn.setText(QCoreApplication.translate("Widget", u"Minus", None))
    # retranslateUi

