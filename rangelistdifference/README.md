# RangeListDifference
A program to subtract two lists containing pairwise range of values.

### Input
* -a = the range values for the first list
* -b = the range values for the second list
### Output
* the first list of range values
* the second list of range values
* the list of range values after difference of second list from first list

# Run Instructions
First clone the repository 
```git clone <repo_url>```

## Run using docker
```docker built -t . rangelistdiff:v1```  
```docker run rangelistdiff:v1 -a <space_separated_values> -b <space_separated_values>```
## Run python script
```python range_diff.py -a <space_separated_values> -b <space_separated_values>```

# Example
list A = [(1, 3), (4, 7), (13, 14), (18, 20)]  
list B = [(2, 5), (8, 13), (17, 21)]

```docker run rangelistdiff:v1 -a 1 3 4 7 13 14 18 20 -b 2 5 8 13 17 21```  
[(1, 3), (4, 7), (13, 14), (18, 20)]  
[(2, 5), (8, 13), (17, 21)]  
[(1, 2), (5, 7), (13, 14)]  
  
```python range_diff.py -a 1546333200 1546340400 1546347600 1546354800 -b 1546333200 1546334100 1546336800 1546337700 1546345800 1546358400```  
[(1546333200, 1546340400), (1546347600, 1546354800)]  
[(1546333200, 1546334100), (1546336800, 1546337700), (1546345800, 1546358400)]  
[(1546334100, 1546336800), (1546337700, 1546340400)]  
