import os
import sys
import xmlparser
import constants as cst
import manager


##path_dir = os.path.join(cst.PATH)
path_config_file = os.path.join(cst.CONFIG_FILE)
path_vps = os.path.join(cst.VP_PATH)
path_output = os.path.join(cst.OUTPUT_FILE)



def main():

    # Instance the manager

    m = manager.Manager()

    # Search files
    m.search(path_vps, m.extract_names(path_config_file))

    # get the info to write
    to_wright = m.collect(cst.CODE_LIST_2, m.xml_files)

    # write into output file
    m.wright(to_wright, path_output, cst.CODE_LIST_2)



if __name__ == '__main__':
    main()
