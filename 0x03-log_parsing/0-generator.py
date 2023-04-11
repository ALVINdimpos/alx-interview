#!/usr/bin/env python3

import random
import sys
from datetime import datetime
from time import sleep

# Generate random log lines in expected format
for i in range(10000):
    ip_address = ".".join(str(random.randint(1, 255)) for _ in range(4))
    timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    method = "GET"
    resource = "/projects/260"
    protocol = "HTTP/1.1"
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)
    log_line = "{} - [{}] \"{} {} {}\" {} {}\n".format(ip_address, timestamp, method, resource, protocol, status_code, file_size)
    sys.stdout.write(log_line)
    sys.stdout.flush()
    sleep(random.random())
