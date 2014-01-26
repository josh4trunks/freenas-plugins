#FreeNAS-Plugins
Information for python-based plugins maintained by me can be found [here](http://forums.freenas.org/threads/freenas-9-plugins-sab-sb-cp-hp-maraschino-htpc-mylar-ll-gamez.16200/).


#PREPARATION
* The ports in ./ports should be copied into your ports tree
    - <code>cp -R ports/* /usr/ports/</code>

* A 'media' user and group need to be added to '/usr/ports/UIDs' and '/usr/ports/GIDs' before compiling Ports or PBIs.
    - /usr/ports/UIDs
        - <code>media:*:816:816::0:0:media Daemon:/nonexistent:/usr/sbin/nologin</code>
        - <code>btsync:*:817:817::0:0:btsync Daemon:/nonexistent:/usr/sbin/nologin</code>
    - /usr/ports/GIDs
        - <code>media:*:816:</code>
        - <code>btsync:*:817:</code>

* Compile
    - <code>pbi_makeport -c ./plugins/**NAME** -o ./pbi --pkgdir ./pkg/**NAME** **CATEGORY/NAME**</code>

* You can optionally use libjpeg-turbo by setting the following line in /usr/ports/graphics/py-imaging/Makefile
    - <code>LIB_DEPENDS=    jpeg.11:${PORTSDIR}/graphics/libjpeg-turbo \\</code>
