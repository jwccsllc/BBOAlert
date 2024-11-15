all: cmc.conf cmc.txt marilynbreeze.conf marilynbreeze.txt pattihartley.conf pattihartley.txt billshardy.conf billshardy.txt melinda.conf melinda.txt tedbhardy.conf tedbhardy.txt tonymhardy.conf tonymhardy.txt brianpotter.conf brianpotter.txt rosemayv.conf rosemayv.txt joel.conf joel.txt carlyng.conf carlyng.txt sfreeling.conf sfreeling.txt sayc.conf sayc.txt gordonchin.conf gordonchin.txt

billshardy.txt: stanscripts.hdr billshardy.hdr shortcuts.txt 1NTOpening-11-14.txt 2NTOpening.txt 1MHardyRaises.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt billshardy.extras
	./conf2txt.py billshardy.conf

brianpotter.txt: stanscripts.hdr brianpotter.hdr shortcuts.txt 2NTOpening.txt 1MHardyRaises.txt 1MDruryResponses.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt 1CToucan.txt brianpotter.extras
	./conf2txt.py brianpotter.conf

carlyng.txt: stanscripts.hdr carlyng.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MRevBergenRaises.txt Kokish3WayGT.txt 1MDruryResponses.txt 1minorOpenings.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt carlyng.extras
	./conf2txt.py carlyng.conf

cmc.txt: stanscripts.hdr cmc.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MOpenings.txt Kokish3WayGT.txt 1minorOpenings.txt 2COpening.txt 2DHSOpenings.txt defensemisc.txt 1NTdef-dont-cap.txt cmc.extras
	./conf2txt.py cmc.conf

gordonchin.txt: prealert.txt stanscripts.hdr gordonchin.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MRevBergenRaises.txt Kokish3WayGT.txt 1minorOpenings.txt 2COpening.txt 2DHSOpenings.txt defensemisc.txt 1NTdef-meckwell-cap.txt gordonchin.extras
	./conf2txt.py gordonchin.conf

joel.txt: stdhdr.txt stanscripts.hdr joel.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MRevBergenRaises.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt joel.extras
	./conf2txt.py joel.conf

marilynbreeze.txt: prealert.txt stanscripts.hdr marilynbreeze.hdr shortcuts.txt 1NTOpening-11-14.txt 2NTOpening.txt 1MOpenings.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-dont-cap.txt marilynbreeze.extras
	./conf2txt.py marilynbreeze.conf

melinda.txt: stdhdr.txt stanscripts.hdr melinda.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MOpenings.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt XYZ.txt defensemisc.txt 1NTdef-modcap.txt melinda.extras
	./conf2txt.py melinda.conf

pattihartley.txt: prealert.txt stanscripts.hdr pattihartley.hdr shortcuts.txt 1NT15-17-Basic.txt 1NT-RangeAsk.txt 1NT-FSSA.txt 2NTOpening.txt 1MOpeningsNoDrury.txt 1MJacobyMulti.txt 1MDruryResponses.txt 2COpening.txt 2DFlannery.txt 2HSOpenings.txt XYZ.txt defensemisc.txt 1NTdef-mosley.txt 1CToucan-No-NT.txt pattihartley.extras
	./conf2txt.py pattihartley.conf

rosemayv.txt: prealert.txt stanscripts.hdr rosemayv.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MOpenings.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt defensemisc.txt 1NTdef-dont-cap.txt rosemayv.extras
	./conf2txt.py rosemayv.conf

sayc.txt: stanscripts.hdr sayc.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MOpenings.txt Kokish3WayGT.txt 1minorOpenings.txt 2COpening.txt 2DHSOpenings.txt defensemisc.txt 1NTdef-dont-cap.txt sayc.extras
	./conf2txt.py sayc.conf

sfreeling.txt: stdhdr.txt stanscripts.hdr sfreeling.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MRevBergenRaises.txt Kokish3WayGT.txt 1minorOpenings.txt 2COpening.txt 2DHSOpenings.txt defensemisc.txt 1NTdef-dont-modcap.txt sfreeling.extras
	./conf2txt.py sfreeling.conf

tedbhardy.txt: stanscripts.hdr tedbhardy.hdr shortcuts.txt 2NTOpening.txt 1MHardyRaises.txt 1MDruryResponses.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt 1CToucan.txt tedbhardy.extras
	./conf2txt.py tedbhardy.conf

tonymhardy.txt: stdhdr.txt stanscripts.hdr tonymhardy.hdr shortcuts.txt 1NTOpening-11-14.txt 2NTOpening.txt 1MHardyRaises.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt tonymhardy.extras
	./conf2txt.py tonymhardy.conf

