class UserModel:
    def __init__(self, userID=0, userName="", emailID="", password="", roleID=0, roleModel=None):
        self.userID = userID
        self.userName = userName
        self.emailID = emailID
        self.password = password
        
        self.roleID = roleID
        self.roleModel=roleModel
        
