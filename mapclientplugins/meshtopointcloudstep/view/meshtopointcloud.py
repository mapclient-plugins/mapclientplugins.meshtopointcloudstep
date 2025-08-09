"""
Created: April, 2023

@author: tsalemink
"""
import os
import json
import webbrowser

import numpy as np
from PySide6 import QtWidgets, QtCore

from cmlibs.utils.zinc.finiteelement import is_field_defined_for_nodeset
from cmlibs.utils.zinc.general import rotate_to_next_standard_view
from cmlibs.widgets.collapsibleboxwidget import CollapsibleBox
from cmlibs.widgets.ui.ui_buttonswidget import Ui_Buttons
from cmlibs.zinc.field import Field

from cmlibs.widgets.handlers.scenemanipulation import SceneManipulation

from mapclientplugins.meshtopointcloudstep.view.ui_meshtopointcloudwidget import Ui_MeshToPointCloud
from mapclientplugins.meshtopointcloudstep.view.ui_configurationwidget import Ui_Configuration
from mapclientplugins.meshtopointcloudstep.view.ui_displaysettingswidget import Ui_DisplaySettings
from mapclientplugins.meshtopointcloudstep.view.ui_statisticswidget import Ui_Statistics
from mapclientplugins.meshtopointcloudstep.scene.meshtopointcloud import MeshToPointCloudScene


class ZincFieldListModel(QtCore.QAbstractListModel):

    def __init__(self):
        super().__init__()
        self._fields = []

    def rowCount(self, parent=...):
        return len(self._fields)

    def data(self, index, role=...):
        if index.isValid():
            if role == QtCore.Qt.ItemDataRole.DisplayRole:
                return self._fields[index.row()].getName()
            elif role == QtCore.Qt.ItemDataRole.UserRole:
                return self._fields[index.row()]

    def populate(self, fields):
        self._fields = fields


def _get_coordinate_fields(region):
    fm = region.getFieldmodule()
    fi = fm.createFielditerator()
    field = fi.next()
    field_list = []
    while field.isValid():
        if field.isTypeCoordinate() and (field.getNumberOfComponents() == 3) and (field.castFiniteElement().isValid()):
            field_list.append(field)

        field = fi.next()

    return field_list


def _documentation_clicked():
    webbrowser.open("https://abi-mapping-tools.readthedocs.io/en/latest/mapclientplugins.meshtopointcloud/docs/index.html")


