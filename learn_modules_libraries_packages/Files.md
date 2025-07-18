# JSON/YAML File Formats

JSON:
 
```
{
    "name": "John Doe",
    "age": 30,
    "isStudent": false,
    "courses": ["Python", "DevOps"],
    "address": {
            "street": "123 Main St",
            "city": "Anytown"
    }
}
```

- Uses [] for define lists
- dictionary format, {}
- double quotes for keys and string values

YAML:

```
name: John Doe
age: 30
isStudent: false
courses:
    - Python
    - DevOps
address:
    street: 123 Main St
    city: Anytown
```


- uses hyphens for lists
- strings don't need quotes
- indenting is necessary for nested lists, dict