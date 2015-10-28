var express   =    require("express");
var HBase = require('hbase-client');
var app       =    express();

var client = HBase.create({
  zookeeperHosts: [
	'52.91.216.161:2181'
  ],
  zookeeperRoot: '/hbase-0.94.18',
});

function handle_database(req,res) {
	// Query parameters
	var userId=req.query.userid;
	var tweetTime=req.query.tweet_time;

	var tweetTime2 = tweetTime.substr(0, 10) + " " + tweetTime.substr(11,20)
	var filterList = new filters.FilterList({operator: filters.FilterList.Operator.MUST_PASS_ALL});

	filterList.addFilter(new filters.SingleColumnValueFilter('data', 'user_id', 'EQUAL', new filters.RegexStringComparator(userId)));
	filterList.addFilter(new filters.SingleColumnValueFilter('data', 'tweet_time', 'EQUAL', new filters.SubstringComparator(tweetTime2)));
	var scan = new Scan('scanner-row0');
	scan.setFilter(filterList);

	var message = "Team Entropy,846185807052\n";
	//Tweet ID1:Score1:TWEETTEXT1\n

	client.getScanner('tweets', scan, function (err, scanner) {
		var index = 0;
		var next = function (numberOfRows) {
			scanner.next(numberOfRows, function (err, rows) {
				// console.log(rows)
				rows.forEach(function (row) {
					var kvs = row.raw(); 
					for (var i = 0; i < kvs.length; i++) {
						var kv = kvs[i];
						var key = kv.toString();
						var value = kv.getValue().toString();
						console.log(key, value)
					}
				});

				next(numberOfRows);
			});
		};
		next(1);
	});
	
	res.send(message);
}

app.get("/q2",function(req,res){
	handle_database(req,res);
});

var server=app.listen(3000,function(){
	var host= server.address().address;
	var port=server.address().port;
	console.log('Server running on %s:%s',host,port);
});
