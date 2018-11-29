![Greenbone Logo](https://www.greenbone.net/wp-content/uploads/gb_logo_resilience_horizontal.png)

# ospd-debsecan

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/greenbone/ospd-debsecan/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/greenbone/ospd-debsecan/?branch=master)
[![code test coverage](https://codecov.io/gh/greenbone/ospd-debsecan/branch/master/graph/badge.svg)](https://codecov.io/gh/greenbone/ospd-debsecan)
[![CircleCI](https://circleci.com/gh/greenbone/ospd-debsecan.svg?style=svg)](https://circleci.com/gh/greenbone/ospd-debsecan)

This is an OSP server implementation to allow GVM to remotely control
a `debsecan` scanner, see <http://www.enyo.de/fw/software/debsecan/>.

`ospd-debsecan` identifies vulnerable packages on the Debian system it is
executed against.

Once running, you need to configure the Scanner for Greenbone Vulnerability
Manager, for example via the web interface Greenbone Security Assistant.
Then you can create scan tasks to use this scanner.

## Installation

### Requirements

Python 3 and later is supported.

Beyond the [ospd base library](https://github.com/greenbone/ospd),
`ospd-debsecan` has dependencies on the following Python package:

- `paramiko`

There are no special installation aspects for this module beyond the general
installation guide for ospd-based scanners.

Please follow the general installation guide for ospd-based scanners:

  <https://github.com/greenbone/ospd/blob/master/doc/INSTALL-ospd-scanner.md>

## Usage

Starting a scan requires an SSH credential parameter because `ospd-debsecan`
needs to login on the target systems to run the locally installed `debsecan`
tool.

Apart from this, there are no special usage aspects for this module beyond the
generic usage guide.

Please follow the general usage guide for ospd-based scanners:

  <https://github.com/greenbone/ospd/blob/master/doc/USAGE-ospd-scanner.md>

## Support

For any question on the usage of ospd-debsecan please use the [Greenbone
Community Portal](https://community.greenbone.net/c/gse). If you found a
problem with the software, please [create an
issue](https://github.com/greenbone/ospd-debsecan/issues) on GitHub. If you are
a Greenbone customer you may alternatively or additionally forward your issue
to the Greenbone Support Portal.

## Maintainer

This project is maintained by [Greenbone Networks
GmbH](https://www.greenbone.net/).

## Contributing

Your contributions are highly appreciated. Please [create a pull
request](https://github.com/greenbone/ospd-debsecan/pulls) on GitHub. Bigger
changes need to be discussed with the development team via the [issues section
at GitHub](https://github.com/greenbone/ospd-debsecan/issues) first.

## License

Copyright (C) 2015-2018 [Greenbone Networks GmbH](https://www.greenbone.net/)

Licensed under the [GNU General Public License v2.0 or later](COPYING).
