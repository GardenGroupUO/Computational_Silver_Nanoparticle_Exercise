import os

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from IPython.display import HTML

from viewer.x3d_HTML_writer import write_x3d_html

def view_x3d(atoms):
    """View atoms inline in a jupyter notbook. This command
    should only be used within a jupyter/ipython notebook.
    
    Args:
        atoms - ase.Atoms, atoms to be rendered"""
    
    output = StringIO()
    write_x3d_html(atoms, output)
    data = output.getvalue()
    with open(os.path.realpath(__file__).replace('/x3d_viewer.py','')+'/'+'html_file.html','w') as write_to:
        write_to.write(data) 
    output.close()
    return HTML(data)