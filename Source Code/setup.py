from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

DATA=[('imageformats',['C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qjpeg4.dll',
    'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qgif4.dll',
    'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qico4.dll',
    'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qmng4.dll',
    'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qsvg4.dll',
    'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qtiff4.dll'
    ]),{'Template.docx','C:\\Users\\julia\\PycharmProjects\\440Wproject\\Template.docx'},
      {'checkwords.txt','C:\\Users\\julia\\PycharmProjects\\440Wproject\\checkwords.txt'}]

setup(
    options = {'py2exe': {"includes":["sip",'lxml.etree', 'lxml._elementpath', 'gzip', 'docx']}},
    windows = [{'script': "main.py"}],
    zipfile = None,
)