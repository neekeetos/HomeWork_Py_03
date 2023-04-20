N = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
eng_dic = {1:'AEIOULNSTR',2:'DG',3:'BCMP',4:'FHVWY',5:'K',8:'JZ',10:'QZ'}
rus_dic = {1:'АВЕИНОРСТ',2:'ДКЛМПУ',3:'БГЁЬЯ',4:'ЙЫ',5:'ЖЗХЦЧ',8:'ШЭЮ',10:'ФЩЪ'}
word = input('Введите слово: ').upper()
if N == 1:
	print('Вы получаете', sum([k for i in word for k, v in eng_dic.items() if i in v]), 'очков')
elif N == 0:
	print('Вы получаете', sum([k for i in word for k, v in rus_dic.items() if i in v]), 'очков')