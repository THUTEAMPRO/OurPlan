var month_util={
    timeselectHTML:
    '<select class="hour"><% for(var i=0;i<=23;i++){%>'+
        '<% if(hour==i){%>'+
            '<option selected="selected"><%=i%></option>'+
        '<%}else{%>'+
            '<option><%=i%></option>'+
        '<%}%>'+
    '<%}%></select>'+":"+
    '<select class="minute"><% for(var i=0;i<=59;i++){%>'+
        '<% if(minute==i){%>'+
            '<option selected="selected"><%=i%></option>'+
        '<%}else{%>'+
            '<option><%=i%></option>'+
        '<%}%>'+
    '<%}%></select>'+":"+
    '<select class="second"><% for(var i=0;i<=59;i++){%>'+
        '<% if(second==i){%>'+
            '<option selected="selected"><%=i%></option>'+
        '<%}else{%>'+
            '<option><%=i%></option>'+
        '<%}%>'+
    '<%}%></select>',
    templateHTML:
    '<div>'+
        '<div><label>date:</label><%=date%></div>'+
        '<div><label>time:</label><%=timeselect%></div>'+
        '<div><label>title:</label><input value="<%=title%>"></input></div>'+
        '<div><label>info:</label><textarea><%=info%></textarea></div>'+
        '<div class="data" <%=data%>><%=button%></div>'+
    '</div>',
    tstemplate:function(time){
        var split=time.split(":");
        return _.template(month_util.timeselectHTML)({
            hour:Number(split[0]),
            minute:Number(split[1]),
            second:Number(split[2])
        });
    },
    template:function(date,time,title,info,tid){
        var button="";
        if(time){
            var data='data-date='+date+' data-id='+tid;
            var timeHTML=month_util.tstemplate(time);
            button='<button class="del">del</button>'+'<button class="update">update</button>';
            return _.template(month_util.templateHTML)({
                title:title,
                info:info,
                date:date,
                data:data,
                timeselect:timeHTML,
                button:button
            });
        }else{
            var data='data-date='+date;
            time="00:00:00";
            var timeHTML=month_util.tstemplate(time);
            button='<button class="add">add</button>';
            return _.template(month_util.templateHTML)({
                title:title,
                info:info,
                date:date,
                data:data,
                timeselect:timeHTML,
                button:button
            });
        }
    },
    bind_task:function(){
        $(".task").html("");
        for(var id in task_data){
            var task=task_data[id];
            var hour=eval(task.time.split(":")[0]);
            var selector="div.task.month[data-date="+task.date+"]";
            var label="<div><label data-id="+id+" data-time="+task.time+" data-date="+task.date+">"+task.title+"</label></div>";
            $(selector).append(label);
        }
        $("td.out").on("click",function(e){
            var $tdout=$(e.target).closest("td.out");
            var $label=$(e.target).closest("label");
            if($label.length==0){
                var data_date=$tdout.find("div.task").attr("data-date");
                overlib(month_util.template(data_date),STICKY);
                month_util.bind_button();
            }else{
                var tid=$tdout.find("label").attr("data-id");
                var task=task_data[tid];
                overlib(month_util.template(task.date,task.time,task.title,task.info,task.id),STICKY);
                month_util.bind_button();
            }
        });
    },
    timenum2str:function(sth){
        sth=String(sth);
        if(sth.length==1) return "0"+sth;
        else return sth;
    },
    bind_button:function(){
        $("button.del").on("click",function(e){
            var tid=$(e.target).closest("div.data").attr("data-id");
            $.post("/api/del_task",{id:tid},function(data){
                if(data.fail){
                    alert("del fail");
                }else{
                    delete task_data[tid];
                    month_util.bind_task();
                }
            });
            nd();
            nd();
        });
        $("button.update").on("click",function(e){
            var tid=$(e.target).closest("div.data").attr("data-id");
            var title=$("#overDiv input").val();
            var info=$("#overDiv textarea").val();
            var hour=$("#overDiv select.hour").val();
            var minute=$("#overDiv select.minute").val();
            var second=$("#overDiv select.second").val();
            hour=month_util.timenum2str(hour);
            minute=month_util.timenum2str(minute);
            second=month_util.timenum2str(second);
            var time=hour+":"+minute+":"+second;
            $.post("/api/update_task", {
                id:tid,
                info:info,
                title:title,
                time:time,
            },
                   function(data){
                       if(data.fail){
                           alert("update fail");
                       }else{
                           task_data[tid].title=title;
                           task_data[tid].info=info;
                           task_data[tid].time=time;
                           month_util.bind_task();
                       }
                   });
            nd();
            nd();
        });
        $("button.add").on("click",function(e){
            var date=$(e.target).closest("div.data").attr("data-date");
            var title=$("#overDiv input").val();
            var info=$("#overDiv textarea").val();
            
            var hour=$("#overDiv select.hour").val();
            var minute=$("#overDiv select.minute").val();
            var second=$("#overDiv select.second").val();
            hour=month_util.timenum2str(hour);
            minute=month_util.timenum2str(minute);
            second=month_util.timenum2str(second);
            var time=hour+":"+minute+":"+second;
            
            $.post("/api/add_task",
                   {
                       time:time,
                       date:date,
                       info:info,
                       title:title
                   },
                   function(data){
                       if(data.fail){
                           alert("add fail");
                       }else{
                           task_data[data.id]={
                               id:data.id,
                               date:date,
                               time:time,
                               info:info,
                               title:data.title,
                           }
                           month_util.bind_task();
                       }
                   });
            nd();
            nd();
        });
    }
}
var month_bind_task=month_util.bind_task;