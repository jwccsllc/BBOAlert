#!/csrel27c/bin/python3.9

# $Header: /vol/cscvs/python-Csys/csmain.py,v 1.4 2009/11/25 07:49:41 csoftmgr Exp $
# $Date: 2009/11/25 07:49:41 $

import csspath
import os, os.path, sys, re
import Csys

__doc__ = '''Create Makefile from *.conf files

usage: %s''' % Csys.Config.progname

__doc__ += '''

$Id: csmain.py,v 1.4 2009/11/25 07:49:41 csoftmgr Exp $
'''

__version__='$Revision: 1.4 $'[11:-2]

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
	configs = {}
	from glob import glob
	configFiles = glob('*.conf')
	all = []
	for config in configFiles: #{
		cfg = Csys.ConfigParser(config)
		configs[config] = cfg
		all.extend([config, cfg.get('bboalert', 'outfile')])
	#}
	print('all: %s\n' % ' '.join(all))
	for config in sorted(configs.keys()): #{
		cfg = configs[config]
		outfile = cfg.get('bboalert', 'outfile')
		modules	= ' '.join(cfg.getList('bboalert', 'modules'))
		print('%s: %s' % (outfile, modules))
		print('\t./conf2txt.py %s\n' % config)
	#}
#}
if __name__ == '__main__': #{
	main()
#}
# vim: noexpandtab sw=4 ts=4 wm=0
