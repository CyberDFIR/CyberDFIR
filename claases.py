with open("server_log.txt", "r") as rfile, open("errors_only.txt", "w") as wfile:
    for line in rfile:
        if "ERROR" in line:
            wfile.write(line)
