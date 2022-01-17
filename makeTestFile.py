#!/csrel27b/bin/python

# $Header: /vol/cscvs/python-Csys/csmain.py,v 1.4 2009/11/25 07:49:41 csoftmgr Exp $
# $Date: 2009/11/25 07:49:41 $

from __future__ import print_function
import os, os.path, sys, re
import csspath
import Csys

__doc__ = '''Make test file for BBOalert

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
	toptext = open('alertTester.txt', 'rb').read()
	body = open(args[0]).read()
	reOpts = re.MULTILINE|re.DOTALL|re.IGNORECASE
	commentPattern = re.compile(r'^#.*?$', reOpts)
	bboAlertPattern = re.compile(r'^\s*BBOalert.*?\n', reOpts)
	body = commentPattern.sub('', body)
	cmdPattern = re.compile(r'^', reOpts)
	body = bboAlertPattern.sub('', body)
	body = re.sub(r'^\s*?\n', '', body, flags=reOpts)
	body = cmdPattern.sub('T', body)
	body = re.sub(r'^T\s*\n', '', body, flags=reOpts).rstrip('T')
	print((	'BBOalert\n%s\nScript,onDataLoad\n'
			'let tests = `\n%s`\n\n'
			'ALERTTESTER.runTests(tests);\n'
			'Script'
		) % (toptext, body))

#}
if __name__ == '__main__': #{
	main()
#}
# vim: noexpandtab sw=4 ts=4 wm=0
