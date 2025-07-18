# Scripting

## What is scripting?
- to write small, "quick and dirty" programs
- automating repetitive tasks
- manipulate data
- perform certain specific actions that don't need the complexity of a full application
- usually run from command line

## How do we get a script to run from the command line?
- sys module
  - helps us get arguments from the command line

```cmd
python script.py arg1 arg2 arg3
```

example convert JSON to YAML:
- arg1 = file_to_convert.json
- script.py is first argument, index 0
- this is why there is always at least one argument
- so arg1 would be index 1 in the list of arguments