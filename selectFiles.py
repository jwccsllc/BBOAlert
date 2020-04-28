#!/csrel27b/bin/python

# $Header: /vol/cscvs/python-Csys/csmain.py,v 1.4 2009/11/25 07:49:41 csoftmgr Exp $
# $Date: 2009/11/25 07:49:41 $

import os, os.path, sys, re
try: import Csys #{
except: #{
	sys.path.extend([
		os.path.join(sys.prefix, 'lib/python'),
		os.path.join(sys.prefix, 'lib/python/site-packages'),
	])
	import Csys
#}}
# from Tkinter import *
# import Tkinter, Tkconstants, tkFileDialog
from Csys.Curses import *
from curses import panel
from glob import glob
import traceback
try: #{{
	from io import BytesIO
#}
except ImportError: #{
	from cStringIO import StringIO as BytesIO
#}}

__doc__ = '''File Selection

usage: %s outFile [dir]''' % Csys.Config.progname

__doc__ += '''

$Id: csmain.py,v 1.4 2009/11/25 07:49:41 csoftmgr Exp $
'''

__version__='$Revision: 1.4 $'[11:-2]

menuDict = {}

class GlobalVars(object): #{
	def __init__(self): #{
		self.colMenuLines	= {} # table of menuLines for each column
		self.colMenus		= {} # The ScrollMenu for each column
		self.win			= curses.newwin(
			term_lines_avail, term_co, term_firsty, 0)
		self.panel			= panel.new_panel(self.win)
		self.colWindows		= {} # The win derived windows for each column
		self.newTables		= True
		self.max_y, self.max_x = self.win.getmaxyx()
		self.currentTitle	= ''
	#} __init__
#} class GlobalVars

class ModuleFile(object): #{
	def __init__(self, fname): #{
		self.prompt	= fname
		self.data	= fname
		self.keypressed	= ''
	#}

	def __str__(self): return(self.prompt)

	def __cmp__(self, othr): #{
		return(cmp(self.data, othr.data))
	#}
#} class ModuleFile

G = GlobalVars()

colPrompts = dict(
	active = (
		UserPrompt('s',	'[S]elect'),
		UserPrompt('q',	'[Q]uit'),
	),
	selected = (
		UserPrompt('d', '[D]elete'),
		UserPrompt('u',	'[U]p'),
		UserPrompt('d',	'[D]own'),
		UserPrompt('q',	'[Q]uit'),
		UserPrompt('w',	'[W]rite'),
	)
) # colPrompts

colNames = ('files', 'selected')
column_files, column_select = range(len(colNames))

def initTables(dir, selFile=None): #{
	unerrs('dir = %s selFile = %s' % (dir, selFile))
	global G
	if G is None: G = GlobalVars()
	colTables = {}
	for name in colNames: #{
		if not name in G.colMenuLines: #{
			G.colMenuLines[name] = []
		#}
		table = G.colMenuLines[name]
		table.clear()
		colTables[name] = []
	#}
	unerrs('colTables = %s' % repr(colTables))
	dsp_prmpt('Getting Files')

	gl = ('%s/*.txt' % dir)
	for file in sorted(glob(gl)): #{
		# unerrs('file %s' % file)
		colTables['files'].append(file)
	#}
	try: #{{
		unerrs('selFile = %s' % repr(selFile))
		unerrs('len colTables["files"] = %d' % len(colTables['files']))
	#}
	except: #{
		buf = BytesIO()
		exc_type, exc_value, exc_traceback = sys.exc_info()
		traceback.print_tb(exc_traceback, limit=1, file=buf)
		buf.seek(0)
		for l in buf: #{
			unerrs('print_tb: %s' % l)
		#}
	#}}
	if selFile: #{
		fh = open(selFile)
		for line in fh: #{
			colTables['selected'].append(line.rstrip())
		#}
	#}
	# put them in the appropriate MenuLines
	for name in colNames: #{
		unerrs('colNames[%s]' % name)
		unerrs('MenuLines[%s]' % name)
		menuLines = []
		unerrs('type menuLines = %s' % type(menuLines))
		for i, file in enumerate(colTables[name]): #{
			dsp = os.path.basename(file)
			menuLines.append(ModuleFile(file))
		#}
		G.colMenuLines[name] = menuLines
	#}
	dsp_prmpt('')
	
	# now create the MenuScroll objects
	for name in colNames: #{
		unerrs('reload %s' % name)
		G.colMenus[name].reload()
	#}
	unerrs('colMenus reloaded')
#} def initTables

def selectFiles(): #{
	global G, dir, selFile
	if G is None: G = GlobalVars()
	G.currentTitle = 'Select Files For Inclusion'
	windows_title_set(
		G.currentTitle,
		right=Csys.Config.hostname_short,
		refresh=True
	)
	colwin = G.win
	colwin_panel = G.panel
	colwin_panel.top()
	maxy_, max_x = re.win.getmaxyx()
	offset = 0
	colwidth = int(max_x / len(colNames))
	for name in colNames: #{
		win = G.colWindows[name] = colwin.derwin(max_y, colwidth, 0, offset)
		offset += colwidth
		menuLines = G.colMenuLines[name] = []
		G.colMenus[name] = MenuScroll('',
			menuLines,
			hdrLine = name,
			border = True,
			win = win,
			vcenter = False,
			userPrompts = colPrompts[name]
		)
	#}
	colwin_panel.top()
	colwin_panel.show()
	colwin.refresh()
	panel.update_panels()
	for name in colNames: #{
		subwin = G.colMenus[name].win
		subwin.noutrefresh()
	#}
	# create tuple of menus.
	menus = tuple([G.colMenus[name] for name in colNames])
	n = len(menus) - 1
	column = 0
	column_motion = 0
