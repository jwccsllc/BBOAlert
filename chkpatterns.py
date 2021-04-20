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
import six
if six.PY3:
	from io import open

__doc__ = '''Celestial Software Main program prototype

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

	skipPattern = re.compile(r'(^#|BBOalert|Option)', re.IGNORECASE)


	verbose = ''
	if options.verbose: #{
		verbose = '-v'
		sys.stdout = sys.stderr
	#}
	Csys.getoptionsEnvironment(options)

	contexts = {}

	if not args: args.append('tedbhardy.txt')

	with open(args[0], 'rb') as fh: #{
		n = 0
		for line in fh: #{
			n += 1
			line = line.rstrip()
			if skipPattern.search(line): #{{
				if not line[0] == '#':
					print(n, line)
			#}
			else: #{
				try: #{{
					context, bid, alert = line.split(',', 3)
					# print(n, context, bid, alert)
					key = (context, bid)
					if key in contexts: #{
						print('duplicate line %d %s\n\t%s' %
							(n, key, contexts[key]))
					#}
					contexts[key] = (n, line)
				#}
				except Exception as e: #{
					pass
				#}}
			#}}
		#}
	#}
#}
if __name__ == '__main__': #{
	main()
#}
# vim: noexpandtab sw=4 ts=4 wm=0
