from cmlibs.utils.zinc.general import ChangeManager
from cmlibs.zinc.field import Field
from cmlibs.zinc.glyph import Glyph
from cmlibs.zinc.graphics import Graphics


def _set_graphic_point_size(graphic, size):
    attributes = graphic.getGraphicspointattributes()
    attributes.setBaseSize(size)


def _create_surface_graphics(region):
    scene = region.getScene()
    surfaces = scene.createGraphicsSurfaces()
    surfaces.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_SHADED)
    surfaces.setVisibilityFlag(True)

    field_module = region.getFieldmodule()
    coordinates = field_module.findFieldByName("coordinates")
    surfaces.setCoordinateField(coordinates)

    return surfaces


class MeshToPointCloudScene(object):

    def __init__(self, model):
        self._model = model
        self._surface_graphics = None
        self._surface_material = None
        self._node_graphics = None
        self._pixel_scale = 1
        self._data_point_base_size = 0.15

    def setup_visualisation(self):
        if self._node_graphics is None:
            mesh_region = self._model.get_mesh_region()
            scene = mesh_region.getScene()

            with ChangeManager(scene):
                mm = scene.getMaterialmodule()
                blue = mm.findMaterialByName('blue')

                self._surface_material = mm.findMaterialByName('white')
                self._node_graphics = self.create_point_graphics(scene, None, None, blue, Field.DOMAIN_TYPE_DATAPOINTS)

    def create_point_graphics(self, scene, finite_element_field, subgroup_field, material, domain, mode=Graphics.SELECT_MODE_DRAW_UNSELECTED):
        with ChangeManager(scene):
            graphic = scene.createGraphicsPoints()
            graphic.setFieldDomainType(domain)

            if finite_element_field:
                graphic.setCoordinateField(finite_element_field)

            graphic.setSelectMode(mode)

            if subgroup_field:
                graphic.setSubgroupField(subgroup_field)
                graphic.setName(subgroup_field.getName())

            if material:
                graphic.setMaterial(material)

            attributes = graphic.getGraphicspointattributes()
            attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
            _set_graphic_point_size(graphic, self._data_point_base_size * self._pixel_scale)

        return graphic

    def update_mesh_coordinates(self, coordinate_field):
        self._node_graphics.setCoordinateField(coordinate_field)
        self._surface_graphics.setCoordinateField(coordinate_field)

    def set_pixel_scale(self, scale):
        self._pixel_scale = scale
        self._update_graphic_point_size()

    def _update_graphic_point_size(self):
        _set_graphic_point_size(self._node_graphics, self._data_point_base_size * self._pixel_scale)

    def get_node_size(self):
        return self._data_point_base_size

    def set_node_size(self, size):
        self._data_point_base_size = size
        self._update_graphic_point_size()

    def are_surface_graphics_available(self):
        return self._surface_graphics is not None and self._surface_graphics.isValid()

    def are_point_graphics_available(self):
        return self._node_graphics is not None and self._node_graphics.isValid() and self._model.have_data_points()

    def set_surfaces_visibility(self, state):
        self._surface_graphics.setVisibilityFlag(state != 0)

    def set_points_visibility(self, state):
        self._node_graphics.setVisibilityFlag(state != 0)

    def create_mesh_surface(self):
        region = self._model.get_mesh_region()
        self._surface_graphics = _create_surface_graphics(region)
        self._surface_graphics.setMaterial(self._surface_material)
