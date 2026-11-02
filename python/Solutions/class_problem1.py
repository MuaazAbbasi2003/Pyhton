class User:
    def __init__(self,user_id,name):
        self.userId=user_id
        self.name=name
        self.followers=0
        self.following=0

    def follow(self,user):
        self.following +=1
        user.followers +=1



user1=User(1,"Honda")
user2=User(2,"MUaaz")
user1.follow(user2)

print(user2.followers)