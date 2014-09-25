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
