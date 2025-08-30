import pyodbc
import Constants
from ContestantModel import ContestantModel
from ElectionModel import ElectionModel

from PoliticalPartyModel import PoliticalPartyModel
from ConstituencyModel import ConstituencyModel
from VoterModel import VoterModel
class VoterCastModel:
    def __init__(self, uniqueID=0, contestantID=0, contestantModel = None, voterID = 0, voterModel=None, electionID=0, electionModel=None,  constituencyID=0, constituencyModel=None, isBlockChainGenerated=0, hash="", prevHash=""):
        self.uniqueID = uniqueID
        self.contestantID = contestantID
        self.contestantModel = contestantModel
        self.voterID = voterID
        self.voterModel = voterModel
        self.electionID = electionID
        self.electionModel = electionModel
        self.constituencyID = constituencyID
        self.constituencyModel = constituencyModel
        self.isBlockChainGenerated = isBlockChainGenerated
        self.hash = hash
        self.prevHash = prevHash
         
    @staticmethod
    def getAllVoterCast():
        conn3 = pyodbc.connect(Constants.connString, autocommit=True)
        cur3 = conn3.cursor()
        
        sqlcmd = "SELECT * FROM VoteCastDetails ORDER BY uniqueID"
        print(sqlcmd)
        cur3.execute(sqlcmd)
        
        voterCastList = []
        while True:
            row = cur3.fetchone()
            if row:
                contestantObject = ContestantModel.getContestantNameByID(row[1])
                voterObject = VoterModel.getVoterByID(row[2])
                electionObject = ElectionModel.getElectionNameByID(row[3])
                constituencyObject = ConstituencyModel.getConstituencyNameByID(row[4])
                
                voterCastModel = VoterCastModel(row[0], contestantID = row[1], contestantModel= contestantObject, voterID=row[2], voterModel=voterObject, electionID=row[1], electionModel=electionObject,  constituencyID = row[4], constituencyModel=constituencyObject, hash=row[6],prevHash=row[7])
                print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",voterCastModel.contestantModel.firstName)
                voterCastList.append(voterCastModel)
            else:
                break
        return voterCastList  
    
    
    @staticmethod
    def getAllContestantByElectionByConstituency(electionID, constituencyID):
        conn3 = pyodbc.connect(Constants.connString, autocommit=True)
        cur3 = conn3.cursor()
        
        sqlcmd = "SELECT ContestantMaster.contestantID, firstName FROM ContestantMaster INNER JOIN ContestantElectionDetails ON ContestantElectionDetails.contestantID = ContestantMaster.contestantID WHERE  ContestantElectionDetails.electionID = '"+str(electionID)+"' AND ContestantElectionDetails.constituencyID = '"+str(constituencyID)+"'"
        print(sqlcmd)
        cur3.execute(sqlcmd)
        
        contestantsList = []
        while True:
            row = cur3.fetchone()
            if not row:
                break
            contestantModel = ContestantModel(row[0], firstName=row[1])
            contestantsList.append(contestantModel)
        return contestantsList   