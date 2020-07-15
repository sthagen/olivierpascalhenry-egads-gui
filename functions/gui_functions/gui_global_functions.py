import logging
import pathlib
import xml
import os
from egads import EgadsData
from PyQt5 import QtWidgets, QtCore, QtGui
from functions.utils import (font_creation_function, stylesheet_creation_function, humansize, icon_creation_function,
                             clear_layout, full_path_name_from_treewidget, replace_old_path_by_new_path,
                             replace_old_path_by_new_path_tooltip, get_element_value)
from functions.gui_functions.gui_widgets import DropFrame
from functions.gui_functions.gui_support_functions import too_many_files


def gui_reset_function(self):
    logging.debug('gui - old_gui_global_functions.py - gui_initialization')
    try:
        self.tab_view.currentChanged.disconnect()
    except TypeError:
        pass
    self.tab_view.setCurrentIndex(0)
    update_icons_state(self)
    clear_layout(self.global_container)
    clear_layout(self.variable_widget_container)
    clear_layout(self.newvariable_widget_container)
    try:
        clear_layout(self.metadata_container)
    except AttributeError:
        pass
    try:
        clear_layout(self.newmetadata_container)
    except AttributeError:
        pass
    self.tab_view.removeTab(2)
    self.tab_view.setEnabled(False)
    self.tab_view.setVisible(False)
    self.gridLayout.removeWidget(self.tab_view)


def file_drop_layout(self):
    logging.debug('gui - old_gui_global_functions.py - file_drop_layout')
    font1 = font_creation_function('normal')
    self.drop_grid_layout_2 = QtWidgets.QGridLayout()
    self.drop_grid_layout_2.setObjectName("drop_grid_layout_2")
    self.drop_grid_layout_2.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Expanding), 0, 1, 1, 1)
    self.drop_grid_layout_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Minimum), 1, 0, 1, 1)
    self.drop_frame = DropFrame()
    self.drop_frame.setMinimumSize(QtCore.QSize(380, 190))
    self.drop_frame.setMaximumSize(QtCore.QSize(380, 190))
    self.drop_frame.setAcceptDrops(True)
    self.drop_frame.setStyleSheet(stylesheet_creation_function('qframe'))
    self.drop_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.drop_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    self.drop_frame.setObjectName("drop_frame")
    self.drop_grid_layout = QtWidgets.QGridLayout(self.drop_frame)
    self.drop_grid_layout.setObjectName("drop_grid_layout")
    self.drop_grid_layout.addItem(QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum,
                                                        QtWidgets.QSizePolicy.Expanding), 0, 1, 1, 1)
    self.drop_grid_layout.addItem(QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum), 1, 0, 1, 1)
    self.drop_vert_layout = QtWidgets.QVBoxLayout()
    self.drop_vert_layout.setObjectName("drop_vert_layout")
    self.drop_hor_layout = QtWidgets.QHBoxLayout()
    self.drop_hor_layout.setObjectName("drop_hor_layout")
    self.drop_hor_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                       QtWidgets.QSizePolicy.Minimum))
    self.drop_label_1 = QtWidgets.QLabel(self.drop_frame)
    self.drop_label_1.setMinimumSize(QtCore.QSize(50, 50))
    self.drop_label_1.setMaximumSize(QtCore.QSize(50, 50))
    self.drop_label_1.setStyleSheet(stylesheet_creation_function('qlabel_noborder'))
    self.drop_label_1.setText("")
    self.drop_label_1.setPixmap(QtGui.QPixmap("icons/egads_icon.svg"))
    self.drop_label_1.setScaledContents(True)
    self.drop_label_1.setObjectName("drop_label_1")
    self.drop_hor_layout.addWidget(self.drop_label_1)
    self.drop_hor_layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                       QtWidgets.QSizePolicy.Minimum))
    self.drop_vert_layout.addLayout(self.drop_hor_layout)
    self.drop_label_2 = QtWidgets.QLabel(self.drop_frame)
    self.drop_label_2.setMinimumSize(QtCore.QSize(0, 27))
    self.drop_label_2.setMaximumSize(QtCore.QSize(16777215, 27))
    self.drop_label_2.setFont(font1)
    self.drop_label_2.setStyleSheet(stylesheet_creation_function('qlabel_noborder'))
    self.drop_label_2.setObjectName("drop_label_2")
    self.drop_label_2.setText("<html><head/><body><p><span style=\" font-weight:600;\">Choose</span> a file or <span "
                              "style=\" font-weight:600;\">drop</span> it here.</p></body></html>")
    self.drop_vert_layout.addWidget(self.drop_label_2)
    self.drop_grid_layout.addLayout(self.drop_vert_layout, 1, 1, 1, 1)
    self.drop_grid_layout.addItem(QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum), 1, 2, 1, 1)
    self.drop_grid_layout.addItem(QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum,
                                                        QtWidgets.QSizePolicy.Expanding), 2, 1, 1, 1)
    self.drop_grid_layout_2.addWidget(self.drop_frame, 1, 1, 1, 1)
    self.drop_grid_layout_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Minimum), 1, 2, 1, 1)
    self.drop_grid_layout_2.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                          QtWidgets.QSizePolicy.Expanding), 2, 1, 1, 1)
    self.gridLayout.addLayout(self.drop_grid_layout_2, 0, 0, 1, 1)
    self.drop_frame.leftClick.connect(self.open_file)
    self.drop_frame.dropFile.connect(self.open_file)
    self.drop_frame.manyFiles.connect(lambda: too_many_files(self))


