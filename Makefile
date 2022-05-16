all: joel.conf joel.txt pattihartley.conf pattihartley.txt sfreeling.conf sfreeling.txt tedbhardy.conf tedbhardy.txt tonymhardy.conf tonymhardy.txt gordonchin.conf gordonchin.txt marilynbreeze.conf marilynbreeze.txt sayc.conf sayc.txt melinda.conf melinda.txt billshardy.conf billshardy.txt cmc.conf cmc.txt carlyng.conf carlyng.txt

billshardy.txt: prealert.txt stanscripts.hdr billshardy.hdr shortcuts.txt 1NTOpening-11-14.txt 2NTOpening.txt 1MHardyRaises.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt billshardy.extras
	./conf2txt.py billshardy.conf

carlyng.txt: prealertnorth.txt stanscripts.hdr carlyng.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MRevBergenRaises.txt Kokish3WayGT.txt 1minorOpenings.txt 2COpening.txt 2DHSOpenings.txt defensemisc.txt 1NTdef-dont-cap.txt carlyng.extras
	./conf2txt.py carlyng.conf

cmc.txt: cmc.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MOpenings.txt Kokish3WayGT.txt 1minorOpenings.txt 2COpening.txt 2DHSOpenings.txt defensemisc.txt 1NTdef-dont-cap.txt cmc.extras
	./conf2txt.py cmc.conf

gordonchin.txt: prealert.txt stanscripts.hdr gordonchin.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MRevBergenRaises.txt Kokish3WayGT.txt 1minorOpenings.txt 2COpening.txt 2DHSOpenings.txt defensemisc.txt 1NTdef-meckwell-cap.txt gordonchin.extras
	./conf2txt.py gordonchin.conf

joel.txt: stdhdr.txt joel.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MRevBergenRaises.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt joel.extras
	./conf2txt.py joel.conf

marilynbreeze.txt: prealert.txt stanscripts.hdr marilynbreeze.hdr shortcuts.txt 1NTOpening-11-14.txt 2NTOpening.txt 1MOpenings.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-dont-cap.txt marilynbreeze.extras
	./conf2txt.py marilynbreeze.conf

melinda.txt: stdhdr.txt melinda.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MOpenings.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt XYZ.txt defensemisc.txt 1NTdef-modcap.txt melinda.extras
	./conf2txt.py melinda.conf

pattihartley.txt: prealert.txt stanscripts.hdr pattihartley.hdr shortcuts.txt 2NTOpening.txt 1MOpenings.txt 1MDruryResponses.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt 1CToucan.txt pattihartley.extras
	./conf2txt.py pattihartley.conf

sayc.txt: stanscripts.hdr sayc.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MOpenings.txt Kokish3WayGT.txt 1minorOpenings.txt 2COpening.txt 2DHSOpenings.txt defensemisc.txt 1NTdef-dont-cap.txt sayc.extras
	./conf2txt.py sayc.conf

sfreeling.txt: stdhdr.txt sfreeling.hdr shortcuts.txt 1NTOpening-15-17.txt 2NTOpening.txt 1MRevBergenRaises.txt Kokish3WayGT.txt 1minorOpenings.txt 2COpening.txt 2DHSOpenings.txt defensemisc.txt 1NTdef-dont-modcap.txt sfreeling.extras
	./conf2txt.py sfreeling.conf

tedbhardy.txt: prealert.txt stanscripts.hdr tedbhardy.hdr shortcuts.txt 2NTOpening.txt 1MHardyRaises.txt 1MDruryResponses.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt 1CToucan.txt tedbhardy.extras
	./conf2txt.py tedbhardy.conf

tonymhardy.txt: stdhdr.txt tonymhardy.hdr shortcuts.txt 1NTOpening-11-14.txt 2NTOpening.txt 1MHardyRaises.txt 1minorOpenings.txt 1mSpiral.txt 2COpening.txt 2DHSOpenings.txt 2DFlannery.txt XYZ.txt defensemisc.txt 1NTdef-suction.txt 1CDef-Suction.txt 2CDef-Suction.txt tonymhardy.extras
	./conf2txt.py tonymhardy.conf

