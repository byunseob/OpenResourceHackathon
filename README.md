[![Run on Ainize](https://ainize.ai/static/images/run_on_ainize_button.svg)](http://34.67.222.84/locust/form)

# Locust

[![Build Status](https://img.shields.io/travis/locustio/locust.svg)](https://travis-ci.org/locustio/locust)
[![codecov](https://codecov.io/gh/locustio/locust/branch/master/graph/badge.svg)](https://codecov.io/gh/locustio/locust)
[![license](https://img.shields.io/github/license/locustio/locust.svg)](https://github.com/locustio/locust/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/locustio.svg)](https://pypi.org/project/locustio/)
[![PyPI](https://img.shields.io/pypi/pyversions/locustio.svg)](https://pypi.org/project/locustio/)
[![GitHub contributors](https://img.shields.io/github/contributors/locustio/locust.svg)](https://github.com/locustio/locust/graphs/contributors)

## Links

* Website: <a href="https://locust.io">locust.io</a>
* Documentation: <a href="https://docs.locust.io">docs.locust.io</a>
* Support/Questions: [Slack signup](https://slack.locust.io/)

## Description

Locust is an easy-to-use, distributed, user load testing tool. It is intended for load-testing web sites (or other systems) and
figuring out how many concurrent users a system can handle.

The idea is that during a test, a swarm of locusts will attack your website. The behavior of each locust (or test user if you will) is
defined by you and the swarming process is monitored from a web UI in real-time. This will help you battle test and identify bottlenecks
in your code before letting real users in.

Locust is completely event-based, and therefore it's possible to support thousands of concurrent users on a single machine.
In contrast to many other event-based apps it doesn't use callbacks. Instead it uses light-weight processes, through <a href="http://www.gevent.org/">gevent</a>.
Each locust swarming your site is actually running inside its own process (or greenlet, to be correct).
This allows you to write very expressive scenarios in Python without complicating your code with callbacks.


## Features
* **Write user test scenarios in plain-old Python**<br>
 No need for clunky UIs or bloated XML—just code as you normally would. Based on coroutines instead
of callbacks, your code looks and behaves like normal, blocking Python code.

* **Distributed & Scalable - supports hundreds of thousands of users**<br>
 Locust supports running load tests distributed over multiple machines.
 Being event-based, even one Locust node can handle thousands of users in a single process.
 Part of the reason behind this is that even if you simulate that many users, not all are actively hitting your system. Often, users are idle figuring out what to do next. Requests per second != number of users online.

* **Web-based UI**<br>
 Locust has a neat HTML+JS that shows all relevant test details in real-time. And since the UI is web-based, it's cross-platform and easily extendable.

* **Can test any system**<br>
 Even though Locust is web-oriented, it can be used to test almost any system. Just write a client for what ever you wish to test and swarm it with locusts! It's super easy!

* **Hackable**<br>
 Locust is very small and very hackable and we intend to keep it that way. All heavy-lifting of evented I/O and coroutines are delegated to gevent. The brittleness of alternative testing tools was the reason we created Locust.

## Docker build
```
docker build -t byunseob/locust_helper3 .
```
## Docker run
```
docker run -p 80:80 -p8089:8089 -d byunseob/locust_helper3
```

## locust  초기화 API 호출
```
    curl --location --request POST "HOST/locust" \
      --header "Content-Type: application/json" \
      --data "{
        \"method\":\"get\",
        \"host\":\"http://www.mocky.io/v2/5deae5e13000006f6b2b0b27\",
        \"params\": {
            \"name\": \"byunseob\"
        }
    }"
```