def populate_tree_widget(variable_list, variable_dict):
    variable_list.clear()
    for item in sorted(list(variable_dict.keys())):
        if isinstance(variable_dict[item][0], EgadsData):
            item_type = 'dataset'
        else:
            item_type = 'group'
        if item[0] == '/':
            item = item[1:]
        root_item = None
        for i, subitem in enumerate(item.split('/')):
            if i == 0:
                existing_item = variable_list.findItems(subitem, QtCore.Qt.MatchExactly)
                if not existing_item:
                    widget = QtWidgets.QTreeWidgetItem()
                    widget.setText(0, subitem)
                    widget.setToolTip(0, item_type + ': ' + item)
                    variable_list.addTopLevelItem(widget)
                    root_item = widget
                else:
                    root_item = existing_item[0]
            else:
                child_count = root_item.columnCount()
                if child_count == 0:
                    widget = QtWidgets.QTreeWidgetItem()
                    widget.setText(0, subitem)
                    widget.setToolTip(0, item_type + ': ' + item)
                    root_item.addChild(widget)
                    root_item = widget
                else:
                    child_found = False
                    for j in range(child_count):
                        child = root_item.child(j)
                        if child is not None:
                            if child.text(0) == subitem:
                                root_item = child
                                child_found = True
                                break
                    if not child_found:
                        widget = QtWidgets.QTreeWidgetItem()
                        widget.setText(0, subitem)
                        widget.setToolTip(0, item_type + ': ' + item)
                        root_item.addChild(widget)
                        root_item = widget


def read_set_attribute_gui(gui_object, attr_name, attr_dict=None):
    logging.debug('gui - old_gui_global_functions.py - read_set_attribute_gui')
    if attr_dict is not None:
        try:
            value = attr_dict[attr_name]
        except KeyError:
            value = ''
        if isinstance(value, list):
            long_string = ''
            for string in value:
                if isinstance(string, int):
                    long_string += str(string) + '-'
                else:
                    long_string += string + ', '
            if long_string[-1:] == '-':
                value = long_string[:-1]
            else:
                value = long_string[:-2]
        try:
            gui_object.setText(str(value))
            if not isinstance(gui_object, QtWidgets.QLabel):
                gui_object.setCursorPosition(0)
        except AttributeError:
            gui_object.setPlainText(str(value))
    else:
        try:
            gui_object.setText(str(attr_name))
            if not isinstance(gui_object, QtWidgets.QLabel):
                gui_object.setCursorPosition(0)
        except AttributeError:
            gui_object.setPlainText(str(attr_name))


def modify_attribute_gui_global(self, click):
    button = self.sender()
    attr = button.objectName()[4: -3]
    line = self.findChild(QtWidgets.QLineEdit, button.objectName()[:-2] + 'ln')
    if not line:
        line = self.findChild(QtWidgets.QPlainTextEdit, button.objectName()[:-2] + 'ln')
    if not line.isEnabled():
        if click == 'left':
            line.setEnabled(True)
            button.setIcon(icon_creation_function('save_as_icon.svg'))
    else:
        if self.file_ext == 'NASA Ames Files (*.na)':
            attr = attr.upper()
        if click == 'left':
            try:
                self.list_of_global_attributes[attr] = str(line.text())
            except AttributeError:
                self.list_of_global_attributes[attr] = str(line.toPlainText())
            self.start_status_bar_msg_thread('Global attributes have been modified...')
            self.modified = True
            self.make_window_title()
            line.setEnabled(False)
            button.setIcon(icon_creation_function('edit_icon.svg'))
        elif click == 'right':
            line.setEnabled(False)
            button.setIcon(icon_creation_function('edit_icon.svg'))
            try:
                if isinstance(self.list_of_global_attributes[attr], list):
                    long_string = ''
                    for string in self.list_of_global_attributes[attr]:
                        if isinstance(string, int):
                            long_string += str(string) + '-'
                        else:
                            long_string += string + ', '
                    if long_string[-1:] == '-':
                        text = long_string[:-1]
                    else:
                        text = long_string[:-2]
                else:
                    text = self.list_of_global_attributes[attr]
            except KeyError:
                text = ''
            try:
                line.setText(text)
                line.setCursorPosition(0)
            except AttributeError:
                line.setPlainText(text)
            self.start_status_bar_msg_thread('The modification has been canceled...')


