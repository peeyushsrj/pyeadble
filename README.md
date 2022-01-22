# pyeadble
A simple tool, to give rought idea for complexity of your python programs.

![image](https://user-images.githubusercontent.com/5060113/150646611-cf38938e-3bc7-449d-b3e1-f190c05af288.png)

Nth - 1 rule of coding is to write a beautiful and clear python code. One way for this is to minimize no. of lines used in program.
Base on this hypothis, this tool - 

- [ ] Exclude empty lines (`\n`)
- [ ] Exclude lines for package `imports`
- [ ] Exclude lines used for `function definitions`

And thus outputs only logic lines. If you pass number of features, it gives you code density. 

# execude non gui version

```
python code-complexity.py file-to-scan.py 12
```

where 
- `python` must be installed to exucute this.
- `code-complexity.py` is the source written.
- `12` is optional , which is number of features. If passed, it shows outputs code density.

### dm for hosted version (gui based)
