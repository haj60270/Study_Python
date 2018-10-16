#--------------------#
#    配列・連想配列
#--------------------#
# no.01 タプル
# 複数の要素から構成されたそれを１つのモノとして扱う機能
# リストとの違いは、作成した後で要素の追加や削除が可能か否か
#--------------------#

import datetime

def get_today():
	today = datetime.datetime.today()
	value = (today.year, today.month, today.day)
	
	return value
	
test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])

#--------------------#
# no.02 リスト
# タプルとと違い、作成した後に要素の追加や削除が可能
#--------------------#
# 02-01. リストの基本

test_list_1 = ['Pyhon', '-', 'ista', '.', 'net']
print(test_list_1)

print('------------------------------------')

for i in test_list_1:
	print(i)
	
# 02-02. 要素の追加

test_list_1 = []
print(test_list_1)

print('------------------------------------')

test_list_1.append('Python')
test_list_1.append('-')
test_list_1.append('ista')
test_list_1.append('.')
test_list_1.append('net')
print(test_list_1)

print('------------------------------------')

# no.02-03 インデックスを指定して追加

test_list_1 = ['Python', 'ista', 'net']
print(test_list_1)

print('------------------------------------')

test_list_1.insert(1, '-')
test_list_1.insert(3, '.')
print(test_list_1)

test_list_1.insert(0, 'http://')
print(test_list_1)

print('------------------------------------')

# no.02-04 要素の削除1
# removeは最初に見つかった要素のみ削除する

test_list_1 = ['1', '2', '3', '2', '1']
print(test_list_1)

print('------------------------------------')

test_list_1.remove('2')
print(test_list_1)

print('------------------------------------')

# no.02-05 要素の削除2
# popは指定のインデックス値に存在する要素の削除を行い、
# 削除された要素を戻り値として返す。
# 引数なしで使用すると末尾の要素が削除される

test_list_1 = ['1', '2', '3', '2', '1']
print(test_list_1)

print('------------------------------------')

print(test_list_1.pop(1))
print(test_list_1)
print(test_list_1.pop())
print(test_list_1)

print('------------------------------------')

# no.02-06 要素のインデックスの取得
# indexは最初に見つかった要素のインデックス値のみ取得できる

test_list_1 =['100', '200', '300', '200', '100']
print(test_list_1.index('200'))

print('------------------------------------')

# no.02-07 リスト内での要素数を取得

test_list_1 =['100', '200', '300', '200', '100']
print(test_list_1.count('200'))

print('------------------------------------')

#--------------------#
# no.03 ディクショナリ
# keyとvalueをセットにする
#--------------------#
# no.03-01 ディクショナリの基本

test_dict_1 = {'YEAR':'2018', 'MONTH':'10', 'DAY':'11'}
print(test_dict_1)

for i in test_dict_1:
	print(i)
	print(test_dict_1[i])
	print('-----')
	
print('------------------------------------')

# no.03-02 valueの取得

