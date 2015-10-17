var bigInt = require("big-integer");
var express  = require('express');
var app      = express();     
// var PythonShell = require('python-shell');

// https://github.com/extrabacon/python-shell
// Function for string formatting from http://stackoverflow.com/questions/610406/javascript-equivalent-to-printf-string-format                 

String.prototype.format = function() {
    var formatted = this;
    for( var arg in arguments ) {
        formatted = formatted.replace("{" + arg + "}", arguments[arg]);
    }
    return formatted;
};

app.get('/q1', function(req, res) {
    var message_key = req.query.key;
    var cipher = req.query.message;

   	var x = bigInt("8271997208960872478735181815578166723519929177896558845922250595511921395049126920528021164569045773");
   	var xy = bigInt(message_key);
   	var y = xy.divide(x);
   	var z_big = y.mod(25).add(1);
   	var z = z_big.valueOf();
	
	var size = Math.sqrt(cipher.length);

	var matrix = [];
	for(var i=0; i<size; i++) {
	    matrix[i] = [];
	    for(var j=0; j<size; j++) {
	        matrix[i][j] = cipher.charAt(i*size+j);
	    }
	}

	var inter = "";

	for(var i = 0; i < size; i++) {
		var a = i;
		var b = 0;
		while(true) {
			inter+=matrix[b][a];
			if( a == 0) 
				break;
			else {
				a-=1;
				b+=1;
			}
		}
	}

	for(var i = 1; i < size; i++) {
		var a = (size-1);
		var b = i;
		while(true) {
			inter+=matrix[b][a];
			if(b == (size-1)) 
				break;
			else {
				a-=1;
				b+=1;
			}
		}
	}

	var shift = (26-z)%26;
	var result = "";
	for (var i = 0; i < inter.length; i++) {
		var c = inter.charCodeAt(i);
		result += String.fromCharCode((c - 65 + shift) % 26 + 65); // Uppercase
	}

    var dated = new Date();
    dated.setUTCHours(dated.getUTCHours() - 4);
    var datetime = dated.getUTCFullYear() + "-" + (dated.getUTCMonth()+1)  + "-" 
                + dated.getUTCDate() + " " + dated.getUTCHours() + ":"  
                + dated.getUTCMinutes() + ":" + dated.getUTCSeconds();

    var message = "Team Entropy,846185807052\n{0}\n{1}\n".format(datetime, result);
    res.send(message);
});

var server = app.listen(80, function () {
    var host = server.address().address;
    var port = server.address().port;
    console.log('App listening at http://%s:%s', host, port);
});
