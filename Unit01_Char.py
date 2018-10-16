#--------------#
#   文字列操作   
#--------------#
# --- no.01 文字列の基礎
print('test_str')

# --- no.02 文字列の連結1
test_str = 'test'
test_str = test_str + '_string'
print(test_str)

# --- no.03 文字列の連結2
test_str = '123'
test_str += '456'
test_str += '789'
print(test_str)

# --- no.04 文字列の連結3
test_str = 'abc' * 3
print(test_str)

# --- no.05 文字列の連結4
test_int = 100
print(str(test_int)+'円')

# --- no.06 文字列の置換
test_str = 'test_str'
print(test_str.replace('str', 'string'))

# --- no.07 文字列の分割
test_str = 'test_string'
dev_str = test_str.split('_')
for s in dev_str:
	print(s)

# --- no.08 文字列の桁揃え1
test_str = '1234'
print(test_str.rjust(8, 'a'))

# --- no.09 文字列の桁揃え2
test_str = '1234'
print(test_str.zfill(8))
print(test_str.zfill(2)) #文字数以下をしていしても桁揃えはされない

# --- no.10 文字列の検索 文字の先頭が任意の文字列か
test_str = 'python-ista'
print(test_str.startswith('python'))
print(test_str.startswith('ista'))

# --- no.11 文字列の検索 任意の文字列含まれているか
test_str = 'python-ista'
print('h' in test_str)
print('z' in test_str)

# --- no.12 大文字・小文字変換
test_str = 'Python-Ista'
print(test_str.upper())
print(test_str.lower())

# --- no.13 先頭、末尾の削除
print('-------------------------')

test_str = '              python-ista'
print(test_str)

test_str = test_str.lstrip()	#引数なしは、空白を除去する
print(test_str)

test_str = test_str.lstrip('python')
print(test_str)

print('-------------------------')
test_str = 'python-ista             '
print(test_str + '/')

test_str = test_str.rstrip()	#引数なしは、空白を除去する
print(test_str + '/')

test_str = test_str.rstrip('-ista')
print(test_str)

print('-------------------------')
