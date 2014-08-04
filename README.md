#PREPARATION
* The ports in ./ports should be copied into your ports tree
    - <code>cp -R ports/* /usr/ports/</code>

* Some user(s) and group(s) need to be added to '/usr/ports/UIDs' and '/usr/ports/GIDs' before compiling Ports or PBIs.
    - /usr/ports/UIDs
        - <code>media:*:816:816::0:0:Media Plugins Daemon:/nonexistent:/usr/sbin/nologin</code>
        - <code>syncthing:*:819:819::0:0:Syncthing Daemon:/nonexistent:/usr/sbin/nologin</code>

    - /usr/ports/GIDs
        - <code>media:*:816:</code>
        - <code>syncthing:*:819:</code>

* Compile
    - <code>pbi_makeport -c ./plugins/**NAME** -o ./pbi --pkgdir ./pkg/**NAME** **CATEGORY/NAME**</code>
