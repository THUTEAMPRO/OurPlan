var oDate = new Object();
function DateClass(_container) {
        this.container = _container;
        this.weekArr = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        this.dateArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        this.monthArr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
        
        this.tableRowText = '<tr height=80 valign="top">';

        this.showTable = function(_year, _month) {
             this.container.innerHTML = this.getDateTable(_year, _month);
             
        }

        this.getDateTable = function(_year, _month) {	
                 _year = parseInt(this.checkDate(_year, _month).split('-')[0]);
                 _month = parseInt(this.checkDate(_year, _month).split('-')[1]);
                 today_year = new Date().getFullYear();
                 today_month = new Date().getMonth() + 1;
                 this.Thead = '  <input type="button" value="today" onclick="oDate.showTable(' +today_year+ ', ' + today_month+ '); "/>';
                 this.Thead += '  <input type="button" value="prev m" onclick="oDate.showTable(' + _year + ', ' + eval(_month-1) + '); "/>';
                 this.Thead += this.monthArr[_month-1] + ' '+ _year;
                 this.Thead += '  <input type="button" value="next m" onclick="oDate.showTable(' + _year + ', ' + eval(_month+1) + '); "/>';
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
                 for (var i=1; i<=this.dateArr[_month-1]; i++) {
                      if (this.firstPos(_year, _month) == 0) {
                          if (i!=1 && i%7==1) this.Tbody += '</tr>\n' + this.tableRowText;
                      } else {
                          if ((i+this.firstPos(_year, _month))%7==1) this.Tbody += '</tr>\n' + this.tableRowText;                      }
                      if (!this.today(_year, _month, i)) {
                          this.Tbody += '<td align="left" class="out"  onclick="oDate.showDateStr(' + _year + ', ' + _month + ', ' + i + ', \'' + this.weekArr[new Date(_year, _month-1, i).getDay()] + '\');">' + i + '</td>';
                      } else {
                         this.Tbody += '<td align="left" class="Today" onclick="oDate.showDateStr(' + _year + ', ' + _month + ', ' + i + ', \'' + this.weekArr[new Date(_year, _month-1, i).getDay()] + '\');">' + i + '</td>'; 
                      } 
                 }
                 for (var i=0; i<6-this.lastPos(_year, _month); i++) this.Tbody += '<td class="BlankTd"></td>';
                 this.Tbody += '</tr>\n'; 
                 this.TFoot = '</table>\n';
                 
                 this.Table = this.Thead + this.Tbody + this.TFoot;
                 return this.Table;
         }

         this.firstPos = function(_year, _month) {
              return new Date(_year, _month-1, 1).getDay();
         }

         this.lastPos = function(_year, _month) {
              return new Date(_year, _month-1, this.dateArr[_month-1]).getDay();
         }

         this.checkYear = function(_year) {
              return ((_year % 4 == 0) && (_year % 100 != 0)) || (_year % 400 == 0);
         }

         this.today = function(_year, _month, _date) {
              return (new Date().getFullYear() == _year) && (new Date().getMonth() == _month-1) && (new Date().getDate() == _date);
         }

         this.checkDate = function(_year, _month) {
              if (_month<1) { 
                  _year --;
                  _month = 12;
              }
              if (_month>12) { 
                  _year ++;
                  _month = 1;
              }
              return _year + '-' + _month;
         } 
         
         this.showDateStr = function(_year, _month, _date, _week) {
              window.alert('准备添加日程'); 
         }
}
   
    window.onload = function() {
         oDate = new DateClass(self.mTableContainer);
         oDate.showTable(new Date().getFullYear(), new Date().getMonth()+1);
    }
    