def modify_attribute_gui_var(self, click):
    button = self.sender()
    attr = button.objectName()[4:-3]
    line = self.findChild(QtWidgets.QLineEdit, button.objectName()[:-2] + 'ln')
    if not line:
        line = self.findChild(QtWidgets.QPlainTextEdit, button.objectName()[:-2] + 'ln')
    if not line.isEnabled():
        if click == 'left':
            line.setEnabled(True)
            button.setIcon(icon_creation_function('save_as_icon.svg'))
    else:
        if self.tab_view.currentIndex() == 1:
            variable_list = self.variable_list
            variable_dict = self.list_of_variables_and_attributes
        else:
            variable_list = self.new_variable_list
            variable_dict = self.list_of_new_variables_and_attributes
        path, _ = full_path_name_from_treewidget(variable_list)
        if click == 'left':
            if attr == 'varname' or attr == 'groupname':
                parent = str(pathlib.PurePosixPath(path).parent)
                if parent == '/':
                    parent = ''
                new_path = parent + '/' + str(line.text())
                variable_dict[new_path] = variable_dict.pop(path)

                if variable_dict[new_path][2]:
                    for var, value in variable_dict.items():
                        dim_dict = value[1]
                        modified = False
                        for dim_path in dim_dict:
                            if dim_path == path:
                                dim_dict[new_path] = dim_dict.pop(path)
                                modified = True
                        if modified:
                            variable_dict[var][1] = dim_dict
                    dimensions_str = ''
                    for key, value in variable_dict[new_path][1].items():
                        dimensions_str = dimensions_str + str(value) + ' (' + os.path.basename(key) + '), '
                    read_set_attribute_gui(self.var_dimensions_ln, dimensions_str[:-2])

                variable_list.currentItem().setText(0, str(line.text()))
                if attr == 'groupname':
                    replace_old_path_by_new_path(variable_dict, path, new_path)
                    replace_old_path_by_new_path_tooltip(variable_list, new_path)
            else:
                try:
                    variable_dict[path][0].metadata[attr] = str(line.text())
                except AttributeError:
                    variable_dict[path][0].metadata[attr] = str(line.toPlainText())
            self.start_status_bar_msg_thread('Variable attributes have been modified...')
            self.modified = True
            self.make_window_title()
            line.setEnabled(False)
            button.setIcon(icon_creation_function('edit_icon.svg'))
        elif click == 'right':
            line.setEnabled(False)
            button.setIcon(icon_creation_function('edit_icon.svg'))
            if attr == 'varname' or attr == 'groupname':
                line.setText(variable_list.selectedItems()[0].text(0))
            else:
                try:
                    line.setText(variable_dict[path][0].metadata[attr])
                    line.setCursorPosition(0)
                except KeyError:
                    line.setText('')


def clear_var_metadata_layout(self):
    var_list, container = None, None
    if self.tab_view.currentIndex() == 1:
        var_list = self.variable_list
        container = self.metadata_container
    elif self.tab_view.currentIndex() == 2:
        var_list = self.new_variable_list
        container = self.new_metadata_container
    if not var_list.selectedItems():
        clear_layout(container)


