from .Structure import Structure

class PyARSA(Structure):
    """Create and modify ARSA model."""

    def __init__(self, app):
        super().__init__(app)

    def add_nodes(self, coord_array):
        """Adds nodes in the model space.
        Parameters:
        coord_array(numpy.array): [node_number, X, Y, Z]"""
        self.structure.Nodes()
        pass

    def add_bar(self):
        pass

    def add_contour(self):
        pass
