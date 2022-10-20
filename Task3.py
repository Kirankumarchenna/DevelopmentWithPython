from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

auth_provider = PlainTextAuthProvider("ocs_superuser", "password")
cluster = Cluster(['10.106.4.233'], auth_provider=auth_provider, control_connection_timeout=20.0)
session = cluster.connect()
ResultSet = session.execute("update smart.costedevent2_220319000 set data={apesdelta : [],billcostmny : NULL,"
                            "chargenumber : 1,clustersubid : 0,competitorcostmny : NULL,costcentreid : NULL,"
                            "discountdata : NULL,eventcostmny :0,eventlifecycletype : 0,externalcostmny : NULL,"
                            "flexibleattributes : ['321646982472079', '3313', '1', 'O', '', '', '3313', 'BEL', '', "
                            "'100082', '3PPS', '200082', '', '', '', 'CA-Yir1SKr5ZOjYfZMJ', '0', '200000000', '', "
                            "'F', '', '999999900000000', '999999700000000', 'T', 'BTL_SMS_MO-200000000C', 'Belgium', "
                            "'3313', 'Belgium', 'BTL_SMS_MO-200000000C', 'T', '3313', 'F', '1', '01646982472079', "
                            "'3313', '1', 'c8lfaflav5iehm3ti190;1646982472093;r1', '', '', '', '', '02:-B,B,B,"
                            "L68IA;D,D,BiKvYV,L68IA;C,E,BiKvYV,L68IA', 'F23f4rfr43fAVE', '2', '1', '0', "
                            "'32486000005', '2', '0', '', 'BA-Yir1SKr5ZOjYfZNx^1^1^321646982472079', '2', "
                            "'PREMIUM_MO', '', 'T', '200082', '-99', '-99', '0', '8', '1', 'TELENET', '', '', '', '', "
                            "'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', "
                            "'', '', '', '', '', '', '', '', '', '', ''],fragmentnumber : 1,highestprioritydiscid : "
                            "NULL,highestpriorityprodseq : 0,hosteventtypeid : NULL,importedcostmny : NULL,"
                            "importedcurrencycode : 'EUR',inhostcostedboo : NULL,internalcostmny : NULL,"
                            "logicallydeletedboo : NULL,loyaltypoints : NULL,managedfileid : 0,maskbillruleid : NULL,"
                            "maskstoreruleid : NULL,modifiedboo : false,originalaccountnum : NULL,originaleventseq : "
                            "NULL,postbillretentiondays : NULL,predisccostmny : NULL,preveventref : NULL,preveventseq "
                            ": NULL,primaryeventref : NULL,productseq : 2,ratingdiscusagetot : 0,receivableclassid : "
                            "1,revenuecodeid : 100082,rownum : 1,rulenumber : NULL,sourceref : "
                            "'QCM-RATED-EVENTS:1:0:12975:1646982930000',tariffid : 2081,taxoverrideid : 1,"
                            "transactionid : NULL,twineventboo : NULL,ustcategoryid : NULL,ustcodeid : NULL}where "
                            "accountnum='BA-Yir1SKr5ZOjYfZNx' and eventstoragegroup=0 and tenantid=0 and "
                            "eventseq=220319000 and eventsource='321646982472079' and eventtypeid=3 and "
                            "eventdtm='2022-03-11 08:11:18' and eventref='HC9AWbe+wc2ErhCG' ")

ResultSet1 = session.execute("select * from smart.costedevent2_220319000 where accountnum = 'BA-Yir1SKr5ZOjYfZNx' "
                             "allow filtering")
for Row in ResultSet1:
    print(Row[9])

