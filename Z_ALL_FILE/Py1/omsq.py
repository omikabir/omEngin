import pandas as pd
import cx_Oracle, pyodbc, requests, os, time
from mysql import *
from sqlalchemy import create_engine
import omsql.omsqlfn as fn
import omsql.InsUpd as fni
from datetime import *

def sql_between_days(d1 = None, d2 = None):
    print("d1 set to today and d2 set to yesterday")
    nw = datetime.now()
    thisdy = ''
    sincedy = ''
    if d1 == None:
        thisdy = nw.strftime("%Y%m%d")
    else:
        thisdy = d1
    if d2 == None:
        sincedy = ''
    else:
        sincedy = ''
    
def tm():
    nw = datetime.now()
    thistm = nw.strftime("%Y%m%d_%H%M%S")
    return thistm

def wrt2txt(flpath, content):
    try:
        f = open(flpath, 'a+')
        f.write(content)
        f.close()
        print('print from wrt2txt, *success*', flpath, chr(10))
    except:
        lastslash = flpath.rfind('\\')
        flname = flpath[-lastslash :len(flpath)-4]
        print(flname)
        os.system("taskkill /F /FI '"+ flname + "' /T")
        time.sleep(2)
        try:
            f = open(flpath, 'a+')
            f.write(content)
            f.close()
            print('print from wrt2txt, *success*', flpath, chr(10))
        except:
            print('def wrt2txt *failed* ', flpath, chr(10))

def save_cmd(content):
    nw = datetime.now()
    thisdy = nw.strftime("%Y%m%d")
    thistm = nw.strftime("%Y%m%d_%H%M%S")
    fl = os.getcwd() + '\\' + thisdy + '.txt'
    cont = ''
    try:
        if content == None:
            cont = "class initiated - " + thistm + chr(10)
            wrt2txt(fl, cont)
        elif content == '':
            pass
        else:
            cont = content + ' - ' + thistm + chr(10)
            wrt2txt(fl, cont)
    except:
        print('failed to def save_cmd')

def SaveToCsv(df, content = None, path_with_filename = None):
    pth = ''
    if path_with_filename == None:
        pth = os.getcwd() + '\\' + tm() + '.csv'
    else:
        pth = path_with_filename
    if content == None:
        try:
            df.to_csv(pth, index = False)
            print("save 'df' successfully: ", pth)
        except:
            print('could not saved to path : ', pth)
    else:
        try:
            content.to_csv(pth, index = False)
            print("save 'content' successfully: ", pth)
        except:
            print('could not saved to path : ', pth)

def SaveToText(self, content, path_with_filename = None):
    if path_with_filename == None:
        pth = os.getcwd() + '\\' + tm() + '.txt'
    else:
        pth = path_with_filename
    try:
        wrt2txt(pth, content)
    except:
        print('failed to write in text')

def mod_cols_name(df):
    cols = df.columns.to_list()
    sqlkey = ['ADD','ALTER','ALL','AND','ANY',
              'AS','ASC','BETWEEN','CASE','CHECK','COLUMN','CONSTRAINT',
              'CREATE','DATABASE','DEFAULT','DELETE','DESC','DISTINCT','DROP','EXEC','EXISTS','FROM',
              'HAVING','IN','INDEX','JOIN','LIKE','LIMIT','NOT','OR','PROCEDURE',
              'ROWNUM','SELECT','SET','TABLE','TOP','UNION','UNIQUE','UPDATE','VALUES','VIEW','WHERE']
    for i in range(len(cols)):
        st = cols[i]
        stmod = st.replace(' ','_')
        for n in sqlkey:
            if stmod == n:
                xx = '_' + stmod
                stmod = xx
        if st != stmod:
            df = df.rename(columns = {st:stmod})
    return df

##### Class Starts #########

