import facebook

access_token = "<Your Access ID>"
fb = facebook.GraphAPI(access_token)


class facebook:
    def post_on_wall(self, message):
        fb.put_object("me", "feed", message=message)
