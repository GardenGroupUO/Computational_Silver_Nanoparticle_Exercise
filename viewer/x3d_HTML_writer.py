import os
from ase.data import covalent_radii
from ase.data.colors import jmol_colors

def write_x3d_html(atoms, output):
    x3d_obj = X3D(atoms)
    x3d_obj.write(output)


class X3D:
    """Class to write either X3D (readable by open-source rendering
    programs such as Blender) or X3DOM html, readable by modern web
    browsers.
    """

    def __init__(self, atoms):
        self._atoms = atoms

    def write(self, fileobj):
        viewer_construct_filename = os.path.realpath(__file__).replace('/x3d_HTML_writer.py','')+'/'+'viewer_construct.html'
        with open(viewer_construct_filename,'r') as viewer_construct:
            for line in viewer_construct:
                if '################### Atoms Go In Here ###################' in line:
                    elements = {}
                    for atom in self._atoms:
                        for indent, line in self.atom_lines(atom, elements):
                            print(line, file=fileobj)
                else:
                    print(line.rstrip(), file=fileobj)
                
    def atom_lines(self,atom,elements):
        """Generates a segment of X3D lines representing an atom."""
        x, y, z = atom.position
        symbol = atom.symbol
        no_of_elements_currently = elements.get(symbol, 0) + 1
        elements[symbol] = no_of_elements_currently
        atom_id = symbol+str(no_of_elements_currently)
        lines = [(0, '<Transform id="transform_'+atom_id+'" translation="%.2f %.2f %.2f">' % (x, y, z))]
        lines += [(1, '<Shape DEF="'+atom_id+'">')]
        lines += [(2, '<Appearance DEF="'+atom_id+'">')]
        color = 'diffuseColor="%.3f %.3f %.3f"' % tuple(jmol_colors[atom.number])
        colour_original = 'originalColor="%.3f %.3f %.3f"' % tuple(jmol_colors[atom.number])
        lines += [(3, '<Material id="'+atom_id+'" '+color+' '+colour_original+' specularColor="0.5 0.5 0.5"></Material>')]
        #lines += [(3, '<Material id="color" %s specularColor="0.5 0.5 0.5">' % color)]

        lines += [(2, '</Appearance>')]
        lines += [(2, '<Sphere DEF="'+atom_id+'" radius="%.2f"> </Sphere>' % covalent_radii[atom.number])] # onclick="changeColor();"
        lines += [(1, '</Shape>')]
        lines += [(0, '</Transform>')]
        return lines
