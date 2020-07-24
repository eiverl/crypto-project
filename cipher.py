#Made by Eiverl

import os

class CaesarCipher:
	
	#select Mode
	def selectMode(self):
		while True:
			print("암호화하려면 E, 복호화하려면 D를 입력해주세요.")
			self.mode = input().upper()
			if self.mode == 'E' or self.mode == 'D':
				return self.mode

	#input key file
	def find_key_file(self):
		while True:
			try:
				print("key File의 이름을 정확히 입력해주세요.")
				key_name = str(input())
				key_open = open(os.getcwd()+"/"+key_name+".txt", mode = "r")
				self.key = key_open.readline().strip('\n')
				key_open.close()
				for i in '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'.split():
					if self.key == i:
						return self.key
				print("유효하지 않은 값입니다. key file의 내용을 확인해주세요.")
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
				
				
	#input plain text
	def find_plain_text(self):
		while True:
			cipher_text = ""
			try:
				print("암호화할 평문 파일을 찾습니다.")
				plain_name = str(input())
				plain_open = open(os.getcwd()+"/"+plain_name+".txt", mode = "r")
				plain_text = plain_open.readline().strip('\n').upper()
				plain_open.close()
				
				for i in plain_text:
					cipher_num = 0
					if i == " ":
						cipher_text = cipher_text + " "
					else:
						cipher_num = ord(i) + int(self.key)
						if cipher_num > 90:
							cipher_num = ord(i) - (26 - int(self.key))
						cipher_text = cipher_text + chr(cipher_num)
					
				cipher_file = open(os.getcwd()+"/"+plain_name+"_1E.txt", mode = "w")
				cipher_file.write(cipher_text)
				cipher_file.close()
				print("암호화 완료!!! plain text file 의 이름에 _1E를 붙여 텍스트 파일로 저장했습니다.")
				break
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("유효하지 않은 값입니다. Plain text file의 내용을 확인해주세요.")

				
	#input cipher text
	def find_cipher_text(self):
		while True:
			plain_text = ""
			try:
				print("복호화할 암호문 파일을 찾습니다.")
				cipher_name = str(input())
				cipher_open = open(os.getcwd()+"/"+cipher_name+".txt", mode = "r")
				cipher_text = cipher_open.readline().strip('\n').upper()
				cipher_open.close()
				
				for i in cipher_text:
					plain_num = 0
					if i == " ":
						plain_text = plain_text + " "
					else:
						plain_num = ord(i) - int(self.key)
						if plain_num < 65:
							plain_num = ord(i) + (26 - int(self.key))
						plain_text = plain_text + chr(plain_num)
						
				plain_file = open(os.getcwd()+"/"+cipher_name+"_1D.txt", mode = "w")
				plain_file.write(plain_text)
				plain_file.close()
				print("복호화 완료!!! cipher text file 의 이름에 _1D를 붙여 텍스트 파일로 저장했습니다.")
				break
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("유효하지 않은 값입니다. Plain text file의 내용을 확인해주세요.")
				
				
class simpleSubtitution:
		
	#select Mode
	def selectMode(self):
		while True:
			print("암호화하려면 E, 복호화하려면 D를 입력해주세요.")
			self.mode = input().upper()
			if self.mode == 'E' or self.mode == 'D':
				return self.mode
				
	def find_key_file(self):
		while True:
			try:
				print("key File의 이름을 정확히 입력해주세요.")
				key_name = str(input())
				key_open = open(os.getcwd()+"/"+key_name+".txt", mode = "r")
				key = key_open.readline().strip('\n')
				key_open.close()
				for i in key:
					for j in (1, 10):
						if str(i) == str(j):
							raise ValueError
				for i in key:
					l = 0
					l = l + ord(i)
					self.key = l%26
				return self.key
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("Key 값이 유효하지 않습니다.")
				
	
				
	def find_plain_text(self):
		self.table1 = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
		self.table2 = "Q A Z C D E T G B M J U O L P K I N H Y R F V X S W".split()
		while True:
			cipher_text = ""
			try:
				print("암호화할 평문 파일을 찾습니다.")
				plain_name = str(input())
				plain_open = open(os.getcwd()+"/"+plain_name+".txt", mode = "r")
				plain_text = plain_open.readline().strip('\n').upper()
				plain_open.close()
				
				cip = []
				cipher_t = []
				
				for i in plain_text:
					i = ord(i)
					cip.append(i)	
					
				for i in cip:
					for j in range(0, 26):
						if self.table1[j] == chr(i):
							if (j+self.key) > 26:
								cipher_t.append(self.table2[self.key - 26 + j])
							else:
								cipher_t.append(self.table2[self.key + j])
				
				for i in cipher_t:
					cipher_text = cipher_text + i
					
				cipher_file = open(os.getcwd()+"/"+plain_name+"_2E.txt", mode = "w")
				cipher_file.write(cipher_text)
				cipher_file.close()
				print("암호화 완료!!! plain text file 의 이름에 _2E를 붙여 텍스트 파일로 저장했습니다.")
				break	
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("유효하지 않은 값입니다. Plain text file의 내용을 확인해주세요.")	
				
				
	def find_cipher_text(self):
		self.table1 = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
		self.table2 = "Q A Z C D E T G B M J U O L P K I N H Y R F V X S W".split()
		while True:
			plain_text = ""
			try:
				print("복호화할 암호문 파일을 찾습니다.")
				cipher_name = str(input())
				cipher_open = open(os.getcwd()+"/"+cipher_name+".txt", mode = "r")
				cipher_text = cipher_open.readline().strip('\n').upper()
				cipher_open.close()			

				pla = []
				plain_t = []
				
				for i in cipher_text:
					i = ord(i)
					pla.append(i)
					
				for i in pla:
					for j in range(0, 26):
						if self.table2[j] == chr(i):
							if (j-self.key) < 0:
								plain_t.append(self.table1[j-self.key+26])
							else:
								plain_t.append(self.table1[j-self.key])
				
				for i in plain_t:
					plain_text = plain_text + i
					
				plain_file = open(os.getcwd()+"/"+cipher_name+"_2D.txt", mode = "w")
				plain_file.write(plain_text)
				plain_file.close()
				print("복호화 완료!!! cipher text file 의 이름에 _2D를 붙여 텍스트 파일로 저장했습니다.")
				break
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("유효하지 않은 값입니다. cipher text file의 내용을 확인해주세요.")	
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("유효하지 않은 값입니다. Plain text file의 내용을 확인해주세요.")
				
				
class OTP_with_XOR:

	#select Mode
	def selectMode(self):
		while True:
			print("암호화하려면 E, 복호화하려면 D를 입력해주세요.")
			self.mode = input().upper()
			if self.mode == 'E' or self.mode == 'D':
				return self.mode

	def find_key_file(self):
		while True:
			try:
				print("key File의 이름을 정확히 입력해주세요.")
				key_name = str(input())
				key_open = open(os.getcwd()+"/"+key_name+".txt", mode = "r")
				self.key = key_open.readline().strip('\n').upper()
				key_open.close()
				for i in self.key:
					for j in (1, 10):
						if str(i) == str(j):
							raise ValueError
				return self.key
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("Key 값이 유효하지 않습니다.")
				
	def find_plain_text(self):
		while True:
			cipher_text = ""
			try:
				print("암호화할 평문 파일을 찾습니다.")
				plain_name = str(input())
				plain_open = open(os.getcwd()+"/"+plain_name+".txt", mode = "r")
				plain_text = plain_open.readline().strip('\n').upper()
				plain_open.close()
				
				cip = []
				key_f = []
				cipher_num = []
				
				for i in plain_text:
					i = ord(i) - 65
					cip.append(i)
				
				for i in self.key:
					i = ord(i) - 65
					key_f.append(i)
				
				repeat = 1
				for i in range(len(cip)):
					if i > len(key_f) - 1:
						j = i - (len(key_f)*repeat)
						repeat += 1
						number = key_f[j]^cip[i]
						cipher_num.append(number)
					else:
						number = key_f[i]^cip[i]
						cipher_num.append(number)
			
				for i in cipher_num:
					if i > 25:
						i = i - 25 + 97
						cipher_text += (chr(i))
					else:
						i = i + 65
						cipher_text += (chr(i))					
									
					
				cipher_file = open(os.getcwd()+"/"+plain_name+"_3E.txt", mode = "w")
				cipher_file.write(cipher_text)
				cipher_file.close()
				print("암호화 완료!!! plain text file 의 이름에 _3E를 붙여 텍스트 파일로 저장했습니다.")
				break	
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("유효하지 않은 값입니다. Plain text file의 내용을 확인해주세요.")

				
	def find_cipher_text(self):
		while True:
			plain_text = ""
			try:
				print("복호화할 암호문 파일을 찾습니다.")
				cipher_name = str(input())
				cipher_open = open(os.getcwd()+"/"+cipher_name+".txt", mode = "r")
				cipher_text = cipher_open.readline().strip('\n')
				cipher_open.close()
								
				pla = []
				key_f = []
				plain_num = []		
				repeat = 1				
								
				for i in cipher_text:
					if ord(i) > 90:
						i = ord(i) - 72
					else:
						i = ord(i) - 65
					pla.append(i)
				
				for i in self.key:
					i = ord(i) - 65
					key_f.append(i) 	
					
				for i in range(len(pla)):
					if i > len(key_f) - 1:
						j = i - (len(key_f)*repeat)
						repeat += 1
						number = key_f[j]^pla[i]
						plain_num.append(number)
					else:
						number = key_f[i]^pla[i]
						plain_num.append(number)
			
				for i in plain_num:
					if i > 25:
						i = i - 25 + 65
						plain_text += (chr(i))
					else:
						i = i + 65
						plain_text += (chr(i))
						
						
				plain_file = open(os.getcwd()+"/"+cipher_name+"_3D.txt", mode = "w")
				plain_file.write(plain_text)
				plain_file.close()
				print("복호화 완료!!! cipher text file 의 이름에 _3D를 붙여 텍스트 파일로 저장했습니다.")
				break
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("유효하지 않은 값입니다. cipher text file의 내용을 확인해주세요.")	



