# RUTfunctions


Functional helpers for handling RUT Chile written in `Python 3.6` without dependencies

> Helpers funcionales para manipulación de RUT Chileno escritos en `Python 3.6` sin dependencias

--------------------------------------------------------------------------------

## Using:

- rut_clean

```
@param paramrut {string}= 16.761.256-9
@return {string} = 167512569
```

- rut_validate

```
@param paramrut {string} = 16.761.256-9
@return {boolean} = true
```

```python
# Example
rut_validate('167512569')
True
rut_validate('167512568')
False
rut_validate('16.751.256-8')
False
rut_validate('16.751.256-9')
True
```

- rut_format

```
@param paramrut {number/string} = 167512569
@return {string} = 16.761.256-9
```

- rut_get_dv

```
@param paramrut {number/string} = 16751256 / 16.751.256
@return {string} = 9
```

- rut_get_number

```
@param paramrut {string} = 16.751.256-9 / 16751256-9
@return {string} = 16751256
```

- rut_calc_dv

```
@param paramrut {string} = 16.751.256-9 / 16751256-9
@return {string} = 9
```

- rut_add_dv

```
@param paramrut {string} = 16751256
@return {string} = 167512569
```
