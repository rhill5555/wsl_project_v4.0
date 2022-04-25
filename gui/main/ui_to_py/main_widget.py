########################################################################################################################
# Project: wsl_app_v4_0
# FileName: main_widget.py
# Main Python Code for GUI
########################################################################################################################
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

# from gui.common_widget.dialog_widget.popup_add_data import AddLocationDialog, AddTourType, AddEventType, SurferToHeat
from gui.common_widget.dialog_widget.popup_add_data import AddLocationDialog
from gui.main.ui_to_py.wsl_analytics_ui_v2_0 import Ui_Form
from src.models import AddTour, AddLocation, AddSurfer, LocationLists


########################################################################################################################


class MainWidget(QMainWindow, Ui_Form):
    def __init__(self):
        # Call the constructor for the inherited QWidget class.
        QMainWindow.__init__(self)

        # Instances for AddLocationDialog
        add_loc_inst = AddLocation()

        # This function is inherited from the Ui_Form class.
        self.setupUi(self)

        # Call the connect_slots function to connect all the event-handlers to functions in this class.
        self.connect_slots()

        # Call to setup everything on the gui.
        self.on_startup()

    # This defines the event handlers for everything on the Main Widget
    def connect_slots(self):
        # # Slots for Add Event Tab
        # self.cb_addevent_year.currentIndexChanged.connect(self.slot_cb_addevent_year_on_index_change)
        # self.cb_addevent_continent.currentIndexChanged.connect(self.slot_cb_addevent_continent_on_index_change)
        # self.cb_addevent_country.currentIndexChanged.connect(self.slot_cb_addevent_country_on_index_change)
        # self.cb_addevent_region.currentIndexChanged.connect(self.slot_cb_addevent_region_on_index_change)
        #
        # self.pb_addevent_newtour.clicked.connect(self.slot_pb_addevent_newtour_clicked)
        # self.pb_addevent_clear.clicked.connect(self.slot_pb_addevent_clear_clicked)
        # self.pb_addevent_submit.clicked.connect(self.slot_pb_addevent_submit_clicked)
        #
        # # Slots for Add Heat Tab
        # self.cb_addheat_year.currentIndexChanged.connect(self.slot_cb_addheat_year_on_index_change)
        # self.cb_addheat_tour.currentIndexChanged.connect(self.slot_cb_addheat_tour_on_index_change)
        #
        # self.pb_addheat_newround.clicked.connect(self.slot_pb_addheat_newround_clicked)
        # self.pb_addheat_clear.clicked.connect(self.slot_pb_addheat_clear_clicked)
        # self.pb_addheat_submit.clicked.connect(self.slot_pb_addheat_submit_clicked)
        # self.pb_addheat_surfers.clicked.connect(self.slot_pb_addheat_surfers_clicked)
        #
        # # Slots for Add Round Results Tab
        # self.cb_addresults_year.currentIndexChanged.connect(self.slot_cb_addresults_year_on_index_change)
        # self.cb_addresults_tour.currentIndexChanged.connect(self.slot_cb_addresults_tour_on_index_change)
        # self.cb_addresults_event.currentIndexChanged.connect(self.slot_cb_addresults_round_on_index_change)
        # self.cb_addresults_round.currentIndexChanged.connect(self.slot_cb_addresults_heat_on_index_change)
        # self.cb_addresults_heat.currentIndexChanged.connect(self.slot_cb_addresults_surfer_on_index_change)
        #
        # self.pb_addresults_clear.clicked.connect(self.slot_pb_addresults_clear_clicked)
        # self.pb_addresults_submit.clicked.connect(self.slot_pb_addresults_submit_clicked)
        #
        # Slots for Add Break Tab
        self.cb_addbreak_continent.currentIndexChanged.connect(self.slot_cb_addbreak_continent_on_index_change)
        self.cb_addbreak_country.currentIndexChanged.connect(self.slot_cb_addbreak_country_on_index_change)

        self.pb_addbreak_clear.clicked.connect(self.slot_pb_addbreak_clear_clicked)
        self.pb_addbreak_newloc.clicked.connect(self.slot_pb_addbreak_newloc_clicked)
        self.pb_addbreak_submit.clicked.connect(self.slot_pb_addbreak_submit_clicked)

        # # Slots for Add Surfer Tab
        # self.cb_addsurfer_continent.currentIndexChanged.connect(self.slot_cb_addsurfer_continent_on_index_change)
        # self.cb_addsurfer_hcontinent.currentIndexChanged.connect(self.slot_cb_addsurfer_hcontinent_on_index_change)
        # self.cb_addsurfer_hcountry.currentIndexChanged.connect(self.slot_cb_addsurfer_hcountry_on_index_change)
        # self.cb_addsurfer_hregion.currentIndexChanged.connect(self.slot_cb_addsurfer_hregion_on_index_change)
        #
        # self.pb_addsurfer_clear.clicked.connect(self.slot_pb_addsurfer_clear_clicked)
        # self.pb_addsurfer_newloc.clicked.connect(self.slot_pb_addsurfer_newloc_clicked)
        # self.pb_addsurfer_submit.clicked.connect(self.slot_pb_addsurfer_submit_clicked)

    # Everything that should happen when the app has started up
    def on_startup(self):
        # Add Event Tab

        # Add Heat Tab

        # Add Round Results Tab
        # Add Tour Years

        # Add Break Tab
        self.cb_addbreak_continent.addItems([''] + LocationLists.return_continents())

        # Add Surfer Tab

    ########################################################################################################################
    # Add Event Tab

    ####################################################################################################################
    # Add Heat Tab

    ####################################################################################################################
    # Add Results Tab

    ####################################################################################################################
    #  Add Break Tab

    # Change Country List when a Continent is selected
    def slot_cb_addbreak_continent_on_index_change(self):
        self.cb_addbreak_country.clear()
        return_country_inst = LocationLists(entered_continent=self.cb_addbreak_continent.currentText())
        self.cb_addbreak_country.addItems([''] + return_country_inst.return_countries_from_continents())

    # Change Region List when a Country is selected
    def slot_cb_addbreak_country_on_index_change(self):
        self.cb_addbreak_region.clear()
        return_region_inst = LocationLists(entered_continent=self.cb_addbreak_continent.currentText(),
                                           entered_country=self.cb_addbreak_country.currentText())
        self.cb_addbreak_region.addItems([''] + return_region_inst.return_regions_from_countries())

    # Open a PopUp to enter new location when The Add Location Button is selected
    # noinspection PyMethodMayBeStatic
    def slot_pb_addbreak_newloc_clicked(self):
        dialog = AddLocationDialog(title="Add a location to the database.",
                                   prev_selected_continent=self.cb_addbreak_continent.currentText(),
                                   prev_selected_country=self.cb_addbreak_country.currentText(),
                                   prev_selected_region=self.cb_addbreak_region.currentText())

        if dialog.exec() == QDialog.Accepted:
            continent = dialog.cb_continent.currentText()

        entered_continent = dialog.cb_continent.currentText()

        # If country was entered into line edit use that value. Else use combobox.
        country_in_line_edit = dialog.line_country.text() is None or dialog.line_country.text() == ''
        country_in_combobox = dialog.cb_country.currentText() is None or dialog.cb_country.currentText() == ''
        if not country_in_line_edit:
            entered_country = dialog.line_country.text()
            add_country_inst = AddLocation(entered_continent=entered_continent,
                                           entered_country=entered_country)
            add_country_inst.add_new_country()
        elif country_in_combobox:
            print(f"\nSelect or enter a country.\n")
        else:
            entered_country = dialog.cb_country.currentText()

        # If region was entered into line edit use that value. Else use combobox.
        region_in_line_edit = dialog.line_region.text() is None or dialog.line_region.text() == ''
        region_in_combobox = dialog.cb_region.currentText() is None or dialog.cb_region.currentText() == ''
        if not region_in_line_edit:
            entered_region = dialog.line_region.text()
            add_region_inst = AddLocation(entered_continent=entered_continent,
                                          entered_country=entered_country,
                                          entered_region=entered_region)
            add_region_inst.add_new_region()
        elif region_in_combobox:
            print(f"\nSelect or enter a region.\n")
        else:
            entered_region = dialog.cb_region.currentText()

        # Grab City from line edit
        if dialog.line_city.text() is None or dialog.line_city == '':
            print(f"\nEnter a city.\n")
        else:
            entered_city = dialog.line_city.text()
            add_city_inst = AddLocation(entered_continent=entered_continent,
                                        entered_country=entered_country,
                                        entered_region=entered_region,
                                        entered_city=entered_city)
            add_city_inst.add_new_city()

    # Clear the form when the Clear button is checked
    def slot_pb_addbreak_clear_clicked(self):
        pass

    # When the Submit button is clicked all data should be assigned a variable, prepared, and inserted into mysal db
    def slot_pb_addbreak_submit_clicked(self):
        pass

    def testing(self):
        print(f"I'm in testing")

####################################################################################################################
# Add Surfer Tab


########################################################################################################################

if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()

    sys.exit(app.exec())
