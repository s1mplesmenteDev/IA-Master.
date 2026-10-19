from langchain-experimental.utilities import PythonREPL 

python_repl = PythonREPL()
result = python_repl.run({codigo})
print(result)
