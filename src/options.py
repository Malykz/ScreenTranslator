import optparse

parse = optparse.OptionParser()

parse.add_option("-p", dest="proxy",
                 help="Set custom Proxy URL", default="https://translate.google.com", metavar="[str]")

parse.add_option("-f", dest="fontSize",
                 help="Set font size", default=25, metavar="[int]")

parse.add_option("--dh", dest="displayHeight",
                  help="Set display size", default="300", metavar="[int]")

parse.add_option("--dw", dest="displayWidth",
                  help="Set display size", default="400", metavar="[int]")

parse.add_option("-k", dest="key",
                 help="Set activate key", default="t")

(options, args) = parse.parse_args()