#} def selectFiles

class MyGlobals(object): pass

ConfigParser = Csys.ConfigParser

cfg = None

def buildMainMenu(): #{
	global menuDict
	menuList = [
		menuDict['config'],
		menuDict['select'],
		menuDict['write'],
	]
	key = 'main'
	menuDict[key] = Menu(
		'Select Files [%s]' % Csys.Config.hostname_short,
		menuList,
		menuname = key
	)
#} buildMainMenu

configScreen = ('''
      Players: [players                                                    ]
      Outfile: [outfile                                                    ]
 Press F4 or PgDown to save and quit

%metadata
[DEFAULT]
type: char
rname: selectFiles
	''') # strips extra newline at the top

def getConfig(): #{
	global configScreen

	# unerrs('cfg = %s' % cfg)
	cols = cfg.getDict('bboalert')
	# unerrs('ckeys = %s' % repr(cols.keys()))
	fh = BytesIO(configScreen)
	screen = configScreen = Csys.Curses.Screen(
		# cfg = cfg,
		fname = fh,
		hcenter=True, vcenter=False, border=False
	)
	windows_title_set('Player Configuration')
	# unerrs('cols = %s' % repr(cols.keys()))
	for field in screen.fields: #{
		fdesc = field.fdesc
		if fdesc: #{
			# unerrs('fdesc %s' % repr(fdesc))
			lname = fdesc.lname
			# unerrs('lname %s data %s' % (lname, cols.get(lname)))
			data = cols.get(fdesc.lname, '')
			# unerrs('lname = %s len data = %d' % (lname, len(data)))
			# unerrs('displen = %d' % field.displen)
			n = min(len(data), field.displen)
			field.setOrigData(data[:n])
		#}
	#}
	cfg.screen = screen
	# screen = configScreen
	screen.panel.show()
	screen.panel.top()
	while True: #{
		screen.getData()
		if screen.save_requested: #{
			for field in screen.fields: #{
				if field.fdesc: #{
					lname	= field.fdesc.lname
					data	= field.data
					cfg.set('bboalert', lname, data)
				#}
			#}
			cfg.rewrite()
			MyGlobals.Config = cfg.getClass('bboalert')
			MyGlobals.Config.modules = cfg.getList('bboalert', 'modules')
		#}
		break
	#}
	# unerrs('cfg.firstmodule = %s' % repr(MyGlobals.Config))
	screen.panel.hide()
#} getConfig

def getFiles(): #{
	pass
#}

def writeFile(): #{
	fname = MyGlobals.Config.outfile
	# unerrs('fname = %s' % fname)
	fh = Csys.openOut(fname)
	for module in MyGlobals.Config.modules: #{
		data = open(module).read()
		fh.write(data)
	#}
	fh.close()
#} writeFiles

def main(stdscr=None): #{
	global menuDict, cfg
	
	
	def setOptions(): #{
		'''Set command line options'''
		global __doc__

		parser = Csys.getopts(__doc__)

	#	parser.add_option('-d', '--directory',
	#		action='store', type='string', dest='directory', default=None,
	#		help='Change to directory before starting process',
	#	)
	#	parser.add_option('-r', '--restart',
	#		action='store_true', dest='restart', default=False,
	#		help='restart without raising mailbox flags intially',
	#	)
		return parser
	#} setOptions

	parser = setOptions()

	(options, args) = parser.parse_args()

	verbose = ''
	if options.verbose: #{
		verbose = '-v'
		sys.stdout = sys.stderr
	#}
	Csys.getoptionsEnvironment(options)

	MyGlobals.cfg = cfg = ConfigParser(args[0])
	menuDict.update(dict( 
		config	= MenuLine('Get Configuration', seq=0, action=getConfig),
		select	= MenuLine('Get Files', action=getFiles),
		write	= MenuLine('Write File', action=writeFile),
	))

	windows_header_set('Select Files', Csys.Config.progname)
	windows_title_set('Select Files for Inclusion')
	windows_refresh(redraw=True)

	newMenu = None
	unerrs('start')
	buildMainMenu()

	while True: #{
		menu = newMenu or menuDict['main']
		newMenu = None
		rc = menu.getSelection()
		newMenu = menuDict.get(rc)
		if newMenu: continue
		if isinstance(rc, Menu): #{
			newMenu = rc
			continue
		#}
		if isinstance(rc, MenuLine): #{
			if rc.action: #{
				rc.action()
				continue
			#}
		#}
		if rc[0] in ('q', 'Q'): #{
			break
		#}
	#} main loop
	cursesExit()
#}
if __name__ == '__main__': #{
	wrapper(main)
#}
# vim: noexpandtab sw=4 ts=4 wm=0
