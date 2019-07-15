# cppMiniLint
A tool for evaluating a large cpp code base for prioritized refactoring opportunities.  written in python3

cppMiniLint crawls through a codebase and generates a report of files and violations of good programming practice.

*More specifically it is a testing framework that allows for easy addition of new tests, customizeable parsers, and customizeable reporting.*
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
- Refactor observer pattern to be less tightly coupled
- Refactor the communication between parsers and test suites to use a polymorphic message rather than explicit functions
- Add a Weighting system to the report which allows you to assign a weight to a test, and then multiply that by the number of violations and the number of times the file is referenced
### Tests:
- Detection of long files
- Detection of long functions
- Detection of large classes
- Detection of unsearchable names
- Detection of uncopywrited files
- Detection of symbols that don't have a component in the english language

### Reporting:
- Files in report organized by a "badness rating" which is a product of weighted test violations multiplied by the frequency of references to that file, so that you can focus efforts on the dirtiest code most likely to be read by other programmers