class MeshToPointCloudWidget(QtWidgets.QMainWindow):

    def __init__(self, model, parent=None):
        super(MeshToPointCloudWidget, self).__init__(parent)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self._model = model

        self._ui = Ui_MeshToPointCloud()
        self._ui.setupUi(self)

        self._setup_dock_widget()

        self._location = None
        self._callback = None
        self._standardise_output = False
        self._plane_handlers_registered = False
        self._coordinate_field_list = []

        self._scene = MeshToPointCloudScene(model)

        self._make_connections()

        self._ui.widgetZinc.set_grab_focus(True)
        self._ui.widgetZinc.set_context(model.get_context())
        self._ui.widgetZinc.register_handler(SceneManipulation())

        self._update_ui()

    def _setup_dock_widget(self):
        parent_widget = QtWidgets.QWidget(self)

        layout = QtWidgets.QVBoxLayout(parent_widget)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)

        self._identifier_label = QtWidgets.QLabel("Identifier: XXXX")
        layout.addWidget(self._identifier_label)

        self._configuration_ui = Ui_Configuration()
        self._display_settings_ui = Ui_DisplaySettings()
        self._statistics_ui = Ui_Statistics()
        self._buttons_ui = Ui_Buttons()

        for ui in [self._configuration_ui, self._statistics_ui, self._display_settings_ui]:
            form_container = QtWidgets.QWidget()
            ui.setupUi(form_container)
            tools_box = CollapsibleBox(form_container.windowTitle(), checked=True if ui is self._configuration_ui else False)
            tools_box.add_widget(form_container)
            layout.addWidget(tools_box, stretch=1)

        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        layout.addSpacerItem(spacer)

        form_container = QtWidgets.QWidget()
        self._buttons_ui.setupUi(form_container)
        layout.addWidget(form_container)

        self._dock_widget = QtWidgets.QDockWidget("Controls", self)
        self._dock_widget.setObjectName("ControlsDock")
        self._dock_widget.setWidget(parent_widget)

        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea, self._dock_widget)

    def load(self, mesh_file_location):
        self._scene.setup_visualisation()
        self._scene.create_mesh_surface()
        self._load_settings()

        self._identifier_label.setText(f"Identifier: {self._model.get_identifier()}")
        self._model.load(mesh_file_location)

        self._coordinate_field_list = _get_coordinate_fields(self._model.get_mesh_region())
        self._setup_field_combo_boxes()
        self._update_ui()

    def set_location(self, location):
        self._location = location

    def get_output_file(self):
        return self._model.output_point_cloud_filename()

    def register_done_execution(self, done_execution):
        self._callback = done_execution

    def _make_connections(self):
        self._buttons_ui.done_pushButton.clicked.connect(self._continue_execution)
        self._buttons_ui.viewAll_pushButton.clicked.connect(self._view_all_button_clicked)
        self._buttons_ui.stdViews_pushButton.clicked.connect(self._standard_views_clicked)
        self._buttons_ui.pushButtonDocumentation.clicked.connect(_documentation_clicked)
        self._ui.widgetZinc.graphics_initialized.connect(self._zinc_widget_ready)
        self._ui.widgetZinc.pixel_scale_changed.connect(self._pixel_scale_changed)
        self._display_settings_ui.checkBoxSurfacesVisibility.stateChanged.connect(self._scene.set_surfaces_visibility)
        self._display_settings_ui.checkBoxPointsVisibility.stateChanged.connect(self._scene.set_points_visibility)
        self._display_settings_ui.spinBoxNodeSize.valueChanged.connect(self._scene.set_node_size)
        self._configuration_ui.pushButtonSample.clicked.connect(self._sample)

    def _update_ui(self):
        surface_graphics_available = self._scene.are_surface_graphics_available()
        point_graphics_available = self._scene.are_point_graphics_available()
        self._display_settings_ui.checkBoxSurfacesVisibility.setEnabled(surface_graphics_available)
        self._display_settings_ui.checkBoxPointsVisibility.setEnabled(point_graphics_available)

    def _sample(self):
        self._model.sample(self._configuration_ui.doubleSpinBoxSamplingDensity.value())
        self._update_ui()

    def _setup_field_combo_boxes(self):
        node_fields = []
        for field in self._coordinate_field_list:
            if is_field_defined_for_nodeset(field, nodeset_domain=Field.DOMAIN_TYPE_NODES):
                node_fields.append(field)

        node_model = ZincFieldListModel()
        node_model.populate(node_fields)

        self._configuration_ui.comboBoxCoordinateField.setModel(node_model)
        self._configuration_ui.comboBoxCoordinateField.currentTextChanged.connect(self._update_coordinates_field)
        self._update_coordinates_field()

    def _update_coordinates_field(self):
        self._model.set_mesh_coordinates(self._configuration_ui.comboBoxCoordinateField.currentData())
        self._scene.update_mesh_coordinates(self._configuration_ui.comboBoxCoordinateField.currentData())
        minima, maxima = self._model.evaluate_nodes_minima_and_maxima()
        self._populate_statistics_ui(minima, maxima)

    def _populate_statistics_ui(self, minima, maxima):
        self._statistics_ui.lineEditComponent1Min.setText(f"{minima[0]:.3f}")
        self._statistics_ui.lineEditComponent2Min.setText(f"{minima[1]:.3f}")
        self._statistics_ui.lineEditComponent3Min.setText(f"{minima[2]:.3f}")
        self._statistics_ui.lineEditComponent1Max.setText(f"{maxima[0]:.3f}")
        self._statistics_ui.lineEditComponent2Max.setText(f"{maxima[1]:.3f}")
        self._statistics_ui.lineEditComponent3Max.setText(f"{maxima[2]:.3f}")

    def _settings_file(self):
        return os.path.join(self._location, 'settings.json')

    def _write(self):
        if not os.path.exists(self._location):
            os.makedirs(self._location)

        self._model.write_point_cloud(self._location)

    def _zinc_widget_ready(self):
        pass

    def _pixel_scale_changed(self, scale):
        self._scene.set_pixel_scale(scale)

    def _view_all_button_clicked(self):
        self._ui.widgetZinc.view_all()

    def _standard_views_clicked(self):
        rotate_to_next_standard_view(self._ui.widgetZinc.get_zinc_sceneviewer())

    def _continue_execution(self):
        try:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
            self._dock_widget.setFloating(False)
            self._save_settings()
            self._write()
            self._callback()
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    def _load_settings(self):
        settings = {}
        if os.path.isfile(self._settings_file()):
            with open(self._settings_file()) as f:
                settings = json.load(f)

        self._display_settings_ui.spinBoxNodeSize.setValue(settings.get("node_size", 2.0))
        self._configuration_ui.doubleSpinBoxSamplingDensity.setValue(settings.get("density", 1.0))

    def _save_settings(self):
        if not os.path.exists(self._location):
            os.makedirs(self._location)

        settings = {
            "node_size": self._display_settings_ui.spinBoxNodeSize.value(),
            "density": self._configuration_ui.doubleSpinBoxSamplingDensity.value(),
        }

        with open(self._settings_file(), "w") as f:
            json.dump(settings, f)
