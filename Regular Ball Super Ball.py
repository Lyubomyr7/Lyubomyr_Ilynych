class Ball(object):
    def __init__(self,ball_type="regular"):
        self.ball_type = ball_type
    def __str__(self):
        return "%s"% self.ball_type



b1=Ball().ball_type
b2=Ball("super").ball_type
print(b1)
print(b2)