class omsql:
    def __init__(self, User, Password, Host = False, Db = False):
        self.db = Db
        self.user = User
        self.password = Password
        self.host = Host
        self.conn = ''
        self.cur = ''
        self.tabledetails = {}
        self.df = pd.DataFrame([''])
        self.server = ''
        self.cmd = None
        self.TS()

    def TS(self, arg = False):
        if arg:
            self.cmd = arg
            save_cmd(self.cmd)
        else:
            save_cmd(self.cmd)
            self.cmd = ''

    def col_and_type(self, table):
        qry = 'EXPLAIN ' + self.db + '.' + table
        try:
            dfx = pd.read_sql(qry, con= self.engine)
            cols = dfx['Field'].to_list()
            typ = dfx['Type'].to_list()
            zips = zip(cols, typ)
            self.tabledetails = dict(zips)
            return self.tabledetails
        except:
            return "table not exist"

    def MySql(self):
        constr = 'mysql+mysqlconnector://' + self.user + ':' + self.password + '@' + self.host + '/' + self.db
        self.TS(constr)
        try:
            engine = create_engine(constr, echo=False)
            self.conn = engine.raw_connection()
            self.cur = self.conn.cursor()
            self.server = 'mysql'
            print('mysql conn successful')
        except:
            print('mysql conn failed')
    def MsSql(self):
        cstr = "Driver={SQL Server};SERVER=" + self.host + ";DATABASE=" + self.db + ";UID=" + self.user + ";PWD=" + self.password
        self.TS(cstr)
        try:
            self.conn = pyodbc.connect(cstr)
            self.cur = self.conn.cursor()
            self.server = 'mssql'
            print('mssql conn success')
        except:
            print('mssql conn failed')
    def Oracle(self):
        oHost = 'ossam-cluster-scan.robi.com.bd:1721/RBPB.robi.com.bd'
        self.db = 'SEMDB'
        self.conn = cx_Oracle.connect(self.user, self.password, oHost)
        self.server = 'oracle'
        print(self.conn.version)

    def is_table_exist(self, tbl):
        qry = "SELECT TOP 3 * FROM " + tbl
        try:
            rs = self.cur.execute(qry)
            print('table exist')
            return 1
        except:
            print('table does not exist')
            return 0
    
    def CheckExist(self, tbl, colname, values, args_qry = None):
        qry = ''
        msg = ''
        rw = 0
        if args_qry == None:
            qry = "select * from " + tbl + " where " + colname + "='" + values + "'"
        else:
            qry = "select * from " + tbl + " where " + args_qry + ' and ' + colname + "='" + values + "'"
        self.cmd = qry
        self.TS()
        try:
            self.df = pd.read_sql(qry, self.conn)
            rw = self.df.shape[0]
            msg = 'execution success'
        except:
            rw = 'NA'
            msg = 'execution Failed'
        print(qry,' ',  msg,' ', rw)
        return rw

    def Ex(self, arg, return_type = 'dataframe'):
        self.TS(arg)
        if return_type == 'dataframe':
            print('return datatype will be dataframe')
            try:
                rs = pd.read_sql(arg, con = self.conn)
                return rs
            except:
                print('execution failed, need to check query string')
        elif return_type == 'fetchone' or return_type == 'row':
            print('return datatype will be rows object')
            try:
                rs = self.cur.execute(arg)
                return rs
            except:
                print('execution failed, need to check query string')

    def Getdf(self):
        return self.df
    
    def setdf(self, ndf):
        self.df = ndf
        print('dataframe set to self.df')

    def CreateTable(self, tablename, list_col, list_type = None):
        servername = self.server
        print('list_col = list of columns, servername can be = mysql/mssql')
        st = ""
        finalstr = ''
        x = ""
        if servername.lower() == 'mssql':
            for i in range(len(list_col)):
                if list_type != None:
                    x = list_col[i] + "' " + list_type[i]
                else:
                    x = list_col[i] + "' TEXT NULL"
                if st == "":
                    addsl = " SL INT PRIMARY KEY IDENTITY (1, 1), "
                    st = "CREATE TABLE '" + tablename + "'(" + addsl + "'" + x
                    #st = "CREATE TABLE '" + tablename + "' ( '" + x
                else:
                    st = st + ', ' +  "'" + x
            else:
                finalstr = st + ' )'
                print(finalstr)
                self.cur.execute(finalstr)
                self.conn.commit()
                time.sleep(1)
                print('table created succssfully with cmd', finalstr)
                x = self.col_and_type(tablename)
        elif servername.lower() == 'mysql':
            for i in range(len(list_col)):
                if list_type != None:
                    x = list_col[i] + "` " + list_type[i]
                else:
                    x = list_col[i] + "` TEXT NULL"
                if st == "":
                    addID = "SL INT AUTO_INCREMENT PRIMARY KEY, "
                    st = "CREATE TABLE IF NOT EXISTS `" + tablename + "` ( " + addID + "`" + x
                    #st = "CREATE TABLE IF NOT EXISTS `" + tablename + "` ( `" + x
                else:
                    st = st + ', ' +  "`" + x
            else:
                finalstr = st + ' ) ENGINE=InnoDB'
                print(finalstr)
                self.cur.execute(finalstr)
                self.conn.commit()
                time.sleep(1)
                x = self.col_and_type(tablename)
                print('table created succssfully with cmd', finalstr)

    def Upd_or_Insert(self, tbl, ndf, bycols = False):
        if bycols:
            fni.InsertUpdate(self.db, tbl, self.conn, ndf, bycols)
        else:
            fni.InsertUpdate(self.db, tbl, self.conn, ndf)

    def InsertSingle(self, tbl, colname, values):
        self.cmd = "insert into " + tbl + ' ' + fn.prep_insert(colname,values)
        print('qry string from insert: ', self.cmd)
        try:
            self.cur.execute(self.cmd)
            self.conn.commit()
            print('insert success')
        except:
            print('error')

    def InsertBulk(self, tbl, dataframe , cols = []):
        if len(cols) == 0:
            self.Upd_or_Insert(tbl, dataframe)
        else:
            if isinstance(cols, list):
                xdf = dataframe[cols]
                self.Upd_or_Insert(tbl, xdf)

    def UpdateSingle(self, tbl, listcols, listvalue, bycol, bycolv):
        self.cmd = ''
        x = self.CheckExist(tbl, bycol, bycolv)
        if x != 0 :
            self.cmd = "update " + tbl + ' set ' + fn.prep_update(listcols,listvalue) + ' where ' + bycol + "='" + bycolv + "'"
            TS()
            print('Existing rows found, proceed for insert', self.cmd)
        else:
            self.cmd = "update " + tbl + ' set ' + fn.prep_insert(listcols,listvalue)
            print('no existing value found, proceed for inserting \n', self.cmd)
        self.cur.execute(self.cmd)
        self.conn.commit()
      
    def UpdateBulk(self, tbl, bycond_colname, ndf = False, oncols = False):
        if ndf == False:
            ndf = self.df
        if oncols:
            try:
                xdf = ndf[oncols]
                ndf = xdf
                self.Upd_or_Insert(tbl, ndf, bycond_colname)
            except:
                print('def UpdateBulk- oncols mustbe list by u provide ', type(oncols))
                print('update execution halted')

    def Query(self, tbl, colname = False, condition = False):
        qry = "select * from " + tbl
        if colname != False:
            cname = str(colname)
            if condition == False:
                qry = "select " + cname + " from " + tbl
            else:
                cond = str(condition)
                qry = "select " + cname + " from " + tbl + " where " + cond
        print('query: ', qry)
        try:
            dfx = pd.read_sql(qry, con= self.engine)
        except:
            self.cur.execute(qry)
            dfx = pd.DataFrame(self.cur.fetchall())
        self.df = dfx

    def DeleteByCond(self, tbl, col, cond):
        xx = "DELETE FROM " + tbl + " WHERE " + col + " Like '" + cond + "'"
        print(xx)
        self.cur.execute(xx)
        self.conn.commit()

    def DeleteDuplicate(self, tbl, cond_col):
        qry = "delete t1 FROM " + tbl + " t1 INNER JOIN "+ tbl + " t2 where t1.SL < t2.SL and t1." + cond_col + " = t2." + cond_col
        print(qry)
        self.cur.execute(qry)
        self.conn.commit()

    def csv2sql(self, csvfile, tblname, table_cols = 'csvhead', table_dtype = 'TEXT', by_cond_cols = False):
        if isinstance(csvfile, str):
            ndf = pd.read_csv(csvfile)
            self.df = ndf.apply(lambda x: x.str.replace("'",''))
        else:
            ndf = csvfile
            self.df = ndf.apply(lambda x: x.str.replace("'",''))
        xx = self.is_table_exist(tblname)
        if xx == 0:
            xdf = mod_cols_name(self.df)
            self.df = xdf
            if table_cols == 'csvhead' or table_cols == 'dataframe_head':
                cols = self.df.columns.to_list()
            else:
                cols = table_cols
            try:
                if isinstance(table_dtype, str):
                    self.CreateTable(tblname,cols,None)
                elif isinstance(table_dtype, list) and len(table_dtype) == len(cols):
                    self.CreateTable(tblname,cols,table_dtype)
                else:
                    print('table cols and table_dtype field not same')
                    exit()
            except:
                print(self.tabledetails)
        if by_cond_cols:
            self.Upd_or_Insert(tblname,self.df, by_cond_cols)
        else:
            self.Upd_or_Insert(tblname,self.df)

    def df2sql(self, tblname, ndf, table_cols = 'dataframe_head', table_dtype = 'TEXT', by_cond_cols = False):
        if by_cond_cols:
            self.csv2sql(ndf, tblname, table_cols, table_dtype, by_cond_cols)
        else:
            self.csv2sql(ndf, tblname, table_cols, table_dtype)




