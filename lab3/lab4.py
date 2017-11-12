class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.favourite_color=favorite_color
	def eat(self,food):
		self.food= food
		print("yummy!! "+self.name +" is eating "+food)
	def description (self):
		print(self.name+"is" + str(self.age) +"years old and loves the color" + self.favorite_color)
	def rsound(self):
		print(self.sound*3)
a= Animal ("mawww r", "catie" , 2 , "blue")
a.eat("curry")
a.rsound()

class Person (object):
	def __init__(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def breakfast(self,food):
		self.food= food
		print("yummm " + self.food)
	def fsport(self,sport):
		self.sport=sport	
		print("IIIII LOveee" + self.sport)


reeko= Person ("yooo ", 15 , "jerusalem", "male")
reeko.breakfast (" curry")			
reeko.fsport(" basketball")


class Song (object):
	def __init__(self, lyrics):
		self.lyrics=lyrics
	def sing_me(self):
		a=0
		for i in range (len(self.lyrics)):
			print(self.lyrics[a])
			a+=1
flower_song= Song(["Roses are red,",
	"Violets are blue,",
	"I wrote this poem for you."])

flower_song.sing_me()

another_song = ("i'm gonna pop some tags", "only got twenty dollars in my pocket")






