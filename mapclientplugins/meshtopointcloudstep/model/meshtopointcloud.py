import os

from cmlibs.maths.vectorops import add, cross, magnitude, matrix_vector_mult, angle, axis_angle_to_rotation_matrix, mult, sub
from cmlibs.utils.zinc.field import create_field_coordinates, findOrCreateFieldGroup
from cmlibs.utils.zinc.finiteelement import evaluate_field_nodeset_range, create_square_element
from cmlibs.utils.zinc.general import ChangeManager
from cmlibs.utils.zinc.node import project_nodes, rotate_nodes, translate_nodes, get_field_values
from cmlibs.utils.geometry.plane import ZincPlane
from cmlibs.utils.zinc.region import write_to_buffer, read_from_buffer
from cmlibs.zinc.context import Context
from cmlibs.zinc.field import Field


class MeshToPointCloud(object):

    def __init__(self):
        self._mesh = None
        self._mesh_coordinates_field = None
        self._identifier = None
        self._mesh_file_location = None

        self._context = Context("Mesh")
        self._output_context = Context("OutputPointCloud")
        self._root_region = self._context.getDefaultRegion()

        self._mesh_region = self._root_region.createChild("mesh")
        self._output_point_cloud = self._root_region.createChild("point_cloud")

        self.define_standard_materials()
        self.define_standard_glyphs()

    def load(self, mesh_file_location, mesh_coordinates_name=None):
        fm = self._mesh_region.getFieldmodule()
        with ChangeManager(fm):
            self._mesh_region.readFile(mesh_file_location)
            if mesh_coordinates_name is not None:
                potential_coordinates_field = fm.findFieldByName(mesh_coordinates_name).castFiniteElement()
                if potential_coordinates_field.isValid():
                    self._mesh_coordinates_field = potential_coordinates_field
        self._mesh_file_location = mesh_file_location

    def set_identifier(self, identifier):
        self._identifier = identifier

    def get_identifier(self):
        return self._identifier

    def get_root_region(self):
        return self._root_region

    def get_context(self):
        return self._context

    def get_output_context(self):
        return self._output_context

    def get_mesh_coordinates(self):
        return self._mesh_coordinates_field

    def set_mesh_coordinates(self, coordinates):
        self._mesh_coordinates_field = coordinates

    def get_mesh_region(self):
        return self._mesh_region

    def get_mesh(self):
        return self._mesh

    def _create_selection_filter(self):
        m = self._context.getScenefiltermodule()
        # r1 = m.createScenefilterRegion(self._detection_model.get_region())
        # r2 = m.createScenefilterRegion(self._marker_model.get_region())
        o = m.createScenefilterOperatorOr()
        # o.appendOperand(r1)
        # o.appendOperand(r2)
        return o

    def define_standard_glyphs(self):
        """
        Helper method to define the standard glyphs
        """
        self._context.getGlyphmodule().defineStandardGlyphs()
        self._output_context.getGlyphmodule().defineStandardGlyphs()

    def define_standard_materials(self):
        """
        Helper method to define the standard materials.
        """
        self._context.getMaterialmodule().defineStandardMaterials()
        self._output_context.getMaterialmodule().defineStandardMaterials()

    def evaluate_nodes_minima_and_maxima(self):
        fm = self._mesh_region.getFieldmodule()
        nodes = fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        return evaluate_field_nodeset_range(self._mesh_coordinates_field, nodes)

    def mesh_nodes_coordinates(self):
        return get_field_values(self._mesh_region, self._mesh_coordinates_field)

    def have_data_points(self):
        fm = self._mesh_region.getFieldmodule()
        datapoints = fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        return datapoints.isValid() and datapoints.getSize() > 0

    def sample(self, point_density=1.0):
        """
        Sample the mesh region to create a point cloud.
        :param point_density: The density of points to sample.
        :return: A node set containing the sampled points.
        """
        fm = self._mesh_region.getFieldmodule()
        datapoints = fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        coordinates = self._mesh_coordinates_field
        # data_group = findOrCreateFieldGroup(fm, name="point_cloud_data")
        # data_nodes_group = data_group.getOrCreateNodesetGroup(datapoints)
        datapoints.destroyAllNodes()
        graphics_filter = self._context.getScenefiltermodule().getDefaultScenefilter()
        self._mesh_region.getScene().convertToPointCloud(graphics_filter, datapoints, coordinates, 0.0, 0.0, point_density, 1.0)

    def output_point_cloud_filename(self):
        """
        Generate the output filename for the point cloud.
        :return: The output filename.
        """
        if not self._identifier:
            raise ValueError("Identifier must be set before generating the output filename.")

        return f"{self._identifier.lower()}-point-cloud.exf"

    def write_point_cloud(self, output_location):
        """
        Write the point cloud to a file.
        :param output_location: The location where the point cloud file will be saved.
        """
        output_file = self.output_point_cloud_filename()
        buffer = write_to_buffer(self._mesh_region, resource_domain_type=Field.DOMAIN_TYPE_DATAPOINTS)
        with open(os.path.join(output_location, output_file), 'wb') as f:
            f.write(buffer)
