import re,argparse
import os
import sys
import matplotlib.pyplot as plt
import plistlib
import numpy as np

def findCommonTrack(fileNames):
    """ Find common track in given playlist file,
    and save them to common.txt"""
    # a list of sét of track names
    trackNameSets=[]
    for fileName in fileNames:
        trackNames=set()
        # read in playlist
        plist=plistlib.readPlist(fileName)
        # get the tracks
        tracks=plist['Tracks']
        # iterate through the track
        for trackId,track in tracks.items():
            try:
                # add the track name to a set
                 trackNames.add(track['Name'])
            except:
                # ignore
                   pass
        # add to list
        trackNameSets.append(trackNames)
    # get common tracks
    commonTracks=set.intersection(*trackNameSets)
    # write to file

    if len(commonTracks)>0:
        f=open("common.txt",'wb')
        for val in commonTracks:
            s="%s\n" %  val
            f.write(s.encode("UTF-8"))
        f.close()
        print("% common tracks found."
              "Track name written to common.txt" % len(commonTracks))
    else:
        print("No common tracks!")

def plotStart(fileName):

    """
    Plot some statistic by readin track information from playlist.

    """

    # read in playlist
    plist=plistlib.readPlist(fileName)
    # get the tracks
    tracks=plist['Tracks']
    #create lists of rating and duration
    ratings=[]
    durations=[]

    #iterate through tracks

    for trackId,track in tracks.items():
        try:
            ratings.append((track['Album Rating']))
            durations.append((track['Total Time']))
        except:
            # ignore
              pass
    # ensure valid data was collected
    if ratings==[] or durations==[]:
        print("No valid Album Rating/Total time data in %s." % fileName)
        return
    # cross plot

    x=np.array(durations,np.int32)
    # convert to minutes

    x=x/60000.0
    y=np.array(ratings,np.int32)
    plt.subplot(2,1,1)
    plt.plot(x,y,'*')
    plt.axis([0,1.05*np.max(x),-1,110])
    plt.xlabel('Track duration')
    plt.ylabel('Track rating')

    #plot historgram

    plt.subplot(2,1,2)
    plt.hist(x,bins=20)
    plt.xlabel('Track Duration')
    plt.ylabel('Count')

    #show plot
    plt.show()
def findDup(fileName):
    """
    find duplicate tracks given play list
    :param fileName:
    :return:
    """

    print('Finding duplicate track in %s...'% fileName)
    # ready playlist
    plist=plistlib.readPlist(fileName)
    # get the tracks

    tracks=plist['Tracks']

    # creat a trackname dict

    trackNames={}

    for trackId, track in tracks.items():
        try:
            name=track['Name']
            duration=track['Total Time']
            if name in trackNames:
                # if name and duration matches, increment count
                # duration rounded to nearest second
                if duration//1000 == trackNames[name][1]//1000:
                    count=trackNames[name][1]
                    trackNames[name]=(duration,count+1)
            else:
                # add entry-duration and count
                 trackNames[name]=(duration,1)
        except:
            # ignore
             pass
    # store duplicates as (name,count) tuples

    dups=[]
    for k,v in trackNames.items():
        if v[1]>1:
            dups.append((v[1],k))
    # save dups to file

    if len(dups)>0:
        print("Found % d duplicates. Track names saved to dup.txt" %len(dups))
    else:
        print("No duplicate tracks found!")
    f=open("dups.txt",'w')
    for val in dups:
        f.write("[%d] %s\n" % (val[0],val[1]))
    f.close()

# Gather our code in a main() function

def main():
    # create parser
    desStr="""
    This program analyzes playlist file (.xml) exported from Itunes
    """
    parser=argparse.ArgumentParser(description=desStr)

    # add a mutually exclusive group of arguments

    group=parser.add_mutually_exclusive_group()

    # add expected arguments

    group.add_argument('--common', nargs="*", dest='plFiles', required=False)
    group.add_argument('--stats', dest='plFile', required=False)
    group.add_argument('--dup',dest='plFileD', required=False)

    # parse args

    args=parser.parse_args()

    if args.plFiles:
        # find common tracks
         findCommonTrack(args.plFiles)
    elif args.plFile:
        # plot stats
        plotStart(args.plFile)
    elif args.plFileD:
        # find dup track
        findDup(args.plFileD)
    else:
        print(" Không có track nào mà bạn tìm ở đây")
# main method

if __name__=='__main__':
    main()