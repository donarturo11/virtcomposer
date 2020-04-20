#!/usr/bin/env python2
####                       ##################
####    Virtual composer   ##################
####                       ##################
### donarturo <arturwrona91 (at) gmail (dot) com>
import os, random, sys, numpy 

print """
####                       ##################
####    Virtual composer   ##################
####                       ##################
"""
print """
\t Dear User!\n
Welcome in simple and primitive program
to compose various composition
without of user's intervention
\n
You must only give some numbers to range of randomization\n
"""

## Choose lucky numbers
limit = input("Type lucky number of end: ")
range = input("Input maximum number to random: ")
## Note parameters
volmin = input("MinVolume (>0dB): ")
volmax = input("MaxVolume: ")
freqmin = input("MinFreq (in hZ): ")
freqmax = input("MaxFreq (in hZ): ")
freqres = input("Freq Resolution: ")
timemin = input("MinTime (in s): ")
timemax = input("MaxTime: ")
restmin = input("MinRest: ")
restmax = input("MaxRest: ")
filename = raw_input("Input filename: ")
randlim = random.randint(0,int(range))
fileno = 0
print "Duration\tfreq\twave"
#os.system("rm seq*.wav")

while limit != randlim:
    ### Note parameters
    duration = random.uniform(timemin,timemax)
    freq = random.randrange(freqmin,freqmax,freqres)
    volume = random.randint(volmin,volmax)
    rest = random.uniform(restmin,restmax)
    ### Waveform
    waveform = ['sine','square','triangle','saw']
    wave = random.randint(0,3)
    selwave = waveform[int(wave)] 
    ### Choose between note or rest ###
    note = random.randint(0,1)
    cmdrest="sox -n -b16 -r 44100 -c1 seq%s.wav trim 0 %s"%(fileno,rest)
    cmd="sox -n -b16 -r 44100 -c1 seq%s.wav synth %s %s %s vol %sdb"%(fileno,duration,selwave,freq,volume)
    #################################
    if note == 0:
        os.system(cmd)
        print cmd
    elif note == 1:
        os.system(cmdrest)
        print cmdrest
    fileno += 1
   ### If number of file reaches randomised number, 
   ### creating composition will finish.
    if fileno == randlim:        
        break
 
## Join generated files into one 
cmd_out="sox seq*.wav -r 44100 -c1 %s.wav"%(filename)
os.system(cmd_out)
## Remove temporary files
os.system("rm seq*.wav")
print "THE END"
print "Thank you for use this program"
print "This program is under GPL licence"
print "You have no restrictions in using,\nmodification, or distribution this program"
print "donarturo <arturwrona91(at)gmail(dot)com>" 
