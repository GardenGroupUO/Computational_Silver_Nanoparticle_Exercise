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
    x3d_obj.write(output)


class X3D:
    """Class to write either X3D (readable by open-source rendering
    programs such as Blender) or X3DOM html, readable by modern web
    browsers.
    """

    def __init__(self, atoms):
        self._atoms = atoms

    def write(self, fileobj):

        print('<!DOCTYPE>', file=fileobj)
        print('<html>', file=fileobj)
        print('<head>', file=fileobj)
        print('    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>', file=fileobj)
        print('    <title>Chemistry Viewer</title>', file=fileobj)
        print('    <script type="text/javascript" src="https://www.x3dom.org/download/x3dom.js"> </script>', file=fileobj)
        print('    <link rel="stylesheet" type="text/css" href="https://www.x3dom.org/download/x3dom.css"/>', file=fileobj)
        print('     <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.0.min.js" ></script>', file=fileobj)
        print('    ', file=fileobj)
        '''
        print('    <script>', file=fileobj)
        print('        function changeColor(element_id)', file=fileobj)
        print('        {', file=fileobj)
        #print('            var element_id = "1";', file=fileobj)
        print('            if(document.getElementById(element_id).getAttribute("highlighted")=="0")', file=fileobj)
        print('                document.getElementById(element_id).setAttribute("diffuseColor", "0 0 1");', file=fileobj)
        print('                document.getElementById(element_id).setAttribute("highlighted", "1");', file=fileobj)
        print('            else', file=fileobj)
        print('                document.getElementById(element_id).setAttribute("highlighted", "1 0 0");', file=fileobj)
        print('                document.getElementById(element_id).setAttribute("highlighted", "0");', file=fileobj)
        print('        }', file=fileobj)
        print('    </script>', file=fileobj)
        '''
        print('    <script>', file=fileobj)
        print('        //Round a float value to x.xx format', file=fileobj)
        print('        function roundWithTwoDecimals(value)', file=fileobj)
        print('        {', file=fileobj)
        print('            return (Math.round(value * 1000)) / 1000;', file=fileobj)
        print('        }', file=fileobj)
        print('    ', file=fileobj)
        print('        //Handle click on any group member', file=fileobj)
        print('        function handleGroupClick(event)', file=fileobj)
        print('        {', file=fileobj)
        print('            //Mark hitting point', file=fileobj)
        print('            $("#marker").attr("translation", event.hitPnt);', file=fileobj)
        print('            console.log(event);', file=fileobj)
        print('            ', file=fileobj)
        print('            //Display coordinates of hitting point (rounded)', file=fileobj)
        print('            var coordinates = event.hitPnt;', file=fileobj)
        #print('            $("#coordX").html(roundWithTwoDecimals(coordinates[0]));', file=fileobj)
        #print('            $("#coordY").html(roundWithTwoDecimals(coordinates[1]));', file=fileobj)
        #print('            $("#coordZ").html(roundWithTwoDecimals(coordinates[2]));', file=fileobj)
        print('        }', file=fileobj)
        print('        ', file=fileobj)
        print('        //Handle click on a shape', file=fileobj)
        print('        var highlighted_atoms = ["None", "None"]')
        print('        function handleSingleClick(shape)', file=fileobj)
        print('        {', file=fileobj)
        print('            $("#lastClickedObject").html($(shape).attr("def"));', file=fileobj)
        print('            var oldMaterial = $(shape).attr("def");', file=fileobj) # gets the id of shape
        print('            console.log("The new value is " + oldMaterial);', file=fileobj)

        print('            if(document.getElementById(oldMaterial).getAttribute("highlighted")=="0"){', file=fileobj)
        print('                document.getElementById(oldMaterial).setAttribute("diffuseColor", "0 0 1");', file=fileobj)
        print('                document.getElementById(oldMaterial).setAttribute("highlighted", "1");', file=fileobj)
        print('                if ')
        print('                highlighted_atoms')
        print('            }else{', file=fileobj)
        print('                var original_atom_color = document.getElementById(oldMaterial).getAttribute("originalColor");', file=fileobj)
        print('                document.getElementById(oldMaterial).setAttribute("diffuseColor", original_atom_color);', file=fileobj)
        print('                document.getElementById(oldMaterial).setAttribute("highlighted", "0");', file=fileobj)
        print('            }', file=fileobj)
        print('            var atom_centre_position_str = document.getElementById("transform_"+oldMaterial).getAttribute("translation");', file=fileobj)
        print('            var atom_centre_position = atom_centre_position_str.split(" ").map(Number);', file=fileobj)
        print('            $("#coordX").html(roundWithTwoDecimals(atom_centre_position[0]));', file=fileobj)
        print('            $("#coordY").html(roundWithTwoDecimals(atom_centre_position[1]));', file=fileobj)
        print('            $("#coordZ").html(roundWithTwoDecimals(atom_centre_position[2]));', file=fileobj)

        print('        }', file=fileobj)
        print('        ', file=fileobj)
        print('        $(document).ready(function(){', file=fileobj)
        print('            //Add a onclick callback to every shape', file=fileobj)
        print('            $("shape").each(function() { $(this).attr("onclick", "handleSingleClick(this)"); });', file=fileobj)
        print('        });', file=fileobj)
        print('    </script>', file=fileobj)
        print('', file=fileobj)
        print('<style type="text/css">', file=fileobj)
        print('    #demo_table {', file=fileobj)
        print('        border:0;', file=fileobj)
        print('    }', file=fileobj)
        print('    #demo_table img {', file=fileobj)
        print('        width:128px;', file=fileobj)
        print('        height:128px;', file=fileobj)
        print('    }', file=fileobj)
        print('    #demo_table td img', file=fileobj)
        print('    {', file=fileobj)
        print('        border:1px solid grey;', file=fileobj)
        print('        text-decoration:none;', file=fileobj)
        print('    }', file=fileobj)
        print('', file=fileobj)
        print('     #screenshotPreviews > img {', file=fileobj)
        print('        width:250px;', file=fileobj)
        print('        margin-left:25px;', file=fileobj)
        print('        margin-right:25px;', file=fileobj)
        print('     }', file=fileobj)
        print('</style>', file=fileobj)
        print('    <script type="text/javascript" charset="utf-8">', file=fileobj)
        print('        $(document).ready(function(){', file=fileobj)
        print('            var screenshotCount = 0;', file=fileobj)
        print('    ', file=fileobj)
        print('            //Every time the user clicks on the "take screenhot" button', file=fileobj)
        print('            $("#btnTakeScreenshot").on("click", function() {', file=fileobj)
        print('                //Get data url from the runtime', file=fileobj)
        print('                var imgUrl = document.getElementById("boxes").runtime.getScreenshot();', file=fileobj)
        print('    ', file=fileobj)
        print('                //Create preview image...', file=fileobj)
        print('                var newScreenshotImage = document.createElement("img");', file=fileobj)
        print('                newScreenshotImage.src = imgUrl;', file=fileobj)
        print('                newScreenshotImage.id = "screenshot_" + screenshotCount;', file=fileobj)
        print('                $("#screenshotPreviews").append(newScreenshotImage);', file=fileobj)
        print('    ', file=fileobj)
        print('                //...and download link', file=fileobj)
        print('                var newScreenshotDownloadLink = document.createElement("a");', file=fileobj)
        print('                newScreenshotDownloadLink.href = imgUrl;', file=fileobj)
        print('                newScreenshotDownloadLink.download = "screenshot_" + screenshotCount + ".png";', file=fileobj)
        print('                newScreenshotDownloadLink.innerHTML = "Download";', file=fileobj)
        print('                $("#screenshotPreviews").append(newScreenshotDownloadLink);', file=fileobj)
        print('    ', file=fileobj)
        print('                screenshotCount++;', file=fileobj)
        print('                $("#screenshotCount").html(screenshotCount);', file=fileobj)
        print('            });', file=fileobj)
        print('        });', file=fileobj)
        print('    </script>', file=fileobj)

        print('</head>', file=fileobj)
        print('', file=fileobj)
        print('<body>', file=fileobj)
        print('<h1>Object picking example</h1>', file=fileobj)
        print('<p>', file=fileobj)
        print('Click on any shape to get the id and the coordinates of the hitting point.', file=fileobj)
        print('</p>', file=fileobj)
        print('<X3D  id="boxes" showStat="false" showLog="true" logLevel="Full" x="0px" y="0px" width="500px" height="500px">', file=fileobj)
        print('    <Scene>', file=fileobj)
        print('        <Viewpoint position="-2.25680 3.36560 14.62828" orientation="-0.60104 -0.28053 0.74837 0.40903"></Viewpoint>', file=fileobj)
        print('        <Group onclick="handleGroupClick(event)">', file=fileobj)
        for atom in self._atoms:
            for indent, line in self.atom_lines(atom):
                print(line, file=fileobj)
        print('        </Group>', file=fileobj)
        print('', file=fileobj)
        print('        <Transform id="marker" scale=".15 .15 .15" translation="100 0 0">', file=fileobj)
        print('            <Shape>', file=fileobj)
        print('                <Appearance>', file=fileobj)
        print('                    <Material diffuseColor="#FFD966"></Material>', file=fileobj)
        print('                </Appearance>', file=fileobj)
        print('                <Sphere></Sphere>', file=fileobj)
        print('            </Shape>', file=fileobj)
        print('        </Transform>', file=fileobj)
        print('    </Scene>', file=fileobj)
        print('</X3D>', file=fileobj)
        print('', file=fileobj)
        print('<div style="position:absolute;left:600px;top:70px;width:200px">', file=fileobj)
        print('    <h3>Last clicked object:</h3> ', file=fileobj)
        print('    <span id="lastClickedObject">-</span>', file=fileobj)
        print('    ', file=fileobj)
        print('    <br><br>', file=fileobj)
        print('    ', file=fileobj)
        print('    <h3>Click coordinates:</h3>', file=fileobj)
        print('    <table style="font-size:1em;">', file=fileobj)
        print('        <tr><td>X: </td><td id="coordX">-</td></tr>', file=fileobj)
        print('        <tr><td>Y: </td><td id="coordY">-</td></tr>', file=fileobj)
        print('        <tr><td>Z: </td><td id="coordZ">-</td></tr>', file=fileobj)
        print('    </table>', file=fileobj)
        print('</div>', file=fileobj)

        print('<div style="position:absolute;left: 550px;border:1px solid #dddddd; width:300px;min-height:200px;padding:10px;">', file=fileobj)
        print('    <b>Screenshots: <span id="screenshotCount">0</span></b>', file=fileobj)
        print('    <div id="screenshotPreviews">', file=fileobj)
        print('    </div>', file=fileobj)
        print('</div>', file=fileobj)
        print('<div>', file=fileobj)
        print('    <a href="#" id="btnTakeScreenshot">Take screenshot</a>', file=fileobj)
        print('</div>', file=fileobj)
        print('<table id="demo_table" class="gallery">', file=fileobj)
        print('  <tr>', file=fileobj)
        print('  </tr>', file=fileobj)
        print('</table>', file=fileobj)

        print('<div style="height:420px">', file=fileobj)
        print('    <x3d id="canvas" width="500px" height="400px">', file=fileobj)
        print('        <scene id="mainScene">', file=fileobj)
        print('            <Inline id="inlineBox" nameSpaceName="dcm"/>', file=fileobj)
        print('        </scene>', file=fileobj)
        print('    </x3d>', file=fileobj)
        print('</div>', file=fileobj)

        print('</body>', file=fileobj)
        print('</html>', file=fileobj)

    def atom_lines(self,atom):
        """Generates a segment of X3D lines representing an atom."""
        x, y, z = atom.position
        lines = [(0, '<Transform id="transform_'+str(atom.index)+'" translation="%.2f %.2f %.2f">' % (x, y, z))]
        lines += [(1, '<Shape DEF="'+str(atom.index)+'">')]
        lines += [(2, '<Appearance DEF="'+str(atom.index)+'">')]
        color = 'diffuseColor="%.3f %.3f %.3f"' % tuple(jmol_colors[atom.number])
        colour_original = 'originalColor="%.3f %.3f %.3f"' % tuple(jmol_colors[atom.number])
        lines += [(3, '<Material id="'+str(atom.index)+'" highlighted=0 '+color+' '+colour_original+' position="%.2f %.2f %.2f"></Material>' % (x, y, z))]
        #lines += [(3, '<Material id="color" %s specularColor="0.5 0.5 0.5">' % color)]

        lines += [(2, '</Appearance>')]
        lines += [(2, '<Sphere DEF="'+str(atom.index)+'" radius="%.2f"> </Sphere>' % covalent_radii[atom.number])] # onclick="changeColor();"
        lines += [(1, '</Shape>')]
        lines += [(0, '</Transform>')]
        return lines
