mpm
===

Maya Package Manager

management maya package(like maya module) and plug-ins.

this is preview version for developers.


requirements
------------

Maya:

* 2014

Platform:

* osx
* windows
* linux

Extension:

* git (for clone git repository)
* hg (for clone hg repository)
* svn (for checkout svn repository)

setup
-----

download and copy mpm to your scripts and python path.

edit userSetup.mel

'''
mpmInitialize();
'''


configuration
-------------

make mpm.json to your Maya.env directory.

minimum example

'''
[
    {
		"origin": "smiletechnologyunited/maya_package_sample.git"
    }
]
'''

maximum example 
'''
[
    {
		"name": "mpm_package_sample",
		"origin": "https://github.com/smiletechnologyunited/maya_package_sample.git",
		"revision": "9ea698baa952a2ba054925946c8aea6eaf77170c",
		"disable": false
    }
]
'''

support protocol is git(github, bitbucket), svn, hg and fileserver.

recommended git.
not recommended fileserver. :(

gui
---

mel command 'mpmPackageManager'

install packages
----------------

mel command 'mpmInstall'
or 
push 'install all' on mpmPackageManager.

update packages
---------------

if you did not lock revision, you can upadte package.

mel command 'mpmUpdate'
or 
push 'update all' or 'update' for each packages on mpmPackageManager.


enjoy!
... and join contributors!


