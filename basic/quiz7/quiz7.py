for i in range(1, 51):
    report_file = open("quiz7/week {0}.txt".format(i), "w", encoding = "utf8")
    report_file.write("- week {0} report -".format(i))
    report_file.write("\n department: ")
    report_file.write("\n name: ")
    report_file.write("\n summary of work: ")
    report_file.close()
