import sys
import os
import gc

base_dir = os.path.split(os.path.abspath(__file__))[0]
code_dir = os.path.join(base_dir, 'code')
fig_dir = os.path.join(base_dir, 'figs')

# For relative imports, we need this
sys.path.append(code_dir)

#------------------------------------------------------------
# Check directories
if not os.path.exists(code_dir):
    raise ValueError('code dir does not exist')

if not os.path.exists(fig_dir):
    os.makedirs(fig_dir)

#------------------------------------------------------------
# Prepare plotting scripts
import matplotlib
matplotlib.use('Agg') #don't display plots
import matplotlib.pyplot as plt

#------------------------------------------------------------
# plot all scripts in the code directory
os.chdir(code_dir)
plot_scripts = [f for f in os.listdir(code_dir)
                if f.startswith('fig') and f.endswith('.py')]

for script in plot_scripts:
    fig_fmt = os.path.join(fig_dir,
                           os.path.splitext(script)[0] + '.pdf')

    if os.path.exists(fig_fmt):
        output_modtime = os.stat(fig_fmt).st_mtime
        source_modtime = os.stat(script).st_mtime

        if output_modtime >= source_modtime:
            print "skipping script %s: no modifications" % script
            continue

    print "running script %s" % script
    print "  saving to %s" % fig_dir
    
    plt.close('all')
    execfile(os.path.basename(script), {'pl' : plt,
                                        'plt' : plt,
                                        'pylab' : plt})
    
    fig_mgr_list = matplotlib._pylab_helpers.Gcf.get_all_fig_managers()
    figlist = [manager.canvas.figure for manager in fig_mgr_list]
    figlist = sorted(figlist, key = lambda fig: fig.number)

    if len(figlist) == 0:
        raise ValueError("no figure created")
    elif len(figlist) > 1:
        raise ValueError("multiple figures")
    else:
        figlist[0].savefig(fig_fmt, bbox_inches='tight')

    plt.close('all')
    gc.collect()
