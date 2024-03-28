# Refactor of EDM_Python library

## Goals

- easier interface, i.e. easier library structure, streamlined logical imports
- reuse classes from RDFLib where possible (URIRef, Literal)
- consider removin XSD types if you they don't ease the use of data creation 

## Features the library should support

- at the heart it should be a mapping of the edm to python types. 
- by modelling everything in pydantic, you get validation out of the box. 
- pydantic understands validation as conforming that the output of a model (i.e. any instance of the model) fully conform to the type annotations 
  - pydantic does not use the term validation to express that the Input data was valid or conforms to any schema.
  - pydantic employs or enables you to employ conversions and coercions to create the validated output
- the strength here is: the input data can be anything. 

But this is just the beginning, it should enable us to: 





## Arbitrary Class Instances (former ORM-Mode)

[Pydantic - documentation](https://docs.pydantic.dev/latest/concepts/models/#arbitrary-class-instances)

This would enable us to read data directly from a database or save to it again via the models. 

Would need some tinkering, but get rid of many problems that we might otherwise have. 


## Validtion functions
[Pydantic - documentation] (https://docs.pydantic.dev/latest/concepts/models/#helper-functions)

- model_validate()
  - this is very similar to the __init__ method of the model, except it takes a dict or an object rather than keyword arguments. If the object passed cannot be validated, or if it's not a dictionary or instance of the model in question, a ValidationError will be raised.
- model_validate_json()

## Unitests and Tests in general

consider using hypothesis as testing framework, even though pydantic itself has dropped it's direct support for it. 
[docs hypothesis](https://hypothesis.readthedocs.io/en/latest/)
