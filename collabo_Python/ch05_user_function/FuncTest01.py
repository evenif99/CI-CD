def func01(first, second=5):
    return 2*first+3*second
# end def

su01 = 3
su02 = 5

result = func01(su01, su02)
print('2 * %d + 3 * %d == %d' % (su01, su02, result))

print('2 * %d + 3 * %d == %d' % (4, 7, func01(4,7)))

print('%d' % func01(10))
