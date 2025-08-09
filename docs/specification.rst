.. _mcp-mesh-to-point-cloud-specification:

Ports
-----

This plugin:

* **uses**:

  * *http://physiomeproject.org/workflow/1.0/rdf-schema#file_location*, or
  * *http://physiomeproject.org/workflow/1.0/rdf-schema#ex_file*

and

* **provides**:

  * *http://physiomeproject.org/workflow/1.0/rdf-schema#file_location*, or
  * *http://physiomeproject.org/workflow/1.0/rdf-schema#exf_file*

The **uses** port imports a `Zinc` EXF file defining the input mesh.
The **provides** port outputs a `Zinc` EXF file of datapoints sampled over the input mesh.
