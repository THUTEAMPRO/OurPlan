var myTable = new Object();
function DateClass(_container) {
        this.container = _container;
        this.weekArr = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        this.dateArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        this.monthArr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
        
        this.tableRowText = '<tr height=80 valign="top">';

        
        this.showWeekTable = function(_year, _month, _date, _day) {
             this.container.innerHTML = this.getWeekTable(_year, _month,_date,_day);
            week_bind_task();
        }

        this.getWeekTable = function(_year, _month,_date,_day) {	
        	var ymd = this.checkDate(_year, _month, _date).split('-');
                 _year = parseInt(ymd[0]);
                 _month = parseInt(ymd[1]);
                 _date = parseInt(ymd[2]);
                 
            
    
                 today_year = new Date().getFullYear();
                 today_month = new Date().getMonth() ;
                 today_date = new Date().getDate();
                 today_day = new Date().getDay();
                 
                 this.Thead = '  <input type="button" value="today" onclick="myTable.showWeekTable(' +today_year+ ',' +today_month+ ',' +today_date+ ',' +today_day+ '); "/>';
                 this.Thead += '  <input type="button" value="prev w" onclick="myTable.showWeekTable(' + _year + ', ' +_month+ ',' +eval(_date - 7)+ ',' +_day+ '); "/>';
                 this.Thead +=this.monthArr[_month] + ' ' + _date+ ', '+ _year + ' '+this.weekArr[+_day];
                 this.Thead += '  <input type="button" value="next w" onclick="myTable.showWeekTable(' + _year + ',' +_month+ ',' +eval(_date + 7)+',' +_day+ '); "/>';
                 
                 this.Thead += '  <input type="button" value="month view" align="right" onclick="myTable.showMonthTable(' + _year + ','+_month+','+_date+','+_day+'); "/>';
                 
                 this.Thead += '<br><table  cellspacing="0" >\n';
                 this.Thead += '<col width="60">\n'; // time colonm
                 for (var i = 0; i < 7; i++)
                 	this.Thead += '<col width="200">\n';
                 	
                 this.Thead += '<tr>';
                 this.dateArr[1] = (!this.checkYear(_year)) ? 28 : 29 ;
       
       		 this.Thead += '<th align="center" class="WeekTd"> time </th>';
                 first_date_of_week = _date - _day;
                 
                 for (var i=0; i<this.weekArr.length; i++)  {
                 	this.Thead += '<th class="WeekTd" align="center" >' + this.weekArr[i] + ' ';
                 	this.Thead +=  eval(1 + parseInt(this.checkDate(_year, _month, eval(first_date_of_week+i), i).split('-')[1])) + '/' + parseInt(this.checkDate(_year, _month, eval(first_date_of_week+i), i).split('-')[2]) + '</th>'
                 }
                 this.Thead += '</tr>\n';
        
        	this.Tbody = ' ';
        	 for (var i = 0; i < 24; i++) {
        	 	this.Tbody += '<tr> <td align="right" class="WeekTd">'+i+':00</td>'
                 var data_hour=i;
        	 	for (var j = 0; j < this.weekArr.length; j++) {
                    var data_date=this.checkDate(_year, _month+1, eval(first_date_of_week+j), j);
                    var newDiv='<div class="task" data-hour='+data_hour+' data-date='+data_date+'></div>';
        	 		this.Tbody += '<td class="out">'+newDiv+'</td>'
        	 	}
        	 	this.Tbody += '</tr>';
        	 }
                 this.TFoot = '</table>\n';
                 
                 this.Table = this.Thead + this.Tbody + this.TFoot;
                 return this.Table;
         }


	this.showMonthTable = function(_year, _month,_date,_day) {
             this.container.innerHTML = this.getMonthTable(_year, _month,_date,_day);
        month_bind_task();
             
        }

        this.getMonthTable = function(_year, _month,_date,_day) {	
                 var ymd = this.checkMonth(_year, _month).split('-');
                 _year = parseInt(ymd[0]);
                 _month = parseInt(ymd[1]);
                 
                 today_year = new Date().getFullYear();
                 today_month = new Date().getMonth();
                 
                 this.Thead = '  <input type="button" value="today" onclick="myTable.showMonthTable(' +today_year+ ', ' + today_month+ ',' +_date+',' +_day+'); "/>';
                 this.Thead += '  <input type="button" value="prev m" onclick="myTable.showMonthTable(' + _year + ', ' + eval(_month-1) + ',' +_date+',' +_day+'); "/>';
                 this.Thead += this.monthArr[_month] + ' '+ _year;
                 this.Thead += '  <input type="button" value="next m" onclick="myTable.showMonthTable(' + _year + ', ' + eval(_month+1) + ',' +_date+',' +_day+'); "/>';
                 
                 this.Thead += '  <input type="button" value="week view" align="right" onclick="myTable.showWeekTable(' + _year + ',' +_month+ ',' +_date+',' +_day+ '); "/>';
                 
                 this.Thead += '<br><table  cellspacing="0" >\n';
                 for (var i = 0; i < 7; i++)
                 	this.Thead += '<col width="200">\n';
                 this.Thead += '<tr>';
                 for (var i=0; i<this.weekArr.length; i++) 
                 	this.Thead += '<th align="center" class="WeekTd">' + this.weekArr[i] + '</th>';
                 this.Thead += '</tr>\n';
                 
                 this.Tbody = this.tableRowText;
                 this.dateArr[1] = (!this.checkYear(_year)) ? 28 : 29 ;
                 
                 for (var i=0; i<this.firstPos(_year, _month); i++) 
                 	this.Tbody += '<td class="BlankTd"></td>';
                 	
                 for (var i=1; i<=this.dateArr[_month]; i++) {
                      if (this.firstPos(_year, _month) == 0) {
                          if (i!=1 && i%7==0) this.Tbody += '</tr>\n' + this.tableRowText;
                      } else {
                          if ((i+this.firstPos(_year, _month))%7==1) this.Tbody += '</tr>\n' + this.tableRowText;                      }
                     var newDiv='<div class="task" data-date='+this.checkDate(_year, _month+1, i)+'></div>';
                     	   if (!this.today(_year, _month, i)) {
                          	this.Tbody += '<td align="left" class="out"  onclick="myTable.showDateStr(' + _year + ', ' + _month + ', ' + i + ', \'' + this.weekArr[new Date(_year, _month, i).getDay()] + '\');">' + i + newDiv + '</td>';
                     	  } else {
                         	this.Tbody += '<td align="left" class="Today" onclick="myTable.showDateStr(' + _year + ', ' + _month + ', ' + i + ', \'' + this.weekArr[new Date(_year, _month, i).getDay()] + '\');">' + i + newDiv + '</td>'; 
                         } 
                 }
                 for (var i=0; i<6-this.lastPos(_year, _month); i++) this.Tbody += '<td class="BlankTd"></td>';
                 this.Tbody += '</tr>\n'; 
                 this.TFoot = '</table>\n';
                 
                 this.Table = this.Thead + this.Tbody + this.TFoot;
                 return this.Table;
         }

         this.firstPos = function(_year, _month) {
              return new Date(_year, _month, 1).getDay();
         }

         this.lastPos = function(_year, _month) {
              return new Date(_year, _month, this.dateArr[_month]).getDay();
         }


	
         this.checkYear = function(_year) {
              return ((_year % 4 == 0) && (_year % 100 != 0)) || (_year % 400 == 0);
         }

         this.checkDate = function(_year, _month,_date) {
		if (_date<1) { 
			_month--;  
                 	_year = parseInt(this.checkMonth(_year, _month).split('-')[0]);
			_month = parseInt(this.checkMonth(_year, _month).split('-')[1]);
			this.dateArr[1] = (!this.checkYear(_year)) ? 28 : 29 ;
			_date += this.dateArr[_month];
              }
              
              this.dateArr[1] = (!this.checkYear(_year)) ? 28 : 29 ;
             
              if (_date > this.dateArr[_month]) {
              		ori_month = _month;
              		_month++;
                       	_year = parseInt(this.checkMonth(_year, _month).split('-')[0]);
			_month = parseInt(this.checkMonth(_year, _month).split('-')[1]);

              		_date -= this.dateArr[ori_month];
    
              }  
              return _year + '-' + _month + '-' + _date;
         } 
         
         
         
         this.checkMonth = function(_year, _month) {
         	if (_month < 0) {
         		_year--;
         		_month = 11;	
         	}
         	if (_month > 11) {
         		_year++;
         		_month = 0;	
         	}
         	return _year + '-' + _month;
         }
         
         this.today = function(_year, _month, _date) {
              return (new Date().getFullYear() == _year) && (new Date().getMonth() == _month) && (new Date().getDate() == _date);
         }
         
         this.showTimeStr = function(_year, _month, _date, _week) {
              window.alert('准备添加日程'); 
         }
    this.showDateStr=function(_year, _month, _date, _week){
        console.log("showDateStr...do nothing");
    }
}
   
    window.onload = function() {
         myTable= new DateClass(self.wTableContainer);
         myTable.showWeekTable(new Date().getFullYear(), new Date().getMonth(), new Date().getDate(), new Date().getDay());
    }
    
