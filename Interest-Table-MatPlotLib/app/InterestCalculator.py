from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QTreeWidget,
    QTreeWidgetItem,
    QCheckBox,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QHeaderView,
    QMessageBox
)
from PySide6.QtCore import Qt
from enum import Enum

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas


class WidgetEnums(Enum):
    # if you were to use the WidgetItems.set_widget_on_instance don't forget to add the enums here for looping later
    ROW_1 = [
        "interest_rate_label",
        "interest_rate_field_box",
        "initial_investment_label",
        "initial_investment_field_box",
        "number_of_years_label",
        "number_of_years_field_box",
        "dark_mode_checkbox"
    ]
    ROW_2 = [
        "tree_widget",
        "figure",
        "calculate_btn",
        "reset_btn",
        # "save_btn"
    ]

class WidgetItems():
    def __init__(self, instance):
        self.instance = instance

    # @property
    def get_all_widgets(self):
        return self.instance.__dict__
    
    # @get_all_widgets.setter
    def set_widget_on_instance(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self.instance, key, value)

    def set_design(self):
        if self.instance:
            objects = self.instance.__dict__
            
            if objects["tree_widget"]:
                # settings
                self.instance.tree_widget.setColumnCount(2)
                self.instance.tree_widget.setHeaderLabels(["Year", "Description"])
                self.instance.tree_widget.header().setDefaultAlignment(Qt.AlignCenter)

                # design
                self.instance.tree_widget.setMaximumWidth(245)
                self.instance.tree_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

                self.instance.tree_widget.header().setMinimumSectionSize(100)
                self.instance.tree_widget.header().setDefaultSectionSize(200)
                self.instance.tree_widget.header().setStretchLastSection(False)
                self.instance.tree_widget.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
                self.instance.tree_widget.header().setSectionResizeMode(1, QHeaderView.ResizeToContents)

            if objects["interest_rate_label"]:
                self.instance.interest_rate_field_box.setText("5")

            if objects["initial_investment_label"]:
                self.instance.initial_investment_field_box.setText("1000")

            if objects["number_of_years_field_box"]:
                self.instance.number_of_years_field_box.setText("3")
    
    def return_canvas_object(self):
        if self.instance:
            objects = self.instance.__dict__

            if objects["figure"]:
                canvas = FigureCanvas(self.instance.figure)
        
                return canvas


class InterestCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_assigner = WidgetItems(self)
        
        # define layouts here
        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2_master_layout = QHBoxLayout()

        self.row2_col_1 = QVBoxLayout()
        self.row2_col_2 = QVBoxLayout()

        # define the all the widgets here
        self.widget_assigner.set_widget_on_instance(
            # row 1
            interest_rate_label=QLabel("Interest Rate (%)"),
            interest_rate_field_box=QLineEdit(),
            initial_investment_label=QLabel("Initial Investment"),
            initial_investment_field_box=QLineEdit(),
            number_of_years_label=QLabel("Number of Years"),
            number_of_years_field_box=QLineEdit(),
            dark_mode_checkbox=QCheckBox("Dark Mode"),
            # row 2
            tree_widget=QTreeWidget(),
            figure=plt.figure(),
            calculate_btn=QPushButton("Calculate"),
            reset_btn=QPushButton("Reset"),
            # save_btn=QPushButton("Save")
        )
        self.canvas = None

        # set the design from the widget_assigner
        self.widget_assigner.set_design()

    
        # set the functions here on click
        self.calculate_btn.clicked.connect(self.add_items_to_tree)
        self.reset_btn.clicked.connect(self.reset)

        # set the layout here
        self.set_layout()

    def set_layout(self):
        # add the widget to row 1
        self.add_widget_to_row(self.row1, WidgetEnums.ROW_1.value)
        
        # add the widget to row 2
        self.row2_master_layout.addLayout(self.row2_col_1)
        self.row2_master_layout.addLayout(self.row2_col_2)

        # set the master layout
        # call the function that add the items to the tree here and the buttons and the data visualization qlabel
        # self.add_items_to_tree()

        self.row2_col_1.addWidget(self.tree_widget)

        self.add_buttons_to_row2_col1()
        self.add_data_visualization_data()

        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2_master_layout)

        # set the final layout here
        self.setLayout(self.master_layout)

    def add_data_visualization_data(self):
        if self.figure:
            # call the canvas here
            # set the matplotlib here
            self.canvas = self.widget_assigner.return_canvas_object()

            self.row2_col_2.addWidget(self.canvas)

    def add_items_to_tree(self):
        # item1 = QTreeWidgetItem(["2020", "Started new projects"])
        # item2 = QTreeWidgetItem(["2021", "Expanded new markets"])
        # item3 = QTreeWidgetItem(["2022", "Major Product release"])

        # if self.tree_widget:
        #     self.tree_widget.addTopLevelItem(item1)
        #     self.tree_widget.addTopLevelItem(item2)
        #     self.tree_widget.addTopLevelItem(item3)

        #     self.row2_col_1.addWidget(self.tree_widget)
        try:
            interest_rate = float(self.interest_rate_field_box.text())
            initial_investment = float(self.initial_investment_field_box.text()) 
            years = int(self.number_of_years_field_box.text())
            percent = 100; 
        except ValueError:
            QMessageBox.critical(self, "Value Error", "Invalid values were put in the text box/s")
        else:
            # update the data in the tree box
            total = initial_investment

            for year in range(1, years + 1):
                total += total * (interest_rate / percent)
                item_year = QTreeWidgetItem([
                    str(year), 
                    "{:.2f}".format(total)
                ])
                self.tree_widget.addTopLevelItem(item_year)
            
            # update the chart with our data
            self.figure.clear()
            ax = self.figure.subplots()
            year_list = [i for i in range(1, years + 1)]  
            totals = [initial_investment * (1 + interest_rate / percent) ** year for year in year_list]

            ax.plot(year_list, totals)
            ax.set_title("Interest Chart")
            ax.set_xlabel("Year")
            ax.set_ylabel("Total")

            if self.canvas:
                self.canvas.draw()


    def reset(self):
        if self.interest_rate_field_box and self.initial_investment_field_box and self.number_of_years_field_box and self.tree_widget:

            self.interest_rate_field_box.clear()
            self.initial_investment_field_box.clear()
            self.number_of_years_field_box.clear()
            self.tree_widget.clear()
            self.figure.clear()
            
            if self.canvas:
                self.canvas.draw()

    def add_buttons_to_row2_col1(self):
        # if self.calculate_btn and self.save_btn and self.reset_btn:
        if self.calculate_btn and self.reset_btn:
            self.row2_col_1.addWidget(self.calculate_btn)
            # self.row2_col_1.addWidget(self.save_btn)
            self.row2_col_1.addWidget(self.reset_btn)

    def add_widget_to_row(self, widget_row, enums):
        for key, value in self.__dict__.items():
            if key in enums:
                widget_row.addWidget(value)
        