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
* svn (for checkout svn repository)

setup
-----

download and copy mpm to your scripts path.

edit userSetup.mel

```
mpmInitialize();
```


configuration
-------------

make mpm.conf to your Maya.env directory.

small example

```
[
    {"origin": "smiletechnologyunited/maya_package_sample.git"}
]
```

large example 
```
[
    {
		"name": "mpm_plugins_manager",
		"origin": "git://github.com/smiletechnologyunited/mpm_plugins_manager.git",
		"revision": "9ea698baa952a2ba054925946c8aea6eaf77170c",
    },
    {
		"name": "mpm_package_sample",
		"origin": "https://github.com/smiletechnologyunited/maya_package_sample.git",
		"revision": "9ea698baa952a2ba054925946c8aea6eaf77170c",
    }
]
```

support protocol is git(github, bitbucket), svn, and fileserver.

recommended git.
not recommended fileserver. :(

install packages
----------------

MEL command 'mpmInstall'

update packages
---------------

if you did not lock revision, you can upadte packages.

MEL command 'mpmUpdate'


----


enjoy!

... and join contributors!