def update_icons_state(self):
    logging.debug('gui - gui_global_functions.py - update_icons_state')
    if not self.file_is_opened:
        self.actionSeparator.setText('')
        self.actionSeparator2.setText('')
        self.actionSeparator3.setText('')
        self.actionSeparator4.setText('')
        self.actionSeparator5.setText('')
        self.actionSeparator5.setVisible(False)
        self.actionUpdate.setVisible(False)
        self.actionOpenBar.setEnabled(True)
        self.actionSaveAsBar.setEnabled(False)
        self.actionCloseBar.setEnabled(False)
        self.actionAlgorithmsBar.setEnabled(False)
        self.actionCreatealgorithmBar.setEnabled(True)
        self.actionCreateVariableBar.setEnabled(False)
        self.actionDeleteVariableBar.setEnabled(False)
        self.actionMigrateVariableBar.setEnabled(False)
        self.actionGlobalAttributesBar.setEnabled(False)
        self.actionVariableAttributesBar.setEnabled(False)
        self.actionDisplayBar.setEnabled(False)
        self.actionPlotBar.setEnabled(False)
        self.actionCreate_group.setEnabled(False)
    else:
        self.actionSaveAsBar.setEnabled(True)
        self.actionCloseBar.setEnabled(True)
        self.actionExport.setEnabled(True)
        self.actionAlgorithmsBar.setEnabled(True)
        self.actionGlobalAttributesBar.setEnabled(True)
        self.actionCreateVariableBar.setEnabled(True)
        if self.file_ext in ['NetCDF Files (*.nc *.cdf)', 'Hdf Files (*.h5 *.hdf5 *.he5)']:
            self.actionCreate_group.setEnabled(True)
        else:
            self.actionCreate_group.setEnabled(False)
        if self.tab_view.currentIndex() == 0:
            self.actionDeleteVariableBar.setEnabled(False)
            self.actionMigrateVariableBar.setEnabled(False)
            self.actionVariableAttributesBar.setEnabled(False)
            self.actionDisplayBar.setEnabled(False)
            self.actionPlotBar.setEnabled(False)
        else:
            if self.tab_view.currentIndex() == 1:
                variable_list = self.variable_list
                self.actionMigrateVariableBar.setEnabled(False)
            else:
                variable_list = self.new_variable_list
                self.actionMigrateVariableBar.setEnabled(True)
            if len(variable_list.selectedItems()) > 1:
                dataset_exist = False
                for widget in variable_list.selectedItems():
                    if 'dataset' in widget.toolTip(0):
                        dataset_exist = True
                self.actionDeleteVariableBar.setEnabled(True)
                self.actionVariableAttributesBar.setEnabled(False)
                self.actionDisplayBar.setEnabled(False)
                if dataset_exist:
                    self.actionPlotBar.setEnabled(True)
                else:
                    self.actionPlotBar.setEnabled(False)
            elif len(variable_list.selectedItems()) == 1:
                widget = variable_list.selectedItems()[0]
                if 'group' in widget.toolTip(0):
                    self.actionDeleteVariableBar.setEnabled(True)
                    self.actionVariableAttributesBar.setEnabled(True)
                    self.actionDisplayBar.setEnabled(False)
                    self.actionPlotBar.setEnabled(False)
                else:
                    self.actionDeleteVariableBar.setEnabled(True)
                    self.actionVariableAttributesBar.setEnabled(True)
                    self.actionDisplayBar.setEnabled(True)
                    self.actionPlotBar.setEnabled(True)
            else:
                self.actionDeleteVariableBar.setEnabled(False)
                self.actionMigrateVariableBar.setEnabled(False)
                self.actionVariableAttributesBar.setEnabled(False)
                self.actionDisplayBar.setEnabled(False)
                self.actionPlotBar.setEnabled(False)


def update_edit_icon_state(self):
    if self.tab_view.currentIndex() == 1:
        if 'dataset' in self.variable_list.selectedItems()[0].toolTip(0):
            if self.file_ext in ['NetCDF Files (*.nc *.cdf)', 'Hdf Files (*.h5 *.hdf5 *.he5)']:
                self.var_long_name_bt.setIcon(icon_creation_function('edit_icon.svg'))
                self.var_Category_bt.setIcon(icon_creation_function('edit_icon.svg'))
                self.var_long_name_bt.setEnabled(True)
                self.var_Category_bt.setEnabled(True)
                self.var_long_name_ln.setEnabled(False)
                self.var_Category_ln.setEnabled(False)
            self.var_varname_bt.setIcon(icon_creation_function('edit_icon.svg'))
            self.var_varname_bt.setEnabled(True)
            self.var_varname_ln.setEnabled(False)
        else:
            self.var_groupname_bt.setIcon(icon_creation_function('edit_icon.svg'))
            self.var_groupname_bt.setEnabled(True)
            self.var_groupname_ln.setEnabled(False)

    elif self.tab_view.currentIndex() == 2:
        if 'dataset' in self.new_variable_list.selectedItems()[0].toolTip(0):
            self.new_varname_bt.setIcon(icon_creation_function('edit_icon.svg'))
            self.new_long_name_bt.setIcon(icon_creation_function('edit_icon.svg'))
            self.new_Category_bt.setIcon(icon_creation_function('edit_icon.svg'))
            self.new_varname_bt.setEnabled(True)
            self.new_long_name_bt.setEnabled(True)
            self.new_Category_bt.setEnabled(True)
            self.new_varname_ln.setEnabled(False)
            self.new_long_name_ln.setEnabled(False)
            self.new_Category_ln.setEnabled(False)
        else:
            self.new_groupname_bt.setIcon(icon_creation_function('edit_icon.svg'))
            self.new_groupname_bt.setEnabled(True)
            self.new_groupname_ln.setEnabled(False)


