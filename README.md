mpm
===

Maya Package Manager

preview version.

setup
-----

download and copy mpm to script path and python path.

edit userSetup.mel

'''
mpmInitialize();
'''


configuration
-------------

save mpm.json to Maya.env directory.

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

support git(github, bitbucket), svn, hg and fileserver.

recommented git.
not recommented fileserver. :(

install packages
----------------

mel command 'mpmInstall'
or 
push 'install all' on mpmPackageManager.

update packages
---------------

if you do not lock revision, you can upadte package.

mel command 'mpmUpdate'
or 
push 'update all' or 'update' for each packages on mpmPackageManager.


enjoy!
... and join contributors!