class VigenereCipher:

	#select Mode
	def selectMode(self):
		while True:
			print("암호화하려면 E, 복호화하려면 D를 입력해주세요.")
			self.mode = input().upper()
			if self.mode == 'E' or self.mode == 'D':
				return self.mode
				
				
	#input key file
	def find_key_file(self):
		while True:
			try:
				print("key File의 이름을 정확히 입력해주세요.")
				key_name = str(input())
				key_open = open(os.getcwd()+"/"+key_name+".txt", mode = "r")
				self.key = key_open.readline().strip('\n').split(';')
				key_open.close()
				for i in self.key:
					for j in '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'.split():
						if i == j:
							i = int(i)
					if type(i) != type(1):
						raise ValueError
				return self.key
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("Key 값이 유효하지 않습니다.")
				
	def find_plain_text(self):
		while True:
			cipher_text = ""
			try:
				print("암호화할 평문 파일을 찾습니다.")
				plain_name = str(input())
				plain_open = open(os.getcwd()+"/"+plain_name+".txt", mode = "r")
				plain_text = plain_open.readline().strip('\n').upper()
				plain_open.close()
				
				cip = []
				key_f = []
				repeat = 0
				number = 0
				
				for i in plain_text:
					i = ord(i) - 65
					cip.append(i)

				for i in self.key:
					key_f.append(int(i))
					
				for i in range(len(cip)):
					if i > len(key_f) - 1:
						j = i - len(key_f) - repeat
						repeat += 1
						number = int(key_f[j])+int(cip[i])
						if number > 25:
							number = number - 25
							cipher_text += (chr(number+97))
						else:
							cipher_text += (chr(number+65))
					else:
						number = int(key_f[i])+int(cip[i])
						if number > 25:
							number = number - 25
							cipher_text += (chr(number+97))
						else:
							cipher_text += (chr(number+65))
				
				cipher_file = open(os.getcwd()+"/"+plain_name+"_4E.txt", mode = "w")
				cipher_file.write(cipher_text)
				cipher_file.close()
				print("암호화 완료!!! plain text file 의 이름에 _4E를 붙여 텍스트 파일로 저장했습니다.")
				break	
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("유효하지 않은 값입니다. Plain text file의 내용을 확인해주세요.")
				

	def find_cipher_text(self):
		while True:
			plain_text = ""
			try:
				print("복호화할 암호문 파일을 찾습니다.")
				cipher_name = str(input())
				cipher_open = open(os.getcwd()+"/"+cipher_name+".txt", mode = "r")
				cipher_text = cipher_open.readline().strip('\n')
				cipher_open.close()			
				
				pla = []
				key_f = []	
				repeat = 0
				number = 0
				
				for i in cipher_text:
					if ord(i) > 90:
						i = ord(i) - 72
					else:
						i = ord(i) - 65
					pla.append(i)
					
				for i in self.key:
					key_f.append(int(i))
								
				for i in range(len(pla)):
					if i > len(key_f) - 1:
						j = i - len(key_f) - repeat
						repeat += 1
						number = int(key_f[j])-int(pla[i])
						if number < 0:
							number = abs(number)
						
						plain_text += (chr(number+65))
					else:
						number = int(key_f[i])-int(pla[i])
						if number < 0:
							number = abs(number)
						plain_text += (chr(number+65))
				
				plain_file = open(os.getcwd()+"/"+cipher_name+"_4D.txt", mode = "w")
				plain_file.write(plain_text)
				plain_file.close()
				print("복호화 완료!!! cipher text file 의 이름에 _4D를 붙여 텍스트 파일로 저장했습니다.")
				break
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("유효하지 않은 값입니다. cipher text file의 내용을 확인해주세요.")	
				
			except FileNotFoundError:
				print("파일을 찾을 수 없습니다.")
			except ValueError:
				print("유효하지 않은 값입니다. Plain text file의 내용을 확인해주세요.")				
				

