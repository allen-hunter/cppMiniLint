# cppMiniLint
A tool for evaluating a large cpp code base for prioritized refactoring opportunities.  
written in python3

cppMiniLint crawls through a codebase and generates a report of files and violations of 
good programming practice.

*More specifically it is a testing framework that allows for easy addition of new tests, 
customizeable parsers, and customizeable reporting.*

### Current Status:
- Multiple tests implemented.  
- Files in report organized by a "badness rating" which is a product of weighted test violations 
  multiplied by the frequency of references to that file, so that you can focus efforts on the 
  dirtiest code most likely to be read by other programmers
- Full coverage regression testing via unit tests

Current focus will be on improving the parser to use castxml to
better process cpp, allowing more sophisticated testing

### Current Tests:
- Detection of code blocks commented out with #if 0 preprocessor commands
- Detection of long files
- Detection of uncopyrighted files

## RoadMap:
### Framework Architecture:
- Documentation
- Improve customization of the test run by using a config file that can be overridden via
  command line switches

### Parser:
- Incorporate pygccxml
- symbol detection within member functions (this is not provided by pygccxml/castxml)

### Tests:
- Detection of header protection (ie pragma once or ifdefs)
- Detection of multiple classes within a single header
- Detection of long functions <sup>1</sup>
- Detection of large classes <sup>1</sup>
- Detection of unsearchable names <sup>1</sup>
- Detection of symbols that don't have a component in the english language <sup>1</sup><sup>,2</sup>
- Detection of unused include files

1: should occur after pygccxml is incorportated into the parser
2: should occur after folding in NLTK or SDict
