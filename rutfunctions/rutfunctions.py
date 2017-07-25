# create by claudio.dcv@gmail.com
import re
import math


'''
@param paramrut {string}= 16.761.256-9
@return {string} = 167512569
'''
rut_clean = lambda paramrut : re.sub(r'[^0-9kK]+', '', str(paramrut)).upper()


'''
@param paramrut {number/string} = 16751256 / 16.751.256
@return {string} = 9
'''
def rut_calc_dv(paramrut):
    rut = rut_clean(str(paramrut))
    reverse_rut = ''.join(c for c in rut if c.isdigit())[::-1]
    result = 0
    n = 1

    for digit_rut in reverse_rut:
        n += 1
        result += int(digit_rut) * n
        n = 1 if n == 7 else n

    result = 11 - (result % 11)
    result = 0 if result == 11 else result
    return str('K' if result == 10 else result)


'''
@example =
RUT_validate('167512569')
True
RUT_validate('167512568')
False
RUT_validate('16.751.256-8')
False
RUT_validate('16.751.256-9')
True
@param paramrut {string} = 16.761.256-9
@return {boolean} = True
'''
def rut_validate(paramrut):
    rut = str(paramrut)
    if (not re.match(r'^0*(\d{1,3}(\.?\d{3})*)-?([\dkK])$', rut)):
        return False

    rut = rut_clean(rut)

    dv = rut[-1]
    rut_number = rut[0:-1]

    return rut_calc_dv(rut_number) == dv


'''
@param paramrut {number/string} = 167512569
@return {string} = 16.761.256-9
'''
def rut_format(paramrut):
    rut = str(rut_clean(paramrut))
    result = '{}-{}'.format(rut[-4:-1], rut[-1])
    reverse_rut = rut[0:-1][::-1]

    def for_in_rut(i, rr, out):
        out = rr[i:i+3][::-1] + '.' + out
        i += 3
        return out if i > len(rr) else for_in_rut(i, rr, out)

    return for_in_rut(3, reverse_rut, result)


'''
@param paramrut {string} = 16.751.256-9 / 16751256-9
@return {string} = 16751256
'''
rut_get_number = lambda paramrut : rut_clean(paramrut.split('-', 1)[0])


'''
@param paramrut {string} = 16.751.256-9 / 16751256-9
@return {string} = 9
'''
rut_get_dv = lambda paramrut : rut_clean(paramrut.split('-', 1)[1])


'''
@param paramrut {string} = 16751256
@return {string} = 167512569
'''
rut_add_dv = lambda paramrut : '{}{}'.format(paramrut, rut_calc_dv(paramrut))

'''
test

test1 = rut_clean('16.752.156-9');
test2 = rut_calc_dv('16751256');
test3 = rut_validate('16.751.256-9');
test4 = rut_validate('16.751.256-8');
test5 = rut_format('167512569');
test6 = rut_get_number('16751256');
test7 = rut_get_dv('16.751.256-9');
test8 = rut_add_dv('16751256');

print(test1, test2, test3, test4, test5, test6, test7, test8);
result:
('167521569', '9', True, False, '16.751.256-9', '16751256', '9', '16751256-9')
'''
