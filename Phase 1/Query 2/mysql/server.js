//GET /q2?userid=uid&tweet_time=timestamp
//Response format:
//
//TEAMID,TEAM_AWS_ACCOUNT_ID\n
//Tweet ID1:Score1:TWEETTEXT1\n
//Tweet ID2:Score2:TWEETTEXT2\n


var express   =    require("express");
var mysql     =    require('mysql');
var app       =    express();

var pool      =    mysql.createPool({
    connectionLimit : process.env.DB_CONNS, //number of simultaneous connections
    host     : process.env.DB_HOST,
    user     : process.env.DB_USER,
    password : process.env.DB_PASSWD,
    database : process.env.DB_NAME,
    debug    :  false
});
//http://stackoverflow.com/questions/646628/how-to-check-if-a-string-startswith-another-string
if (typeof String.prototype.startsWith != 'function') {
  String.prototype.startsWith = function (str){
    return this.slice(0, str.length) == str;
  };
}
if (typeof String.prototype.endsWith != 'function') {
  String.prototype.endsWith = function (str){
    return this.slice(-str.length) == str;
  };
}
// Function for string formatting from http://stackoverflow.com/questions/610406/javascript-equivalent-to-printf-string-format                 
String.prototype.format = function() {
    var formatted = this;
    for( var arg in arguments ) {
        formatted = formatted.replace("{" + arg + "}", arguments[arg]);
    }
    return formatted;
};
    
//prepare query result in format for q2
//this method appends a \n dont forget orignal as \t\n as line ending as well as extra quotes : ""orignal""\t\n
function handle_response(rows){
    var message = "Team Entropy,846185807052\n";
	rows.forEach(function(idx,row){
                console.log(row);
                var text=rows[row]['tweet_text'];
	text=text.substr(1,text.length-4);//check if text enclosed in extra "" strip if true
		message+="{0}:{1}:{2}\n".format(rows[row]['tweet_id'],rows[row]['tweet_score'],text);
	});
	console.log(message);
	return message;
}

//
function handle_database(req,res) {
    //get query parameters
	var userId=req.query.userid;
	var tweetTime=req.query.tweet_time;
	var queryString="select tweet_id,tweet_score,stringdecode(tweet_text) as tweet_text from twitter where user_id=? and tweet_time=?"
	var params=[];
	params.push(userId);
	params.push(tweetTime);
//       console.log(queryString+"-"+params);	
    
   pool.getConnection(function(err,connection){
        if (err) {
//          connection.release();
	  console.log(err);
          res.json({"status" : "Error,not connected to database"});
          return;
        }   
        connection.query(queryString,params,function(err,rows){
            connection.release();
            if(!err) {
                console.log(rows);
		var message=handle_response(rows);
		res.setHeader('content-type','text/plain')
		res.send(message);
            }else{ console.log(err)}
        });

        connection.on('error', function(err) {      
              res.json({"status":"Error occurred in database "});
              return;
        });
  });
}

app.get("/q2",function(req,res){
//	console.log(req);
        handle_database(req,res);
});

var server=app.listen(3000,function(){
    var host= server.address().address;
    var port=server.address().port;
    console.log('Server running on %s:%s',host,port);
});

