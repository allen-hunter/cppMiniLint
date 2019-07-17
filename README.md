# cppMiniLint
A tool for evaluating a large cpp code base for prioritized refactoring opportunities.  
written in python3

cppMiniLint crawls through a codebase and generates a report of files and violations of 
good programming practice.

*More specifically it is a testing framework that allows for easy addition of new tests, 
customizeable parsers, and customizeable reporting.*

### Current Status:
End to end functionality demonstrated, with one test implemented.  Current focus remains on refactoring the framework until
I am satisfied that it is satisfies the open-closed principle.

### Current Tests:
- Detection of code blocks commented out with #if 0 preprocessor commands

## RoadMap:
### Unit Testing
- coverage of existing framework with unit tests to facilitate future development

### Framework Architecture:
- Documentation
- Add a Weighting system to the report which allows you to assign a weight to a test, 
  and then multiply that by the number of violations and the number of times the file is referenced
- Switch from command line to configuration file architecture
- Extend parser with pygccxml

### Tests:
- Detection of long files
- Detection of uncopywrited files
- Detection of long functions <sup>1</sup>
- Detection of large classes <sup>1</sup>
- Detection of unsearchable names <sup>1</sup>
- Detection of symbols that don't have a component in the english language <sup>1</sup>

1: should occur after pygccxml is incorportated into the parser
### Reporting:
- Files in report organized by a "badness rating" which is a product of weighted test violations multiplied by the frequency of references to that file, so that you can focus efforts on the dirtiest code most likely to be read by other programmers
