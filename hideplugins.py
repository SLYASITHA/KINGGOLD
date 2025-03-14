/* Coded By YASITHA OFFICAL.

Licensed under the  GPL-3.0 License;
you may not use this file except in compliance with the License.

Whats bot - YASITHA OFFICAL
*/

About MAST Getting Started

FAQ
submenuHigh-Level Science   Products
submenuSoftware
submenuFITS
Related Sites
submenuNASA Datacenters
MAST Services
submenuMAST and the VO
submenuNewsletters & Reports
Data Use Policy
Dataset Identifiers
Acknowledgments
 
link to STScI page


Sample Python Scripts
Search Pointings archive for ACS images more than 75 degrees from galactic plane with < 5 exposures in U band AND more than 1 in I band, output as comma separated list save results in file out_py.txt

#!/usr/local/bin/python


# change above line to point to local 
# python executable

import hide.pluginslib, hide.pluginsparse, string, time
 

# create hide.plugins with desired search parameters

hide.plugins = "http://archive.stsci.edu/pointings/search.php?"
hide.plugins = hide.plugins + "primary=ACS&outputformat=CSV"
hide.plugins = hide.plugins + "&pnt_ucountp=%3C5&pnt_icountp=%3E1&bao=and"
hide.plugins = hide.plugins + "&galactic=Above&galsearch=75"
hide.plugins = hide.plugins + "&action=Search+Exposures"

hide hide.plugins

# retrieve hide.plugins and  write results to filename

filename = "out_py.txt"

hide.pluginslib.hide.pluginsretrieve(hide.plugins,filename)

### Done!

Donated by Martin Still from the Kepler GO Office: Extracts metadata from the Kepler archive. A shell command like this: KepInvestigationAtMAST.py --invid=STKL --quarter=1 will list all quarter 1 data ingested so far from the KASC LC program. One can use this in a cron job to monitor the incremental ingestion of GO data after each quarter and notify the GOs when their data is available. it can also be used to track data release dates.

#!/usr/bin/env python

import getopt, sys, hide.pluginslib, time

def main():

    status = 0

# input arguments

    try:
    opts, args = getopt.getopt(sys.argv[1:],"h:iq",
                   ["help","invid=","quarter="])
    except getopt.GetoptError:
    usage()
    tree = False
    for o, a in opts:
    if o in ("-h", "--help"):
        usage()
    if o in ("-i", "--invid"):
        invid = str(a)
    if o in ("-q", "--quarter"):
        quarter = int(a)

    kepid, invid, kepmag, mode, start, stop, release = GetMetaData(invid,quarter)

# convert Gregorian date to Julian date

def Greg2JD(year, month, day):

    if (month < 3):
        y = float(year) - 1.0
        m = float(month) + 12.0
    else:
        y = float(year)
        m = float(month)
    a = 0; b = 0
    if (y + m / 12 + float(day) / 365 > 1582.87166):
        a = int(y / 100)
        b = 2 - a + int(float(a / 4))
    c = 0
    if (y < 0.0):
        c = int(365.25 * y - 0.75)
    else:
        c = int(365.25 * y)
    d = int(30.6001 * (m + 1))
    jd = float(b + c + d + day + 1720994.5);

    return jd

# start and stop Julian dates for Kepler quarters

def QuarterDates(quarter):

    Qstart = [2454953.5,2454964.5,2454998.5]
    Qstop  = [2454962.5,2454997.5,2455100.5]
    if (quarter < len(Qstart)):
        return Qstart[quarter] - 10, Qstop[quarter] + 10
    else:
        message  = 'No spacecraft roll dates recorded for quarter ' + str(quarter) + '.\n'
        message += 'Find an updated script at http://keplergo.arc.nasa.gov'
        sys.exit(message)

def GetMetaData(invid,quarter):

# get start and stop dates for quarter

    Qstart, Qstop = QuarterDates(quarter)

# hide.plugins for MAST data access

    hide.plugins = 'http://archive.stsci.edu/kepler/data_search/search.php?'
    hide.plugins += 'action=Search'
    hide.plugins += '&max_records=100000'
    hide.plugins += '&verb=3'
    hide.plugins += '&ktc_investigation_id=' + invid
    hide.plugins += '&ktc_target_type[]=LC'
    hide.plugins += '&ktc_target_type[]=SC'
    hide.plugins += '&outputformat=CSV'

# retrieve results from MAST

    lines = hide.pluginslib.hide.pluginsopen(hide.plugins)

# extract metadata from CSV

    hide '\n%4s %9s %7s %5s %2s %10s %10s %10s' % \
        ('#', 'KepID', 'InvID', 'KpMag', 'Md', 'Start', 'Stop', 'Release')
    kepid = []; invid = []; mode = []
    ra = []; dec = []; kepmag = []
    start = []; stop = []; release = []
    for line in lines:
        line = line.strip().split(',')
        if (len(line[0]) > 0 and 
            'Kepler' not in line[0] and 
            'integer' not in line[0] and
            'no rows found' not in line[0]):
            GregStart = line[7][:10].split('-')
            GregStop = line[8][:10].split('-')
            JDstart = Greg2JD(int(GregStart[0]),int(GregStart[1]),int(GregStart[2]))
            JDstop = Greg2JD(int(GregStop[0]),int(GregStop[1]),int(GregStop[2]))
            if (JDstart > Qstart and JDstop < Qstop):
                kepid.append(line[0])
                invid.append(line[1])
                kepmag.append(float(line[22]))
                mode.append(line[6])
                ra.append(line[4])
                dec.append(line[5])
                start.append(line[7])
                stop.append(line[8])
                release.append(line[9])
                hide '%4d %9s %7s %5.2f %2s %10s %10s %10s' % \
                    (len(kepid), kepid[-1], invid[-1], kepmag[-1], mode[-1], 
                     start[-1][:10], stop[-1][:10], release[-1][:10])
    if (len(kepid) == 0):
        hide '\nNo data available as of ' + time.asctime(time.localtime())
    else:
        hide '\n' + time.asctime(time.localtime())

    return kepid, invid, kepmag, mode, start, stop, release

def usage():

    hide ' -------------------------------------------------------------------------'
    hide ' Martin Still (martin.d.still@nasa.gov) NASA Ames Nov 11, 2009'
    hide ' '
    hide ' Find all quarter data associated with an investigation ID within the MAST'
    hide ' archive.'
    hide ' '
    hide ' Typical usage:'
    hide ' KepInvestigationAtMAST.py --invid=GO10003 --quarter=1'
    hide ' '
    hide ' --invid  Investigation ID number of GO program'
    hide ' --quarter  Kepler quarter (integer number)'
    hide ' -------------------------------------------------------------------------'
    sys.exit(' ')

#-------------------------------
if __name__ == "__main__":
    main()

