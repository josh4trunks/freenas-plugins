#PREP
* The folders in ./ports should be moved to /usr/ports/
    - <code>mv ./ports/* /usr/ports</code>

* A 'media' user and group need to be added to '/usr/ports/UIDs' and '/usr/ports/GIDs' before compiling Ports or PBIs.
    - /usr/ports/UIDs
        - <code>media:*:999:999::0:0:media Daemon:/nonexistent:/usr/sbin/nologin</code>
    - /usr/ports/GIDs
        - <code>media:*:999:</code>


* Compile
    - <code>pbi_makeport -c ./plugins/**NAME** -o ./pbi --pkgdir ./pkg/ **CATEGORY/NAME**</code>

* I found it necessary to recomplie some of the packages again when switching between plugins
    - <code>rm ./pkg/*</code>

##NOTE
We need to choose a permanent UID/GID name and number (<1000 and not already taken) and submit a patch to FreeBSD in the future.
