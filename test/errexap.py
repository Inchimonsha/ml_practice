try:
    int('N/A')
except ValueError as e:
    print('Failed:', e)
else:
    print("else")
finally:
    print("fin")
# print(e)