/// 
Class esh.csvpkey.Countries Extends %Persistent [ ClassType = persistent, DdlAllowed, Final, Owner = {irisowner}, ProcedureBlock, SqlRowIdPrivate, SqlTableName = Countries ]
{

Property Name As %Library.String(MAXLEN = 250) [ SqlColumnNumber = 2 ];

Property Code As %Library.String(MAXLEN = 250) [ SqlColumnNumber = 3 ];

Property Capital As %Library.String(MAXLEN = 250) [ SqlColumnNumber = 4 ];

Property Latitude As %Library.Currency [ SqlColumnNumber = 5 ];

Property Longitude As %Library.Currency [ SqlColumnNumber = 6 ];

Parameter USEEXTENTSET = 1;

Index COUNTRIESPKEY1 On Name [ IdKey, PrimaryKey, SqlName = COUNTRIES_PKEY1, Unique ];

Storage Default
{
<Data name="CountriesDefaultData">
<Value name="1">
<Value>Name</Value>
</Value>
<Value name="2">
<Value>Code</Value>
</Value>
<Value name="3">
<Value>Capital</Value>
</Value>
<Value name="4">
<Value>Latitude</Value>
</Value>
<Value name="5">
<Value>Longitude</Value>
</Value>
</Data>
<DataLocation>^E9fO.E5rp.1</DataLocation>
<DefaultData>CountriesDefaultData</DefaultData>
<ExtentLocation>^E9fO.E5rp</ExtentLocation>
<ExtentSize>249</ExtentSize>
<IdFunction>sequence</IdFunction>
<IdLocation>^E9fO.E5rp.1</IdLocation>
<Index name="COUNTRIESPKEY1">
<Location>^E9fO.E5rp.3</Location>
</Index>
<Index name="DDLBEIndex">
<Location>^E9fO.E5rp.2</Location>
</Index>
<Index name="IDKEY">
<Location>^E9fO.E5rp.1</Location>
</Index>
<IndexLocation>^E9fO.E5rp.I</IndexLocation>
<Property name="%%ID">
<AverageFieldSize>12.99</AverageFieldSize>
<Histogram>$lb(.06666666666666666667,0,0,$lb("Afghanistan","Bahrain","Bulgaria","Cook Islands","Eritrea","Gibraltar","Iceland","Kuwait","Mali","Namibia","Palestine, State of","Saint Helena, Ascension and Tristan da Cunha","Slovakia","Taiwan, Province of China","United Arab Emirates","Åland Islands"),$lb(0,1,0,0,0,0,0,0,0,0,0,1,0,0,0),$lb(1097230184,1097230184,1113679986,1634234977,1970038625,1114991719,1131376491,1131376491,1165126004,1165126004,1198088818,1198088818,1231250796,1231250796,1265989473,1265989473,1298230377,1298230377,1315007849,1315007849,1348562021,1348562021,1398892910,1634299508,1819244129,1399615350,1415670135,1415670135,1433299316,1433299316,3312214382,3312214382))</Histogram>
<Selectivity>1</Selectivity>
</Property>
<Property name="Capital">
<AverageFieldSize>9.76</AverageFieldSize>
<Histogram>$lb(.06666666666666666667,0,0,$lb(" "," AMSTERDAM"," BASSE-TERRE"," BUDAPEST"," DILI"," GITEGA"," KAMPALA"," LOMÉ"," MARIGOT"," NEW DELHI"," PAPEETE"," QUITO"," SAN JUAN"," TAIPEI"," VALLETTA"," ZAGREB"),$lb(1,1,2,1,1,1,1,1,1,1,1,1,1,1,1),$lb(536870912,0,1095586644,1095586644,1111577427,1095979845,1430536528,1112884289,1145654345,1145654345,1195988037,1195988037,1262570832,1262570832,1280265673,1280265673,1296126537,1296126537,1313167136,1313167136,1346457669,1346457669,1364543828,1364543828,1396788768,1396788768,1413564752,1413564752,1447119948,1447119948,1514227538,542785863))</Histogram>
<OutlierSelectivity>.032129:</OutlierSelectivity>
<Selectivity>0.4033%</Selectivity>
</Property>
<Property name="Code">
<AverageFieldSize>3.99</AverageFieldSize>
<Histogram>$lb(.06666666666666666667,0,0,$lb(" "," AZ"," BT"," CR"," ER"," GL"," ID"," KI"," LV"," MS"," NR"," PW"," SJ"," TG"," US"," ZW"),$lb(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),$lb(536870912,0,1096417280,1096417280,1112801280,1112801280,1129447424,1129447424,1163001856,1163001856,1196163072,1196163072,1229193216,1229193216,1263075328,1263075328,1280704512,1280704512,1297285120,1297285120,1313996800,1313996800,1347878912,1347878912,1397358592,1397358592,1413939200,1413939200,1431502848,1431502848,1515651072,542791424))</Histogram>
<Selectivity>0.4016%</Selectivity>
</Property>
<Property name="Latitude">
<AverageFieldSize>5.75</AverageFieldSize>
<Histogram>$lb(.06666666666666666667,1,1,$lb(-10000000000000000000,-26.3054,-17.5516,-8.5243,3.139,6.9271,12.1464,14.7167,18.0731,23.8103,32.2942,37.9601,41.9973,47.141,52.52,78.2232),$lb(1,1,1,0,0,0,1,1,0,0,1,0,1,0,0),"")</Histogram>
<OutlierSelectivity>.032129:</OutlierSelectivity>
<Selectivity>0.4050%</Selectivity>
</Property>
<Property name="Longitude">
<AverageFieldSize>5.79</AverageFieldSize>
<Histogram>$lb(.06666666666666666667,1,1,$lb(-10000000000000000000,-99.1332,-74.0721,-62.8508,-56.1645,-6.8417,2.6283,12.4964,18.3564,26.1025,33.3823,44.4991,58.4059,101.6869,126.978,179.1942),$lb(1,1,1,1,1,0,0,1,0,0,0,0,0,1,1),"")</Histogram>
<OutlierSelectivity>.032129:</OutlierSelectivity>
<Selectivity>0.4050%</Selectivity>
</Property>
<Property name="Name">
<AverageFieldSize>12.99</AverageFieldSize>
<Selectivity>1</Selectivity>
</Property>
<SQLMap name="COUNTRIES_PKEY1">
<BlockCount>-8</BlockCount>
</SQLMap>
<StreamLocation>^E9fO.E5rp.S</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
