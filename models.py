from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Group(Base):
    __tablename__ = 'Table_Group'
    ID_Group = Column('ID_Group', String(60), primary_key=True)
    Size = Column('Size', Integer())
    Open = Column('Open', Boolean())
    Treatment = Column('Treatment', String(10))
    BuildingTime = Column('BuildingTime', Integer())
    Status = Column('Status', String())

    def __repr__(self):
        return "<Group(ID_Group='%s', Size=%s, Open=%s, Treatment='%s' BuildingTime=%s, Status='%s')>" % (
                self.ID_Group, self.Size, self.Open, self.Treatment, self.BuildingTime, self.Status)

class Player(Base):
    __tablename__ = 'Table_Player'
    ID_Player = Column('ID_Player', String(60), primary_key=True)
    Sex = Column('Sex', String(10))
    Age = Column('Age', Integer())
    ID_Number = Column('ID_Number', Integer())
    Status_Start = Column('Status_Start', Boolean())
    Status_End = Column('Status_End', Boolean())
    ID_Call = Column('ID_Call', Integer())
    Gain = Column('Gain', Integer())
    Score = Column('Score', Integer())
    BestTotem = Column('BestTotem', Integer())
    Knowledge = Column('Knowledge', Integer())
    Ancestor = Column('Ancestor', Integer())
    ID_Group = Column('ID_Group', ForeignKey('Table_Group.ID_Group'))

class Totem(Base):
    __tablename__ = 'Table_Totem'
    Key_Totem = Column('Key_Totem', Integer(), primary_key=True)
    Totem1 = Column('Totem1', Integer())
    Totem2 = Column('Totem2', Integer())
    Totem3 = Column('Totem3', Integer())
    ScoreTotem = Column('ScoreTotem', Integer())
    TotemTime = Column('TotemTime', Integer())
    ID_Player = Column('ID_Player', ForeignKey('Table_Player.ID_Player'))
