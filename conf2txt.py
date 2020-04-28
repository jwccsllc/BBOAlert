#!/csrel27b/bin/python

# $Header: /vol/cscvs/python-Csys/csmain.py,v 1.3 2007/10/06 00:45:43 csoftmgr Exp $
# $Date: 2007/10/06 00:45:43 $

import Csys, os, os.path, sys, re

__doc__ = '''Write text file from objects in config file

usage: %s fname''' % Csys.Config.progname

__doc__ += '''

$Id: csmain.py,v 1.3 2007/10/06 00:45:43 csoftmgr Exp $
'''

__version__='$Revision: 1.3 $'[11:-2]

def writeFile(cfg): #{
	fname	= cfg.get('bboalert', 'outfile')
	modules	= cfg.getList('bboalert', 'modules')
	fh = Csys.openOut(fname)
	for module in modules: #{
		fh.write('\n# %s\n' % module)
		data = open(module).read()
		fh.write(data)
	#}
	fh.close()
#} writeFile

def main(): #{
	# Add program options to parser here

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

	fname = args[0]
	cfg = Csys.ConfigParser(args)
	writeFile(cfg)
#}
if __name__ == '__main__': #{
	main()
#}
