# bdwgc

Boehm-Demers-Weiser Garbage Collector. A conservative garbage collector for C
and C++.

## Description

This repository provides Sailfish OS packaging for bdwgc.

The bdwgc library is a garbage collecting storage allocator that is intended to
be used as a plug-in replacement for C's malloc.

The library is needed by w3m (a terminal-based web browser), see
https://github.com/llewelld/w3m for more information about this.

## Upstream details

Website: https://www.hboehm.info/gc/

Source code: https://github.com/ivmai/bdwgc

Licence: MIT-style licence, see the upstream/LICENSE file.

## Building

To build the Sailfish OS version, you'll need a copy of the Sailfish SDK
(sometimes refered to as the Sailfish Application SDK) installed, with a
suitable target. See https://docs.sailfishos.org/Tools/Sailfish_SDK/ for more
information about this.

The following steps will grab a copy of the bdwgc source and packaging scripts,
then build the library for Sailfish OS.

```
git clone --recursive https://github.com/llewelld/bdwgc.git
cd bdwgc
sfdk build -d -p
cd ..
```

## Info

Packaged by David Llewellyn-Jones

Website: https://www.flypig.co.uk
