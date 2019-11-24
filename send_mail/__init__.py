import os
from fman import DirectoryPaneCommand, show_alert, YES, NO
from fman.url import as_human_readable
from fman.fs import is_dir, copy, exists, notify_file_added

class SendMail(DirectoryPaneCommand):
    def __call__(self):        
        # get as list of all chosen filenames that need to be attached
        chosenFiles = self.get_chosen_files()
        # create the string for the attachment
        attachment_string = ''
        for it in chosenFiles:
            # save it for comparing later, since zipping a folder will change it.
            itin = str(it)
            # human readable file name
            ithr = as_human_readable(it)
            foldername = ithr.split('/')[-1]
            # check if folder, if so, create a zip file of the folder and add that one to the filename list!
            if is_dir(it):
                # create zipname
                zipname = 'zip://' + ithr + '.zip'
                # make sure the sip file does not exist yet
                if exists(zipname):
                    choice = show_alert('The zip file already exists. Do you want to overwrite it?', buttons=YES|NO, default_button=NO)
                    if choice == NO:
                        return
                # create a zip file, pack the folder into the zip file
                copy(it, zipname + '/' + foldername )
                # inform fman that the zip file exists now
                notify_file_added(zipname)
                # now we want to add the zip file instead of the selected file, so change it before adding it to the string
                it = zipname
            # attach the file to the string of what to attach to the e-mail message
            attachment_string += it
            if itin is not chosenFiles[-1]:
                attachment_string += ','
        # set up the command to start a new e-mail message and attach it
        cmd = 'thunderbird -compose \"attachment=\'' + attachment_string + '\'\"'
        # print the command - untoggle for checking before sending
        # show_alert(cmd)
        # send the command
        os.system(cmd)

