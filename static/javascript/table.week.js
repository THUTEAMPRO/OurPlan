var myWeek = new Object();
function DateClass(_container) {
        this.container = _container;
        this.weekArr = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        this.dateArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        this.monthArr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
        
        this.showWeekTable = function(_year, _month, _date, _day) {
             this.container.innerHTML = this.getWeekTable(_year, _month,_date,_day);
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
                 
                 this.Thead = '  <input type="button" value="today" onclick="myWeek.showWeekTable(' +today_year+ ',' +today_month+ ',' +today_date+ ',' +today_day+ '); "/>';
                 this.Thead += '  <input type="button" value="prev w" onclick="myWeek.showWeekTable(' + _year + ', ' +_month+ ',' +eval(_date - 7)+ ',' +_day+ '); "/>';
                 this.Thead +=this.monthArr[_month] + ' ' + _date+ ', '+ _year + ' '+this.weekArr[+_day];
                 this.Thead += '  <input type="button" value="next w" onclick="myWeek.showWeekTable(' + _year + ',' +_month+ ',' +eval(_date + 7)+',' +_day+ '); "/>';
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
        
        	this.Tbody = '';
        	 for (var i = 0; i < 24; i++) {
        	 	this.Tbody += '<tr> <td align="right" class="WeekTd">'+i+':00</td>'
        	 	for (var j = 0; j < this.weekArr.length; j++) {
        	 		this.Tbody += '<td class="out"></td>'
        	 	}
        	 	this.Tbody += '</tr>';
        	 }
                 this.TFoot = '</table>\n';
                 
                 this.Table = this.Thead + this.Tbody + this.TFoot;
                 return this.Table;
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
         
         this.showTimeStr = function(_year, _month, _date, _week) {
              window.alert('准备添加日程'); 
         }
}
   
    window.onload = function() {
         myWeek = new DateClass(self.wTableContainer);
         myWeek.showWeekTable(new Date().getFullYear(), new Date().getMonth(), new Date().getDate(), new Date().getDay());
    }
    
