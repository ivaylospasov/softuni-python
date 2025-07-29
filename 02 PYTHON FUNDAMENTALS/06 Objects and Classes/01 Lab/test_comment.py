from comment import Comment

# Test with all parameters
comment1 = Comment("user1", "This is a comment", 5)
print(f"Comment 1: username={comment1.username}, content={comment1.content}, likes={comment1.likes}")

# Test with default likes parameter
comment2 = Comment("user2", "Another comment")
print(f"Comment 2: username={comment2.username}, content={comment2.content}, likes={comment2.likes}")

# Test with different values
comment3 = Comment("john_doe", "Great post!", 10)
print(f"Comment 3: username={comment3.username}, content={comment3.content}, likes={comment3.likes}")