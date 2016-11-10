#!/usr/bin/env bash

function restart_edxapp {
    sudo /edx/bin/supervisorctl restart edxapp:
}

function  remove {
    sudo -u edxapp /edx/bin/pip.edxapp uninstall -y xdone-xblock
}

function install {
    sudo -u edxapp /edx/bin/pip.edxapp install ./
}

function reinstall {
	remove
    install
}

case "$1" in
 install-fullstack)
	    install
        restart_edxapp
	;;

 remove-fullstack)
	    remove
	    restart_edxapp
   ;;

 reinstall-fullstack)
	    reinstall
	    restart_edxapp
	;;

 install-devstack)
	    install
	;;

 remove-devstack)
	    remove
   ;;

 reinstall-devstack)
	    reinstall
	;;
 *)
	echo "Usage: ./command.sh {install-[fullstack|devstack]|remove-[fullstack|devstack]|reinstall-[fullstack|devstack]}" >&2
	exit 1
	;;
esac
exit 0