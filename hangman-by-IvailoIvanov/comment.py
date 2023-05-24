class Comment:
    def __init__(self,username,content,like=0):
        self.username = username
        self.content = content
        self.likes = like

comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
