class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interest Rate Calculator with MatPlotLib")
        self.resize(1080, 720)
        
        # Master layouts
        self.master_layout = QVBoxLayout()
        
        # Minor layouts
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout() # master layout na ito

        # row2 two columns
        self.row2_column1 = QVBoxLayout()
        self.row2_column2 = QVBoxLayout()

        # widgets for row 1
        self.interest_rate_label = QLabel("Interest Rate (%)")
        self.interest_rate_field_box = QLineEdit()
        self.interest_rate_field_box.setText("0")

        self.initial_investment_label = QLabel("Initial Investment")
        self.initial_investment_field_box = QLineEdit()
        self.initial_investment_field_box.setText("10000")

        self.number_of_years_label = QLabel("Number of Years")
        self.number_of_years_field_box = QLineEdit()
        self.number_of_years_field_box.setText("25")

        self.dark_mode_checkbox = QCheckBox("Dark mode")

        # widget for row 2
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(2)
        self.tree_widget.setHeaderLabels(["Year", "Description"])
        
        self.data_visualization_box = QLabel("Data Visualization box here")

        self.calculate_btn = QPushButton("Calculate")
        self.reset_btn = QPushButton("Reset")
        self.save_btn = QPushButton("Save")

        # add top-level items
        self.add_items_to_tree()
        # add the button after the tree
        self.add_buttons_to_row2_column1()
        
        # NOTE: add the data_visualization box to row2. Add functionalities on this
        self.row2_column2.addWidget(self.data_visualization_box)

        self.set_design()
        self.set_layout()
    
    def add_items_to_tree(self):
        # list value should match the number of list/column in the tree_widget.setHeaderLabel
        item1 = QTreeWidgetItem(["2020", "Started new projects"])
        item2 = QTreeWidgetItem(["2021", "Expanded new markets"])
        item3 = QTreeWidgetItem(["2022", "Major Product release"])

        self.tree_widget.addTopLevelItem(item1)
        self.tree_widget.addTopLevelItem(item2)
        self.tree_widget.addTopLevelItem(item3)

        # self.row2.addWidget(self.tree_widget)   
        self.row2_column1.addWidget(self.tree_widget)

    def add_buttons_to_row2_column1(self):
        self.row2_column1.addWidget(self.calculate_btn)
        self.row2_column1.addWidget(self.save_btn)
        self.row2_column1.addWidget(self.reset_btn)

    def set_layout(self):
        widgets = [
            "interest_rate_label",
            "interest_rate_field_box",
            "initial_investment_label",
            "initial_investment_field_box",
            "number_of_years_label",
            "number_of_years_field_box",
            "dark_mode_checkbox"
        ]

        for key, value in self.__dict__.items():
            if key in widgets:
                self.row1.addWidget(value)

        self.master_layout.addLayout(self.row1)

        ### add the row2_column1 and row2_column2 to the row2 master layout
        self.row2.addLayout(self.row2_column1)
        self.row2.addLayout(self.row2_column2)

        ### now add the row2 layout inside the master layout
        self.master_layout.addLayout(self.row2)

        self.setLayout(self.master_layout)     

    def set_design(self):
        # set the max width to 300px only
        self.tree_widget.setMaximumWidth(245)

        # Ensure horizontal scrolling is enabled when needed
        self.tree_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Set the minimum section size for the header
        self.tree_widget.header().setMinimumSectionSize(100)
        self.tree_widget.header().setDefaultSectionSize(200)

        # Disable last section from stretching (very important)
        self.tree_widget.header().setStretchLastSection(False)

        # Resizing columns to fit content
        self.tree_widget.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tree_widget.header().setSectionResizeMode(1, QHeaderView.ResizeToContents)