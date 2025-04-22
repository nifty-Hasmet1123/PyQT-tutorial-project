from PySide6.QtWidgets import QCheckBox, QGroupBox, QHBoxLayout, QVBoxLayout, QWidget, QSizePolicy, QButtonGroup, QRadioButton
from PySide6.QtCore import Qt, Slot


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.master_layout = QVBoxLayout()
        self.container = QHBoxLayout()

        self.r1_os_ctn = QHBoxLayout() # for operating system box 
        self.r1_drinks_ctn = QHBoxLayout() # for drink box

        # ----------------------------------------------------------

        # group box for operating system
        self.box_left = QVBoxLayout()
        self.os_grp = QGroupBox("Choose operating system")
        self.os_grp.setLayout(self.box_left) # set the layout for the Groupbox
        self.r1_os_ctn.addWidget(self.os_grp)  
       
        
        # function here
        self.add_checkbox_in_os_container()

        
        self.container.addLayout(self.r1_os_ctn)
        #---------------------------------------------------------
        # for drinks
        self.box_right = QVBoxLayout()
        self.drinks_grp = QGroupBox("Choose drinks")
        self.drinks_grp.setLayout(self.box_right) # set the layout for the Groupbox
        self.r1_drinks_ctn.addWidget(self.drinks_grp)

        # functions here
        self.exlusive_button_to_button_group()

        self.container.addLayout(self.r1_drinks_ctn)
        
        ### ROW 2
        #---------------------------------------------------------
        self.row2 = QVBoxLayout()
        self.radio_grp = QGroupBox("Choose Answer")
        self.radio_grp.setLayout(self.row2)

        # function here
        self.add_radio_buttons()

        # --------------------------------------------------------
        # add master layout
        self.master_layout.addLayout(self.container)
        
        # add the radio_grp to the master layout(bottom of two containers)
        self.master_layout.addWidget(self.radio_grp)
        self.setLayout(self.master_layout)
    
    def add_radio_buttons(self):
        radio_list = [
            QRadioButton(letter)
            for letter in "abcd"
        ]

        for radio_button in radio_list:
            self.row2.addWidget(radio_button)
            
            # event
            radio_button.clicked.connect(
                lambda checked,     # default signal return statement of the QRadioButton
                btn=radio_button: # keyword argument passing the current QRadioButton instance in the loop.
                print(f"Bool: {checked} || Text Button: {btn.text()}")
            )

        # design
        self.row2.setAlignment(Qt.AlignTop)

    def exlusive_button_to_button_group(self):
        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True) # on load set the initial check to beer
        # make the checkboxes exclusive
        exclusive_btn_grp = QButtonGroup(self) # parent class
        exclusive_btn_grp.addButton(beer)
        exclusive_btn_grp.addButton(juice)
        exclusive_btn_grp.addButton(coffee)
        exclusive_btn_grp.setExclusive(True)

        # button group signals
        # exclusive_btn_grp.buttonClicked.connect(
        #     lambda e: print(f"Button: { [attr for attr in dir(e) if not attr.startswith("__")] }")
        # )
        exclusive_btn_grp.buttonClicked.connect(lambda e: print(f"Button: {e.text()}"))

        self.box_right.addWidget(beer)
        self.box_right.addWidget(juice)
        self.box_right.addWidget(coffee)
        self.box_right.setAlignment(Qt.AlignTop)

    def add_checkbox_in_os_container(self):
        windows = QCheckBox("Windows")
        linux = QCheckBox("Linux")
        mac = QCheckBox("Mac")

        # set policy sizes
        # windows.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # linux.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # mac.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # self.os_group_box_layout.setSpacing(2)

        windows.toggled.connect(lambda: print(f"Windows state has been changed: {windows.isChecked()}"))
        linux.toggled.connect(
            lambda checked_event: self.linux_os_slot(checked_event, linux)
        )
        mac.toggled.connect(self.mac_os_signal_slot)
        
        # Add the checkboxes to the group box's layout
        self.box_left.addWidget(windows)
        self.box_left.addWidget(linux)
        self.box_left.addWidget(mac)
        self.box_left.setAlignment(Qt.AlignTop)# set alignment on top only

    @Slot(bool)
    def mac_os_signal_slot(self, is_checked):
        """
        Automatically return a value based on event. calling the checkedState() function from the QCheckbox class
        """

        if is_checked:
            print("Mac state has been changed: {}".format(is_checked))
        else:
            # is_checked is currently false

            print("Mac state has not been selected: {}".format(is_checked))

    @Slot(bool, QCheckBox)
    def linux_os_slot(self, is_checked, instance_obj):
        if is_checked:
            print("Linux object is checkStateChange: {}".format(instance_obj.checkState()))
            print("Linux state has been changed!: {}".format(is_checked))
        else:
            print("Linux has not been checked: {}".format(is_checked))