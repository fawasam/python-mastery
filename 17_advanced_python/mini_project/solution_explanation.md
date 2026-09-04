# Advanced Python Mini Project Breakdown

## Architectural Highlights
1. **Descriptors (`FieldDescriptor`)**: Intercepts attribute assignment to perform strict runtime type checking (`isinstance`).
2. **Metaclasses (`ModelMeta`)**: Intercepts class definition to automatically register descriptor fields into `_fields`.
3. **AST Inspection**: Uses `ast.parse()` and `ast.walk()` for static structure analysis.
