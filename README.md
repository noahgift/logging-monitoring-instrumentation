[![AWS Amazon Linux 2 3.7.9](https://github.com/noahgift/logging-monitoring-instrumentation/actions/workflows/main.yml/badge.svg)](https://github.com/noahgift/logging-monitoring-instrumentation/actions/workflows/main.yml)

# logging-monitoring-instrumentation
A brief repository on logging monitoring and instrumentation in Python

## Items for you to solve

* Toggle log levels from debug to info to etc using config file
* Add a file handler and [emit logs to a file](https://docs.python.org/3/howto/logging.html).  Use `tail -f` to view it.  What does `tail -f` do? 
* Use the `python-json-logger` and convert log message to a JSON format:  https://github.com/madzak/python-json-logger

## Next Steps

* Convert Daemon to click command-line tool and let `--level` be set via a flag.
* Run Daemon to background with `python daemon.py &` # what happens?
* Run Daemon to background with `python daemon.py &` the type `fg` # what happens?  Can you kill it?
* Run Daemon in `screen` and [detach and reattach](https://askubuntu.com/questions/302662/reattaching-to-an-existing-screen-session).
* Can you use a [Daemon library](https://pagure.io/python-daemon/)?  Is this better?

## Dashboard Next Steps

* Send the output of the daemon to AWS:  Cloudwatch, SNS, Kinesis, etc
  * [logging to AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html)   
* Dashboard your daemon output by counting the occurrences
* Log via an AWS Compute Unit:  AWS Lambda, ECS or App Runner
  *  [Try co-pilot](https://aws.github.io/copilot-cli/)
* Use someform of tracing and trace code:  X-Ray/`strace` etc.  What does `strace` do?



