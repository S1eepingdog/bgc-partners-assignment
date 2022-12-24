def output(data, filename):
    """
    output dataframe to file and print log
    :param data: data to be output
    :param filename: file name for output file
    """
    print("output data to {}".format(filename))
    data.to_csv(filename, index=False)
    print("done!")


def skip_comments(filename):
    """
    read file line by line and skip comments
    :param filename: name of file to be read
    :return: yield each line
    """
    with open(filename, 'rb') as f:
        for line in f:
            li = line.strip()
            if not li.startswith(b'#'):
                yield line
