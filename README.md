extraimport
===========

Utilities to be used at import time

lazyimport
-----------
Simple circular dependency resolver - creates a stub object
for the module to be imported in the future, so that when
the module is used inside for the first time inside a function
later, the stub is replaced by the actual module in a seamless way.

ROADMAP
--------
1. Evolve lazyimport to work with packages and more specific syntaxes

2. Port over "MapGetter" from the `extradict` package to allow
using the `import` statement to retrieve object attributes.
