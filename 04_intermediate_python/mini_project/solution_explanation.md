# Solution Explanation: Data Validation & Plugin Processing Engine

## Architectural Breakdown

### 1. Descriptors (`StringField`, `IntegerField`)
We used custom descriptors to replace repetitive validation logic in `__init__` or properties. By defining `__set_name__`, each descriptor manages storage in `instance._<name>` safely without cross-instance data contamination.

### 2. Structural Typing (`Protocol`) & Nominal Typing (`ABC`)
`ProcessorPlugin` uses Python 3.8+ `typing.Protocol` for compile-time duck typing, while `BaseProcessor` provides runtime abstract method enforcement via `abc.ABC`.

### 3. Class Decorators (`@register_plugin`)
Instead of manually adding plugins to a list, `@register_plugin` inspects and registers plugin classes dynamically upon module import.

### 4. Closures (`make_pipeline_runner`)
`make_pipeline_runner` encapsulates the plugin list inside a stateful closure, generating a clean function interface for caller invocation.
