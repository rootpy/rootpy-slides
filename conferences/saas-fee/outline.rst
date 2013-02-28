=====================
rootpy: Pythonic ROOT
=====================
---------------------------------------------
ROOT Users Workshop, Saas-Fee, March 13, 2013
---------------------------------------------

What's the problem?
===================

* Highlight current deficiencies in ROOT with Python.
* Show concrete examples of "gotchas" and awkward code.
* Ad hoc workarounds implemented by many.
* Lack of integration with other powerful scientific Python packages.

What does rootpy offer?
=======================

Main body of talk here. Need to keep it brief and concise.

* trees
* plotting
* matplotlib interface
* memory management
* context managers
* root_numpy
* etc.

The future of rootpy
====================

* Larger documentation coverage. This is important.
* More examples.
* Automatic wrapping of ROOT methods by parsing method signatures.
   - If a method expects a TColor, rootpy can accept any color matplotlib
     accepts and then convert it into ROOT form before passing to the ROOT method.
   - Reduce the amount of code in rootpy.
* TMVA:
   - Feed TMVA NumPy arrays instead of TTrees. 
* RooFit and RooStats:
   - Wrapping RooArgSet as set() and RooArgList as list(), etc.
   - Create RooDataSets from NumPy arrays.

How can I contribute?
=====================

* Using Git for source code management. See next presentation.
* Development is community-driven; made easy by all of Github's "social coding"
  features.
* Cost of submitting issues (bug reports) is low.
* Cost of contibuting is low; anyone can fork the repository and later submit a
  pull request. Git is much better here than Subversion.
* Contributions are reviewed by peers before merging into the main branch.
* No politics. Just a circle of "trusted" developers who have the ability to
  merge commits into the main branch after they have been reviewed.
* All new code is automatically tested against our test suite, that must pass.
  Code that introduces new functionality should bring new unit tests with it;
  untested code is bad code.
* We use Travis CI (https://travis-ci.org/) to perform continuous integration of
  all contributions.
