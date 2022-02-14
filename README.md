# logging-monitoring-instrumentation
A brief repository on logging monitoring and instrumentation in Python

## Items for you to solve

* Toggle log levels from debug to info to etc using config file
* Add a file handler and [emit logs to a file](https://docs.python.org/3/howto/logging.html) 
* Use the `python-json-logger` and convert log message to a JSON format:  https://github.com/madzak/python-json-logger

## Next Steps

* Convert Daemon to click command-line tool and let `--level` be set via a flag.
* Run Daemon to background with `python daemon.py &` # what happens?
* Run Daemon to background with `python daemon.py &` the type `fg` # what happens?  Can you kill it?
* Run Daemon in `screen` and detach and reattach.

## Dashboard Next Steps

* Send the output of the daemon to AWS:  Cloudwatch, SNS, Kinesis, etc
* Dashboard your daemon output by counting the occurrences
* Log via an AWS Compute Unit:  AWS Lambda, ECS or App Runner
* Use someform of tracing and trace code:  X-Ray/`strace` etc



