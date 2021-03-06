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

    def __repr__(self):
        return "<Player(ID_Player=%s, ID_Group='%s', Ancestor=%s, ID_Number=%s, Score=%s)>" % (
                self.ID_Player, self.ID_Group, self.Ancestor, self.ID_Number, self.Score)


class Totem(Base):
    __tablename__ = 'Table_Totem'
    Key_Totem = Column('Key_Totem', Integer(), primary_key=True)
    Totem1 = Column('Totem1', Integer())
    Totem2 = Column('Totem2', Integer())
    Totem3 = Column('Totem3', Integer())
    ScoreTotem = Column('ScoreTotem', Integer())
    TotemTime = Column('TotemTime', Integer())
    ID_Player = Column('ID_Player', ForeignKey('Table_Player.ID_Player'))

    def __repr__(self):
        return "<Totem(ID_Player=%s, ScoreTotem=%s, TotemTime=%s)>" % (
            self.ID_Player, self.ScoreTotem, self.TotemTime
        )


class Workshop(Base):
    __tablename__ = 'Table_Workshop'
    Key_Trial = Column('Key_Trial', Integer(), primary_key=True)
    WorkShop1 = Column('WorkShop1', Integer())
    WorkShop2 = Column('WorkShop2', Integer())
    WorkShop3 = Column('WorkShop3', Integer())
    WorkShop4 = Column('WorkShop4', Integer())
    WorkShopString = Column('WorkShopString', String(15))
    WorkShopResult = Column('WorkShopResult', Integer())
    Success = Column('Success', Boolean())
    Innov = Column('Innov', Boolean())
    TrialTime = Column('TrialTime', Integer())
    ID_Player = Column('ID_Player', ForeignKey('Table_Player.ID_Player'))

    def __repr__(self):
        return "<Workshop(ID_Player=%s, WorkShopString='%s', WorkShopResult='%s')>" % (
            self.ID_Player, self.WorkShopString, self.WorkShopResult
        )


class PlayerObs(Base):
    __tablename__ = 'Table_PlayerObs'
    ID_Obs = Column("ID_Obs", String(60), primary_key=True)
    RankObs = Column("RankObs", Integer())
    RankFocal = Column("RankFocal", Integer())
    StartTime = Column("StartTime", Integer())
    StopTime = Column("StopTime", Integer())
    ID_Player = Column("ID_Player", ForeignKey("Table_Player.ID_Player"))

    def __repr__(self):
        return "<PlayerObs(ID_Obs='%s', ID_Player=%s, RankObs=%s, RankFocal=%s, StartTime=%s, StopTime=%s)>" % (
            self.ID_Obs, self.ID_Player, self.RankObs, self.RankFocal, self.StartTime, self.StopTime
        )


class Drop(Base):
    __tablename__ = 'Table_Drop'
    Key_Drop = Column("Key_Drop", Integer(), primary_key=True)
    Item = Column("Item", Integer())
    DragStart = Column("DragStart", Integer())
    DragEnd = Column("DragEnd", Integer())
    DropTime = Column("DropTime", Integer())
    ID_Player = Column("ID_Player", ForeignKey("Table_Player.ID_Player"))

    def __repr__(self):
        return '<Drop(ID_Player=%s, Item=%s, DragStart=%s, DragEnd=%s, DropTime=%s)>' % (
            self.ID_Player, self.Item, self.DragStart, self.DragEnd, self.DropTime
        )


class WorkShopObs(Base):
    __tablename__ = 'Table_WorkShopObs'
    Key_Tool = Column("Key_Tool", Integer(), primary_key=True)
    ID_Obs_WS = Column("ID_Obs_WS", String(60))
    ToolObs = Column("ToolObs", String(60))
    ToolTime = Column("ToolTime", Integer())
    ID_Player = Column("ID_Player", ForeignKey("Table_Player.ID_Player"))

    def __repr__(self):
        return "<WorkShopObs(ID_Player=%s, ID_Obs_WS='%s', ToolObs='%s')>" % (
            self.ID_Player, self.ID_Obs_WS, self.ToolObs
        )
