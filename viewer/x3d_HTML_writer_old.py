from ase.data import covalent_radii
from ase.data.colors import jmol_colors

class WriteToFile:
    """Creates convenience function to write to a file."""

    def __init__(self, fileobj):
        self._f = fileobj

    def __call__(self, indent, line):
        text = '    ' * indent
        print('%s%s' % (text, line), file=self._f)

def write_x3d_html(atoms, output):
    x3d_obj = X3D(atoms)
    x3d_obj.write(output, datatype='X3DOM')


class X3D:
    """Class to write either X3D (readable by open-source rendering
    programs such as Blender) or X3DOM html, readable by modern web
    browsers.
    """

    def __init__(self, atoms):
        self._atoms = atoms

    def write(self, fileobj, datatype):
        """Writes output to either an 'X3D' or an 'X3DOM' file, based on
        the extension. For X3D, filename should end in '.x3d'. For X3DOM,
        filename should end in '.html'.

        Args:
            datatype - str, output format. 'X3D' or 'X3DOM'.
        """

        # Write the header
        w = WriteToFile(fileobj)
        if datatype == 'X3DOM':
            w(0, '<!DOCTYPE>')
            w(0, '<html>')
            w(1, '<head>')
            w(2, '<meta http-equiv="X-UA-Compatible" content="IE=edge"/>')
            w(2, '<title>ASE atomic visualization</title>')
            w(2, '<script type="text/javascript" src="https://www.x3dom.org/x3dom/release/x3dom.js"> </script>')
            w(2, '<link rel="stylesheet" type="text/css" href="https://www.x3dom.org/x3dom/release/x3dom.css"> </link>')
            w(2, '<script type="text/javascript" src="https://code.jquery.com/jquery-2.1.0.min.js" ></script>')
            
            w(2, '<script>')

            w(3,'//Round a float value to x.xx format')
            w(3,'function roundWithTwoDecimals(value)')
            w(3,'{')
            w(4,'return (Math.round(value * 100)) / 100;')
            w(3,'}')
            w(3,'')
            w(3,'//Handle click on any group member')
            w(3,'function handleGroupClick(event)')
            w(3,'{')
            w(4,'//Mark hitting point')
            w(4,'$("#marker").attr("translation", event.hitPnt);')
            w(4,'console.log(event);')
            
            w(4,'//Display coordinates of hitting point (rounded)')
            w(4,'var coordinates = event.hitPnt;')
            w(4,'$("#coordX").html(roundWithTwoDecimals(coordinates[0]));')
            w(4,'$("#coordY").html(roundWithTwoDecimals(coordinates[1]));')
            w(4,'$("#coordZ").html(roundWithTwoDecimals(coordinates[2]));')

            w(4,'//Change colour to highlight selected atom')
            w(4, 'var element_id = event.target.id;')
            w(4, 'if(document.getElementById(element_id).getAttribute("highlighted")=="0")')
            w(5, 'document.getElementById(element_id).setAttribute("diffuseColor", "0 0 1");')
            w(5, 'document.getElementById(element_id).setAttribute("highlighted", "1");')
            w(4, 'else')
            w(5, 'document.getElementById(element_id).setAttribute("diffuseColor", "1 0 0");')
            w(5, 'document.getElementById(element_id).setAttribute("highlighted", "0");')

            w(3,'}')
            w(3,'')
            w(3,'//Handle click on a shape')
            w(3,'function handleSingleClick(shape)')
            w(3,'{')
            w(4,'$("#lastClickedObject").html($(shape).attr("def"));')
            w(3,'}')
        
            w(3,'$(document).ready(function(){')
            w(4,'//Add a onclick callback to every shape')
            w(4,'$("shape").each(function() {')
            w(5,'$(this).attr("onclick", "handleSingleClick(this)");')
            w(4,'});')
            w(3,'});')

            '''
            w(3, 'function changeColor(event)')
            w(3, '{')
            w(4, 'var element_id = event.target.id;')
            w(4, 'if(document.getElementById(element_id).getAttribute("highlighted")=="0")')
            w(5, 'document.getElementById(element_id).setAttribute("diffuseColor", "0 0 1");')
            w(5, 'document.getElementById(element_id).setAttribute("highlighted", "1");')
            w(4, 'else')
            w(5, 'document.getElementById(element_id).setAttribute("diffuseColor", "1 0 0");')
            w(5, 'document.getElementById(element_id).setAttribute("highlighted", "0");')
            w(3, '}')
            '''


            w(2, '</script>')

            w(1, '</head>')
            w(1, '<body>')
            w(2, '<X3D  id="boxes" showStat="false" showLog="true" x="0px" y="0px" width="500px" height="500px">')
        elif datatype == 'X3D':
            w(0, '<?xml version="1.0" encoding="UTF-8"?>')
            w(0, '<!DOCTYPE X3D PUBLIC "ISO//Web3D//DTD X3D 3.2//EN" '
              '"http://www.web3d.org/specifications/x3d-3.2.dtd">')
            w(0, '<X3D profile="Interchange" version="3.2" '
              'xmlns:xsd="http://www.w3.org/2001/XMLSchema-instance" '
              'xsd:noNamespaceSchemaLocation='
              '"http://www.web3d.org/specifications/x3d-3.2.xsd">')
        else:
            raise ValueError("datatype not supported: " + str(datatype))

        w(3, '<Scene>')

        w(4, '<Viewpoint position="-2.25680 3.36560 14.62828" orientation="-0.60104 -0.28053 0.74837 0.40903"></Viewpoint>')

        w(2, '<script>')
        w(3,'function handleGroupClick(event)')
        w(3,'{')
        w(4,'//Mark hitting point')
        w(4,'$("#marker").attr("translation", event.hitPnt);')
        w(4,'console.log(event);')

        w(4,'//Display coordinates of hitting point (rounded)')
        w(4,'var coordinates = event.hitPnt;')
        w(4,'$("#coordX").html(roundWithTwoDecimals(coordinates[0]));')
        w(4,'$("#coordY").html(roundWithTwoDecimals(coordinates[1]));')
        w(4,'$("#coordZ").html(roundWithTwoDecimals(coordinates[2]));')

        w(4,'//Change colour to highlight selected atom')
        w(4, 'var element_id = event.target.id;')
        w(4, 'if(document.getElementById(element_id).getAttribute("highlighted")=="0")')
        w(5, 'document.getElementById(element_id).setAttribute("diffuseColor", "0 0 1");')
        w(5, 'document.getElementById(element_id).setAttribute("highlighted", "1");')
        w(4, 'else')
        w(5, 'document.getElementById(element_id).setAttribute("diffuseColor", "1 0 0");')
        w(5, 'document.getElementById(element_id).setAttribute("highlighted", "0");')

        w(3,'}')
        w(2, '</script>')

        w(4, '<Group onclick="handleGroupClick(event)">')

        for atom in self._atoms:
            for indent, line in self.atom_lines(atom):
                w(5 + indent, line) # was 4

        w(4, '</Group>')

        w(3, '</Scene>')

        if datatype == 'X3DOM':
            w(2, '</X3D>')

            w(2, '<div style="position:absolute;left:600px;top:70px;width:200px">')
            w(3, '<h3>Last clicked object:</h3> ')
            w(3, '<span id="lastClickedObject">-</span>')
    
            w(3, '<br><br>')
    
            w(3, '<h3>Click coordinates:</h3>')
            w(3, '<table style="font-size:1em;">')
            w(4, '<tr><td>X: </td><td id="coordX">-</td></tr>')
            w(4, '<tr><td>Y: </td><td id="coordY">-</td></tr>')
            w(4, '<tr><td>Z: </td><td id="coordZ">-</td></tr>')
            w(3, '</table>')
            w(2, '</div>')

            w(1, '</body>')
            w(0, '</html>')
        elif datatype == 'X3D':
            w(0, '</X3D>')


    def atom_lines(self,atom):
        """Generates a segment of X3D lines representing an atom."""
        x, y, z = atom.position
        lines = [(0, '<Transform translation="%.2f %.2f %.2f">' % (x, y, z))]
        lines += [(1, '<Shape DEF="'+str(atom.index)+'">')]
        lines += [(2, '<Appearance DEF="'+str(atom.index)+'">')]
        color = 'diffuseColor="%.3f %.3f %.3f"' % (1, 0, 0) #tuple(jmol_colors[atom.number])
        lines += [(3, '<Material id="'+str(atom.index)+'" highlighted=0 '+color+' ></Material>')]
        #lines += [(3, '<Material id="color" %s specularColor="0.5 0.5 0.5">' % color)]

        lines += [(2, '</Appearance>')]
        lines += [(2, '<Sphere DEF="'+str(atom.index)+'" radius="%.2f"> </Sphere>' % covalent_radii[atom.number])]
        lines += [(1, '</Shape>')]
        lines += [(0, '</Transform>')]
        return lines