a = CaesarCipher()
b = simpleSubtitution()
c = OTP_with_XOR()
d = VigenereCipher()
while True:
	print("-*- " + "-"*10 + " 암호화 프로그램 입니다. " + "-"*10 + " -*-")
	print("1. 시저암호, 2. 단일 치환 암호, 3. OTP, 4. 비즈네르 암호")
	print("다음 보기 중 골라 '숫자'만 입력해 주세요.")
	print("프로그램 종료를 원하시면 '5'를 입력해 주세요......")
	selectcipher = int(input())
	if selectcipher == 1:
		print(" '1. 시저암호' 를 선택하셨습니다. ")
		mode = a.selectMode()
		a.find_key_file()
		if mode == "E":
			a.find_plain_text()
		else:
			a.find_cipher_text()
			
	elif selectcipher == 2:
		print(" '2. 단일 치환 암호' 를 선택하셨습니다. ")
		mode = b.selectMode()
		b.find_key_file()
		if mode == "E":
			b.find_plain_text()
		else:
			b.find_cipher_text()
			
	elif selectcipher == 3:
		print(" '3. OTP' 를 선택하셨습니다. ")
		mode = c.selectMode()
		c.find_key_file()
		if mode == "E":
			c.find_plain_text()
		else:
			c.find_cipher_text()

	elif selectcipher == 4:
		print(" '4. 비즈네르 암호' 를 선택하셨습니다. ")
		mode = d.selectMode()
		d.find_key_file()
		if mode == "E":
			d.find_plain_text()
		else:
			d.find_cipher_text()
	
	elif selectcipher == 5:
		break
		
	else:
		print("잘못된 입력입니다.")