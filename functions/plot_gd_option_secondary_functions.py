import logging
import cartopy
from functions.utils import populate_combobox
from functions.other_windows_functions import MyWait, MyProjection, MyTicks, MyColorbarTicks
from functions.material_functions import cmap_default_fig_margins, grid_projection_parameters
from PyQt5 import QtCore, QtGui, QtWidgets


def update_gd_slider_value(self, val):
    logging.debug('gui - plot_gd_option_secondary_functions.py - update_gd_slider_value')
    if self.sender().objectName() == 'pw_grid_slider_1':
        self.pw_grid_label_5.setText(str(float(val) / 100))
    elif self.sender().objectName() == 'pw_grid_slider_2':
        self.pw_grid_label_6.setText(str(float(val) / 100))
    elif self.sender().objectName() == 'pw_grid_slider_3':
        self.pw_grid_label_9.setText(str(float(val) / 100))
    elif self.sender().objectName() == 'pw_grid_slider_4':
        self.pw_grid_label_10.setText(str(float(val) / 100))


def display_grid_projection_options(self, projection_options=None):
    logging.debug('gui - plot_gd_option_secondary_functions.py - display_grid_projection_options')
    if projection_options is None:
        projection_options = self.gd_projection_options
    text = 'Options: '
    for option in sorted(projection_options.keys()):
        text += option + '=' + str(projection_options[option]) + ' ; '
    text = text[: -3]
    self.pw_grid_label_13.setText(text)


def set_projection_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - set_projection_options')
    self.gd_projection_options = grid_projection_parameters()[str(self.pw_grid_combobox_7.currentText())]
    display_grid_projection_options(self, self.gd_projection_options)
    if str(self.pw_grid_combobox_7.currentText()) not in ['PlateCarree', 'Mercator']:
        self.pw_grid_set_ticks.setEnabled(False)
        self.pw_grid_label_14.setEnabled(False)
        self.pw_grid_label_15.setEnabled(False)
    else:
        self.pw_grid_set_ticks.setEnabled(True)
        self.pw_grid_label_14.setEnabled(True)
        self.pw_grid_label_15.setEnabled(True)


def display_grid_ticks_options(self, ticks_options=None):
    logging.debug('gui - plot_gd_option_secondary_functions.py - display_grid_ticks_options')
    if ticks_options is None:
        ticks_options = self.gd_ticks_options
    self.pw_grid_label_14.setText('X: ' + str(ticks_options['xticks']))
    self.pw_grid_label_15.setText('Y: ' + str(ticks_options['yticks']))