def status_bar_update(self):
    logging.debug('gui - old_gui_global_functions.py - status_bar_update')
    if self.file_is_opened:
        filename = pathlib.PurePath(self.file_name).name
        filesize = humansize(pathlib.Path(self.file_name).stat().st_size)
        filetype = ''
        conventions = ''
        if self.file_ext == 'NetCDF Files (*.nc *.cdf)':
            filetype = 'NetCDF'
            conventions = None
            for conv in ['Conventions', 'Convention', 'conventions', 'convention']:
                if conv in self.list_of_global_attributes.keys():
                    conventions = self.list_of_global_attributes[conv]
                    break
            if conventions is None:
                logging.debug('gui - gui_global_functions.py - status_bar_update : no conventions')
                conventions = 'no conventions'
        elif self.file_ext == 'Hdf Files (*.h5 *.hdf5 *.he5)':
            filetype = 'Hdf5'
            conventions = None
            for conv in ['Conventions', 'Convention', 'conventions', 'convention']:
                if conv in self.list_of_global_attributes.keys():
                    conventions = self.list_of_global_attributes[conv]
                    break
            if conventions is None:
                logging.debug('gui - gui_global_functions.py - status_bar_update : no conventions')
                conventions = 'no conventions'
        elif self.file_ext == 'NASA Ames Files (*.na)':
            filetype = 'NASA Ames'
            conventions = 'NASA Ames file conventions'
        self.default_message = filename + '   |   ' + filesize + '   |   ' + filetype + '   |   ' + conventions
    else:
        self.default_message = ''
    self.statusBar.showMessage(self.default_message)


def create_quick_access_menu(self):
    self.menuQuick_access.clear()
    self.menuQuick_access.setEnabled(True)
    font = font_creation_function('normal')
    icon = icon_creation_function('quick_access_icon.svg')
    f = open(str(pathlib.Path(self.user_path).joinpath('user_folder_list.xml')), 'r')
    doc = xml.dom.minidom.parse(f)
    folders = doc.getElementsByTagName('Folders')[0]
    nodes = folders.getElementsByTagName('Folder')
    for node in nodes:
        quick_folder = QtWidgets.QAction(self)
        quick_folder.setIcon(icon)
        quick_folder.setFont(font)
        quick_folder.setText(get_element_value(node, 'Name'))
        quick_folder.setToolTip(get_element_value(node, 'Path'))
        quick_folder.triggered.connect(lambda: quick_access_open_folder(self))
        quick_folder.setObjectName(get_element_value(node, 'Name'))
        self.menuQuick_access.addAction(quick_folder)
    f.close()


def quick_access_open_folder(self):
    path = self.sender().toolTip()
    file_name, _ = self.get_file_name('open', path)
    if file_name:
        self.open_file(file_name)


def create_recent_file_menu(self):
    self.menuOpen_recent.clear()
    self.menuOpen_recent.setEnabled(True)
    if self.opened_file_list:
        font = font_creation_function('normal')
        icon = icon_creation_function('del_icon.svg')
        for i, file in enumerate(self.opened_file_list):
            recent_file = QtWidgets.QAction(self)
            recent_file.setFont(font)
            recent_file.setToolTip(file)
            recent_file.setObjectName(file)
            if len(file) > 65:
                file = file[:30] + ' ... ' + file[-30:]
            recent_file.setText(file)
            recent_file.triggered.connect(lambda: open_recent_filename(self))
            self.menuOpen_recent.addAction(recent_file)
        self.menuOpen_recent.addSeparator()
        del_action = QtWidgets.QAction(self)
        del_action.setFont(font)
        del_action.setIcon(icon)
        del_action.setText('Clear the list...')
        del_action.triggered.connect(lambda: clear_file_list_in_menu(self))
        del_action.setObjectName('del_action')
        self.menuOpen_recent.addAction(del_action)


def clear_file_list_in_menu(self):
    self.opened_file_list.clear()
    create_recent_file_menu(self)


def open_recent_filename(self):
    self.open_file(self.sender().objectName())


def update_dimension_attribute_gui(self, dim_dict):
    dimensions_str = ''
    for key, value in dim_dict.items():
        dimensions_str = dimensions_str + str(value) + ' (' + os.path.basename(key) + '), '
    read_set_attribute_gui(self.var_dimensions_ln, dimensions_str[:-2])