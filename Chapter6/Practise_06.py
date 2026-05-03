post = input("Enter this post:")

# if("Harry" in post):
#     print("This post is talking about Harry")
# else:
#     print("This post is not talking about harry")



# Enter this post:Harry is good 
# This post is talking about Harry

# Enter this post:harry is good
# This post is not talking about harry

if("Harry".lower() in post.lower()):
    print("This post is talking about Harry")
else:
    print("This post is not talking about harry")



# Enter this post:shlip is good
# This post is not talking about harry

# Enter this post:harry is bad
# This post is talking about Harry