def activate_boundaries_hex_rgb_color(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_boundaries_hex_rgb_color')
    if self.sender().objectName() == 'pw_grid_combobox_13':
        if self.sender().currentIndex() == 0:
            self.pw_grid_line_13.setVisible(True)
            self.pw_grid_line_14.setVisible(False)
            self.pw_grid_line_15.setVisible(False)
            self.pw_grid_line_13.setEnabled(True)
            self.pw_grid_line_14.setEnabled(False)
            self.pw_grid_line_15.setEnabled(False)
            self.pw_grid_line_13.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_13.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_13.setText('')
            self.pw_grid_line_14.setText('')
            self.pw_grid_line_15.setText('')
        elif self.sender().currentIndex() == 1:
            self.pw_grid_line_13.setVisible(True)
            self.pw_grid_line_14.setVisible(True)
            self.pw_grid_line_15.setVisible(True)
            self.pw_grid_line_13.setEnabled(True)
            self.pw_grid_line_14.setEnabled(True)
            self.pw_grid_line_15.setEnabled(True)
            self.pw_grid_line_13.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_13.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_13.setText('')
            self.pw_grid_line_14.setText('')
            self.pw_grid_line_15.setText('')
        else:
            self.pw_grid_line_13.setVisible(False)
            self.pw_grid_line_14.setVisible(False)
            self.pw_grid_line_15.setVisible(False)
            self.pw_grid_line_13.setEnabled(False)
            self.pw_grid_line_14.setEnabled(False)
            self.pw_grid_line_15.setEnabled(False)
            self.pw_grid_line_13.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_13.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_13.setText('')
            self.pw_grid_line_14.setText('')
            self.pw_grid_line_15.setText('')
    elif self.sender().objectName() == 'pw_grid_combobox_14':
        if self.sender().currentIndex() == 1:
            self.pw_grid_line_18.setVisible(True)
            self.pw_grid_line_16.setVisible(False)
            self.pw_grid_line_17.setVisible(False)
            self.pw_grid_line_18.setEnabled(True)
            self.pw_grid_line_16.setEnabled(False)
            self.pw_grid_line_17.setEnabled(False)
            self.pw_grid_line_18.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_18.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_18.setText('')
            self.pw_grid_line_16.setText('')
            self.pw_grid_line_17.setText('')
        elif self.sender().currentIndex() == 2:
            self.pw_grid_line_18.setVisible(True)
            self.pw_grid_line_16.setVisible(True)
            self.pw_grid_line_17.setVisible(True)
            self.pw_grid_line_18.setEnabled(True)
            self.pw_grid_line_16.setEnabled(True)
            self.pw_grid_line_17.setEnabled(True)
            self.pw_grid_line_18.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_18.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_18.setText('')
            self.pw_grid_line_16.setText('')
            self.pw_grid_line_17.setText('')
        else:
            self.pw_grid_line_18.setVisible(False)
            self.pw_grid_line_16.setVisible(False)
            self.pw_grid_line_17.setVisible(False)
            self.pw_grid_line_18.setEnabled(False)
            self.pw_grid_line_16.setEnabled(False)
            self.pw_grid_line_17.setEnabled(False)
            self.pw_grid_line_18.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_18.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_18.setText('')
            self.pw_grid_line_16.setText('')
            self.pw_grid_line_17.setText('')
    elif self.sender().objectName() == 'pw_grid_combobox_16':
        if self.sender().currentIndex() == 0:
            self.pw_grid_line_20.setVisible(True)
            self.pw_grid_line_21.setVisible(False)
            self.pw_grid_line_22.setVisible(False)
            self.pw_grid_line_20.setEnabled(True)
            self.pw_grid_line_21.setEnabled(False)
            self.pw_grid_line_22.setEnabled(False)
            self.pw_grid_line_20.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_20.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_20.setText('')
            self.pw_grid_line_21.setText('')
            self.pw_grid_line_22.setText('')
        elif self.sender().currentIndex() == 1:
            self.pw_grid_line_20.setVisible(True)
            self.pw_grid_line_21.setVisible(True)
            self.pw_grid_line_22.setVisible(True)
            self.pw_grid_line_20.setEnabled(True)
            self.pw_grid_line_21.setEnabled(True)
            self.pw_grid_line_22.setEnabled(True)
            self.pw_grid_line_20.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_20.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_20.setText('')
            self.pw_grid_line_21.setText('')
            self.pw_grid_line_22.setText('')
        else:
            self.pw_grid_line_20.setVisible(False)
            self.pw_grid_line_21.setVisible(False)
            self.pw_grid_line_22.setVisible(False)
            self.pw_grid_line_20.setEnabled(False)
            self.pw_grid_line_21.setEnabled(False)
            self.pw_grid_line_22.setEnabled(False)
            self.pw_grid_line_20.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_20.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_20.setText('')
            self.pw_grid_line_21.setText('')
            self.pw_grid_line_22.setText('')
    elif self.sender().objectName() == 'pw_grid_combobox_17':
        if self.sender().currentIndex() == 1:
            self.pw_grid_line_23.setVisible(True)
            self.pw_grid_line_24.setVisible(False)
            self.pw_grid_line_25.setVisible(False)
            self.pw_grid_line_23.setEnabled(True)
            self.pw_grid_line_24.setEnabled(False)
            self.pw_grid_line_25.setEnabled(False)
            self.pw_grid_line_23.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_23.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_23.setText('')
            self.pw_grid_line_24.setText('')
            self.pw_grid_line_25.setText('')
        elif self.sender().currentIndex() == 2:
            self.pw_grid_line_23.setVisible(True)
            self.pw_grid_line_24.setVisible(True)
            self.pw_grid_line_25.setVisible(True)
            self.pw_grid_line_23.setEnabled(True)
            self.pw_grid_line_24.setEnabled(True)
            self.pw_grid_line_25.setEnabled(True)
            self.pw_grid_line_23.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_23.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_23.setText('')
            self.pw_grid_line_24.setText('')
            self.pw_grid_line_25.setText('')
        else:
            self.pw_grid_line_23.setVisible(False)
            self.pw_grid_line_24.setVisible(False)
            self.pw_grid_line_25.setVisible(False)
            self.pw_grid_line_23.setEnabled(False)
            self.pw_grid_line_24.setEnabled(False)
            self.pw_grid_line_25.setEnabled(False)
            self.pw_grid_line_23.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_23.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_23.setText('')
            self.pw_grid_line_24.setText('')
            self.pw_grid_line_25.setText('')
    elif self.sender().objectName() == 'pw_grid_combobox_18':
        if self.sender().currentIndex() == 0:
            self.pw_grid_line_28.setVisible(True)
            self.pw_grid_line_27.setVisible(False)
            self.pw_grid_line_26.setVisible(False)
            self.pw_grid_line_28.setEnabled(True)
            self.pw_grid_line_27.setEnabled(False)
            self.pw_grid_line_26.setEnabled(False)
            self.pw_grid_line_28.setMinimumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_28.setMaximumSize(QtCore.QSize(100, 27))
            self.pw_grid_line_28.setText('')
            self.pw_grid_line_27.setText('')
            self.pw_grid_line_26.setText('')
        elif self.sender().currentIndex() == 1:
            self.pw_grid_line_28.setVisible(True)
            self.pw_grid_line_27.setVisible(True)
            self.pw_grid_line_26.setVisible(True)
            self.pw_grid_line_28.setEnabled(True)
            self.pw_grid_line_27.setEnabled(True)
            self.pw_grid_line_26.setEnabled(True)
            self.pw_grid_line_28.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_28.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_28.setText('')
            self.pw_grid_line_27.setText('')
            self.pw_grid_line_26.setText('')
        else:
            self.pw_grid_line_28.setVisible(False)
            self.pw_grid_line_27.setVisible(False)
            self.pw_grid_line_26.setVisible(False)
            self.pw_grid_line_28.setEnabled(False)
            self.pw_grid_line_27.setEnabled(False)
            self.pw_grid_line_26.setEnabled(False)
            self.pw_grid_line_28.setMinimumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_28.setMaximumSize(QtCore.QSize(60, 27))
            self.pw_grid_line_28.setText('')
            self.pw_grid_line_27.setText('')
            self.pw_grid_line_26.setText('')


def activate_coastlines_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_coastlines_options')
    self.pw_grid_label_27.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_label_29.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_label_30.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_label_40.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_combobox_12.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_line_12.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_combobox_13.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_combobox_14.setEnabled(self.pw_grid_checkbox_6.isChecked())
    self.pw_grid_line_12.setText('1')
    self.pw_grid_combobox_12.setCurrentIndex(2)
    self.pw_grid_combobox_13.setCurrentIndex(2)
    self.pw_grid_combobox_14.setCurrentIndex(0)


def activate_lakes_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_lakes_options')
    self.pw_grid_label_28.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_label_41.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_label_42.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_label_43.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_combobox_15.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_line_19.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_combobox_16.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_combobox_17.setEnabled(self.pw_grid_checkbox_7.isChecked())
    self.pw_grid_line_19.setText('0.5')
    self.pw_grid_combobox_15.setCurrentIndex(2)
    self.pw_grid_combobox_16.setCurrentIndex(3)
    self.pw_grid_combobox_17.setCurrentIndex(4)


def activate_grid_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_grid_options')
    self.pw_grid_label_23.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_label_24.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_label_25.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_combobox_8.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_combobox_18.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_line_4.setEnabled(self.pw_grid_checkbox_1.isChecked())
    self.pw_grid_combobox_8.setCurrentIndex(3)
    self.pw_grid_combobox_18.setCurrentIndex(2)
    self.pw_grid_line_4.setText('0.5')


def activate_colormap_dimensions(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_colormap_dimensions')
    self.pw_grid_label_36.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_label_37.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_label_38.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_label_39.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_line_8.setText('')
    self.pw_grid_line_9.setText('')
    self.pw_grid_line_10.setText('')
    self.pw_grid_line_11.setText('')
    self.pw_grid_line_8.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_line_9.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_line_10.setEnabled(not self.pw_grid_checkbox_5.isChecked())
    self.pw_grid_line_11.setEnabled(not self.pw_grid_checkbox_5.isChecked())


def activate_colormap_values(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_colormap_values')
    self.pw_grid_line_5.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_line_6.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_line_7.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_line_5.setText('')
    self.pw_grid_line_6.setText('')
    self.pw_grid_line_7.setText('')
    self.pw_grid_label_33.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_label_34.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_label_35.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_label_57.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_set_cmap_ticks.setEnabled(not self.pw_grid_checkbox_4.isChecked())
    self.pw_grid_label_57.setText('')
    self.gd_cbar_ticks_options = []


def activate_colormap_options(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - activate_colormap_options')
    self.pw_grid_label_31.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_label_32.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_label_45.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_line_29.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_info_button_5.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_combobox_10.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_combobox_11.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_combobox_10.setCurrentIndex(1)
    self.pw_grid_combobox_11.setCurrentIndex(3)
    self.pw_grid_checkbox_3.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_checkbox_4.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_checkbox_5.setEnabled(self.pw_grid_checkbox_2.isChecked())
    self.pw_grid_checkbox_3.setChecked(False)
    self.pw_grid_checkbox_4.setChecked(True)
    self.pw_grid_checkbox_5.setChecked(True)


def set_colormap_default_dimensions(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - set_colormap_default_dimensions')
    self.pw_grid_combobox_11.currentIndex()


def set_colormap_default_margins(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - set_colormap_default_margins')
    margins_dict = cmap_default_fig_margins()[int(self.pw_grid_combobox_11.currentIndex())]
    self.pw_grid_slider_1.setSliderPosition(margins_dict['margin_left'] * 100)
    self.pw_grid_slider_2.setSliderPosition(100 - margins_dict['margin_top'] * 100)
    self.pw_grid_slider_3.setSliderPosition(100 - margins_dict['margin_right'] * 100)
    self.pw_grid_slider_4.setSliderPosition(margins_dict['margin_bottom'] * 100)


def set_projection_function(proj, option_dict):
    logging.debug('gui - plot_gd_option_secondary_functions.py - set_projection_function')
    proj_result = None
    if proj == 'PlateCarree':
        proj_result = cartopy.crs.PlateCarree(central_longitude=option_dict['central_longitude'],
                                              globe=option_dict['globe'])
    elif proj == 'AlbersEqualArea':
        proj_result = cartopy.crs.AlbersEqualArea(central_longitude=option_dict['central_longitude'],
                                                  central_latitude=option_dict['central_latitude'],
                                                  false_easting=option_dict['false_easting'],
                                                  false_northing=option_dict['false_northing'],
                                                  standard_parallels=option_dict['standard_parallels'],
                                                  globe=option_dict['globe'])
    elif proj == 'AzimuthalEquidistant':
        proj_result = cartopy.crs.AzimuthalEquidistant(central_longitude=option_dict['central_longitude'],
                                                       entral_latitude=option_dict['entral_latitude'],
                                                       false_easting=option_dict['false_easting'],
                                                       false_northing=option_dict['false_northing'],
                                                       globe=option_dict['globe'])
    elif proj == 'EquidistantConic':
        proj_result = cartopy.crs.EquidistantConic(central_longitude=option_dict['central_longitude'],
                                                   central_latitude=option_dict['central_latitude'],
                                                   false_easting=option_dict['false_easting'],
                                                   false_northing=option_dict['false_northing'],
                                                   standard_parallels=option_dict['standard_parallels'],
                                                   globe=option_dict['globe'])
    elif proj == 'LambertConformal':
        proj_result = cartopy.crs.LambertConformal(central_longitude=option_dict['central_longitude'],
                                                   central_latitude=option_dict['central_latitude'],
                                                   false_easting=option_dict['false_easting'],
                                                   false_northing=option_dict['false_northing'],
                                                   secant_latitudes=option_dict['secant_latitudes'],
                                                   standard_parallels=option_dict['standard_parallels'],
                                                   globe=option_dict['globe'],
                                                   cutoff=option_dict['cutoff'])
    elif proj == 'Mollweide':
        proj_result = cartopy.crs.Mollweide(central_longitude=option_dict['central_longitude'],
                                            globe=option_dict['globe'],
                                            false_easting=option_dict['false_easting'],
                                            false_northing=option_dict['false_northing'])
    elif proj == 'Orthographic':
        proj_result = cartopy.crs.Orthographic(central_longitude=option_dict['central_longitude'],
                                               central_latitude=option_dict['central_latitude'],
                                               globe=option_dict['globe'])
    elif proj == 'LambertCylindrical':
        proj_result = cartopy.crs.LambertCylindrical(central_longitude=option_dict['central_longitude'])
    elif proj == 'Mercator':
        proj_result = cartopy.crs.Mercator(central_longitude=option_dict['central_longitude'],
                                           min_latitude=option_dict['min_latitude'],
                                           max_latitude=option_dict['max_latitude'],
                                           globe=option_dict['globe'],
                                           latitude_true_scale=option_dict['latitude_true_scale'],
                                           false_easting=option_dict['false_easting'],
                                           false_northing=option_dict['false_northing'],
                                           scale_factor=option_dict['scale_factor'])
    elif proj == 'Miller':
        proj_result = cartopy.crs.Miller(central_longitude=option_dict['central_longitude'],
                                         globe=option_dict['globe'])
    elif proj == 'Robinson':
        proj_result = cartopy.crs.Robinson(central_longitude=option_dict['central_longitude'],
                                           globe=option_dict['globe'],
                                           false_easting=option_dict['false_easting'],
                                           false_northing=option_dict['false_northing'])
    elif proj == 'Sinusoidal':
        proj_result = cartopy.crs.Sinusoidal(central_longitude=option_dict['central_longitude'],
                                             false_easting=option_dict['false_easting'],
                                             false_northing=option_dict['false_northing'],
                                             globe=option_dict['globe'])
    elif proj == 'Geostationary':
        proj_result = cartopy.crs.Geostationary(central_longitude=option_dict['central_longitude'],
                                                satellite_height=option_dict['satellite_height'],
                                                false_easting=option_dict['false_easting'],
                                                false_northing=option_dict['false_northing'],
                                                globe=option_dict['globe'],
                                                sweep_axis=option_dict['sweep_axis'])
    elif proj == 'EckertI':
        proj_result = cartopy.crs.EckertI(central_longitude=option_dict['central_longitude'],
                                          false_easting=option_dict['false_easting'],
                                          false_northing=option_dict['false_northing'],
                                          globe=option_dict['globe'])
    elif proj == 'EqualEarth':
        proj_result = cartopy.crs.EqualEarth(central_longitude=option_dict['central_longitude'],
                                             false_easting=option_dict['false_easting'],
                                             false_northing=option_dict['false_northing'],
                                             globe=option_dict['globe'])
    elif proj == 'NorthPolarStereo':
        proj_result = cartopy.crs.NorthPolarStereo(central_longitude=option_dict['central_longitude'],
                                                   true_scale_latitude=option_dict['true_scale_latitude'],
                                                   globe=option_dict['globe'])
    elif proj == 'SouthPolarStereo':
        proj_result = cartopy.crs.SouthPolarStereo(central_longitude=option_dict['central_longitude'],
                                                   true_scale_latitude=option_dict['true_scale_latitude'],
                                                   globe=option_dict['globe'])

    return proj_result


def wait_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - wait_window')
    info_text = 'Rendering figure, please wait...'
    self.mywait_window = MyWait(info_text)
    self.mywait_window.exec_()


def update_wait_window(self, text):
    logging.debug('gui - plot_gd_option_secondary_functions.py - update_wait_window')
    self.mywait_window.label.setText(text)


def close_wait_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - close_wait_window')
    self.mywait_window.close()


def projection_option_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - projection_option_window')
    option_window = MyProjection(self.gd_projection_options, str(self.pw_grid_combobox_7.currentText()))
    option_window.exec_()
    if option_window.new_option_dict is not None:
        self.gd_projection_options = option_window.new_option_dict
        display_grid_projection_options(self)


def tick_option_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - tick_option_window')
    ticks_window = MyTicks(self.gd_ticks_options)
    ticks_window.exec_()
    if ticks_window.new_option_dict is not None:
        self.gd_ticks_options = ticks_window.new_option_dict
        display_grid_ticks_options(self)


def colorbar_tick_option_window(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - colorbar_tick_option_window')
    cbar_ticks_window = MyColorbarTicks(self.gd_cbar_ticks_options)
    cbar_ticks_window.exec_()
    if cbar_ticks_window.new_option_dict is not None:
        self.gd_cbar_ticks_options = cbar_ticks_window.new_option_dict
        self.pw_grid_line_5.setText('man')
        self.pw_grid_line_6.setText('man')
        self.pw_grid_line_7.setText('man')
        self.pw_grid_label_57.setText(str(self.gd_cbar_ticks_options))


def colorbar_tick_option_man_remove(self):
    logging.debug('gui - plot_gd_option_secondary_functions.py - colorbar_tick_option_man_remove')
    self.pw_grid_label_57.setText('')
    self.gd_cbar_ticks_options = []