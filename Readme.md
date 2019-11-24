# SendAsEMail fman plugin

**Version 0.1.0**

*Attach files to a new e-mail directly from fman. Currently only Thunderbird is supported.*

This plugin allows the sending of e-mails directly from fman. At the moment it only works
thunderbird on Linux (maybe on OSX, untested) by invoking the thunderbird command:

    thunderbird -compose "attachment='absolute_path_file1,absolute_path_file2,...'"

The command is invoked by using python's os package:

    import os
    os.system(command)

If a folder is chosen, the files will be copied to a zip archive containing the folder, and this file will subsequently be sent. If the zip file already exists, the plugin will ask the user if the zip file should be replaced.

## Key Bindings
 * [Ctrl+S]:    Send E-Mail with given files

Feel free to adjust the KeyBindings to your liking!

## ToDo:
 * More e-mail client support: If you have any ideas on how to implement this, please fill free to open an issue on github or simply edit the plugin and create a pull request.

## Installation:
Use fmans built in plugin installation tools. This will install the release version that is currently created. 

For a testing version, please download the source code and install it into your fman/Plugins/User directory. On linux this would be:

    ~/.config/fman/Plugins/User

