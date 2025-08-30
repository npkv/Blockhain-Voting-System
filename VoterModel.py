import pyodbc
import Constants
class VoterModel:
    def __init__(self, voteID, title="", firstName="", middleName="", lastName="", wardNumber="", streetName="", area="", city="", district="", state="", dob=None, addressProof="", ageProof="", constituencyID=0, constituencyModel = None, isApproved=0, ssn="", mobileNbr="", emailID="", password="", gender=""):
        self.voteID = voteID
        self.title = title
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.wardNumber = wardNumber
        self.streetName = streetName
        self.area = area
        self.city = city
        self.district = district
        self.state = state
        self.dob = dob
        self.addressProof = addressProof
        self.ageProof = ageProof
        self.constituencyID = constituencyID
        self.constituencyModel = constituencyModel
        self.isApproved = isApproved
        self.ssn = ssn
        self.mobileNbr = mobileNbr
        self.emailID = emailID
        self.password = password
        self.gender=gender
    
    @staticmethod
    def getVoterByID(rid):
        conn3 = pyodbc.connect(Constants.connString, autocommit=True)
        cur3 = conn3.cursor()
        
        sqlcmd = "SELECT voteID, firstName FROM VoterMaster WHERE voteID = '"+str(rid)+"'"
        print("DDDDDDDDDDDDDDDDDDDDD", sqlcmd)
        cur3.execute(sqlcmd)
        row = cur3.fetchone()
        voterModel = None
        if row:
            voterModel = VoterModel(row[0], firstName=row[1])
        return voterModel
    
    
    @staticmethod
    def getVoterByEmailID(emailID):
        conn3 = pyodbc.connect(Constants.connString, autocommit=True)
        cur3 = conn3.cursor()
        
        sqlcmd = "SELECT voteID, firstName FROM VoterMaster WHERE emailID = '"+str(emailID)+"'"
        print("DDDDDDDDDDDDDDDDDDDDD", sqlcmd)
        cur3.execute(sqlcmd)
        row = cur3.fetchone()
        voterModel = None
        if row:
            voterModel = VoterModel(row[0], firstName=row[1])
        return voterModel


