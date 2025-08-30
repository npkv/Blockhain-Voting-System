class VoteDataModel:
    def __init__(self, voteID, politicalPartyID=0, userID=0, idToUpload="", isBlockChainGenerated=0, hash="", prevHash="", PoliticalParty=None, User=None):
        self.voteID = voteID
        self.politicalPartyID = politicalPartyID
        self.userID = userID
        self.idToUpload = idToUpload
        self.isBlockChainGenerated = isBlockChainGenerated
        self.hash = hash
        self.prevHash = prevHash
        self.PoliticalParty = PoliticalParty
        self.User = User
