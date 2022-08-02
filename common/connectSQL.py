import requests
import yaml
import pymssql
from common import loadYaml

load_yaml = loadYaml.loadYaml()
connectSQL = pymssql.connect(server=load_yaml['DB']['server'], user=load_yaml['DB']['user'], password=load_yaml['DB']['password'], database=load_yaml['DB']['database'])

def sqlConnectCount(sqlCommand):
    cursor = connectSQL.cursor()
    cursor.execute(sqlCommand)
    sqls = cursor.fetchall()
    sqlCountLen = len(sqls)
    return sqlCountLen

def sqlClose():
    connectSQL.close()

class searchDB:
    # 事件類別
    def eventCategory():
        sqlCount = sqlConnectCount('SELECT Id FROM EventTypes')
        return sqlCount
    # 設備事件
    def deviceEvent():
        sqlCount = sqlConnectCount('SELECT * FROM Events where HasDevice = 1 AND Category = 0 AND EventTypeId is not NULL')
        return sqlCount

    # 設備事件 篩選
    def deviceEventSearch():
        sqlCount = sqlConnectCount("SELECT * FROM Events where HasDevice = 1 AND Category = 0 AND Name LIKE  '%火%'")
        return sqlCount

    # 數值事件
    def valueEvent():
        sqlCount = sqlConnectCount('SELECT * FROM Events where Enable = 1 AND Category = 1')
        return sqlCount

    # 複合式事件
    def customMultipleEvent():
        sqlCount = sqlConnectCount('SELECT * FROM Events where Enable = 1 AND Category = 2')
        return sqlCount

    # 子系統資訊
    def subsystemInformation():
        sqlCount = sqlConnectCount('SELECT Id FROM Subsystems')
        return sqlCount


    # 設備資訊 只篩子系統
    def deviceInformationOnlySub():
        sqlCount = sqlConnectCount('select * from Devices where SubsystemId = 12')
        return sqlCount

    # 設備資訊 只篩設備類別
    def deviceInformationOnlyCategory():
        sqlCount = sqlConnectCount('select * from Devices where DeviceTypeId = 26')
        return sqlCount

    # 設備資訊 篩子系統 + 設備類別 + 關鍵字
    def deviceInformationAll():
        sqlCount = sqlConnectCount("select * from Devices where DeviceTypeId = 24 AND CustomName LIKE '%SC%'")
        return sqlCount

    # 運轉紀錄
    def booleanTime():
        sqlCount = sqlConnectCount('select * from BooleanTimes where Enable = 1')
        return sqlCount

    # 動作群組
    def actionGroup():
        sqlCount = sqlConnectCount('select * from ActionGroups where Enable = 1')
        return sqlCount

    # 連動設定
    def interaction():
        sqlCount = sqlConnectCount('select * from Interactions where Enable = 1')
        return sqlCount

    # 平面圖設定 圖層
    def mapFolder():
        sqlCount = sqlConnectCount('select * from MapFolders where ParentMapFolderId is NULL')
        return sqlCount

    # 平面圖設定 圖面
    def maps():
        sqlCount = sqlConnectCount('select * from Maps where Enable = 1')
        return sqlCount

    # 聯絡人
    def contactPerson():
        sqlCount = sqlConnectCount('select * from ContactPersons where Enable = 1')
        return sqlCount

    # 聯絡人群組
    def contactPersonGroup():
        sqlCount = sqlConnectCount('select * from ContactPersonGroups')
        return sqlCount

    # 設備事件通知
    def deviceEventNotify():
        sqlCount = sqlConnectCount('select * from Notifications where Enable = 1 and EventCategory = 0')
        return sqlCount

    # 數值事件通知
    def valueEventNotify():
        sqlCount = sqlConnectCount('select * from Notifications where Enable = 1 and EventCategory = 1')
        return sqlCount

    # 複合式事件通知
    def customMultipleEventNotify():
        sqlCount = sqlConnectCount('select * from Notifications where Enable = 1 and EventCategory = 2')
        return sqlCount

    # 連動時間排程
    def interactionSchedule():
        sqlCount = sqlConnectCount('select * from Schedules where Enable = 1')
        return sqlCount

    # 定期工作設定
    def regularWorkSet():
        sqlCount = sqlConnectCount('select * from RegularWorks where Enable = 1')
        return sqlCount
    # 國定假日
    def nationalHoliday():
        sqlCount = sqlConnectCount('select * from NationalHolidays')
        return sqlCount

    # 相關連結
    def relevantLink():
        sqlCount = sqlConnectCount('select * from OtherLinks')
        return sqlCount

    # 帳號管理
    def accountManage():
        sqlCount = sqlConnectCount('select * from AspNetUsers')
        return sqlCount