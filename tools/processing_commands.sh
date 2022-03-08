
#Removing the first header line from all data files
sed -i 1d *.csv

#Removing the first column (_id) from all data files
for f in ./data/* ; do 
cut --complement -f 1 -d, $f > temp && mv temp $f
done

#Adding data from csv to neo4j
neo4j-admin import --database=neo4j --nodes=Address=nodes.csv --relationships=TRANSFERED_TO=header.csv,data/2017-10.csv,data/2017-11.csv,data/2017-12.csv,data/2017-6.csv,data/2017-7.csv,data/2017-8.csv,data/2017-9.csv,data/2018-10.csv,data/2018-11.csv,data/2018-12.csv,data/2018-1.csv,data/2018-2.csv,data/2018-3.csv,data/2018-4.csv,data/2018-5.csv,data/2018-6.csv,data/2018-7.csv,data/2018-8.csv,data/2018-9.csv,data/2019-10.csv,data/2019-11.csv,data/2019-12.csv,data/2019-1.csv,data/2019-2.csv,data/2019-3.csv,data/2019-4.csv,data/2019-5.csv,data/2019-6.csv,data/2019-7.csv,data/2019-8.csv,data/2019-9.csv,data/2020-10.csv,data/2020-11.csv,data/2020-12.csv,data/2020-1.csv,data/2020-2.csv,data/2020-3.csv,data/2020-4.csv,data/2020-5.csv,data/2020-6.csv,data/2020-7.csv,data/2020-8.csv,data/2020-9.csv,data/2021-10.csv,data/2021-11.csv,data/2021-12.csv,data/2021-1.csv,data/2021-2.csv,data/2021-3.csv,data/2021-4.csv,data/2021-5.csv,data/2021-6.csv,data/2021-7.csv,data/2021-8.csv,data/2021-9.csv,data/2022-1.csv,data/2022-2.csv
