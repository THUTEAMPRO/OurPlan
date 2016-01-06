var week_util={
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
        '<div class="time"><label>time:</label><%=timeselect%></div>'+
        '<div class="duration"><label>duration:</label><%=durationselect%></div>'+
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
    template:function(date,time,duration,title,info,tid){
        var button="";
        var data="";
        var timets="";
        var durationts="";
        if(tid){
            var hour=time.split(":")[0];
            data='data-hour='+hour+' data-date='+date+' data-id='+tid;
            button='<button class="del">del</button>'+'<button class="update">update</button>';
            timets=week_util.tstemplate(time);
            durationts=week_util.tstemplate(duration);
        }else{
            data='data-hour='+hour+' data-date='+date;
            button='<button class="add">add</button>';
            timets=week_util.tstemplate("00:00:00");
            durationts=week_util.tstemplate("00:00:00");
        }
        return _.template(week_util.templateHTML)({
            durationselect:durationts,
            timeselect:timets,
            title:title,
            info:info,
            data:data,
            button:button
        });
    },
    timenum2str:function(sth){
        sth=String(sth);
        if(sth.length==1) return "0"+sth;
        else return sth;
    },
    getDuration:function(){
        var hour=$("#overDiv div.duration select.hour").val();
        var minute=$("#overDiv div.duration select.minute").val();
        var second=$("#overDiv div.duration select.second").val();
        hour=month_util.timenum2str(hour);
        minute=month_util.timenum2str(minute);
        second=month_util.timenum2str(second);
        var time=hour+":"+minute+":"+second;
        return time;
    },
    getTime:function(){
        var hour=$("#overDiv div.time select.hour").val();
        var minute=$("#overDiv div.time select.minute").val();
        var second=$("#overDiv div.time select.second").val();
        hour=month_util.timenum2str(hour);
        minute=month_util.timenum2str(minute);
        second=month_util.timenum2str(second);
        var duration=hour+":"+minute+":"+second;
        return duration;
    },
}
var week_bind_task=function(){
    selected_data.view_type="week";
    $(".task").html("");
    for(var id in task_data){
        var task=task_data[id];
        var hour=eval(task.time.split(":")[0]);
        var selector="div.task.week[data-date="+task.date+"][data-hour="+hour+"]";
        var label='<label class="tasklabel" data-id='+id+">"+task.title+"</label>"
        $(selector).append(label);
    }
    $("td.out").on("mouseenter",function(){
                  $(this).addClass("enter_effect");
           });
   $("td.out").on("mouseleave",function(){
                    $(this).removeClass("enter_effect");
                    // $(this).css({"color":"blue","border":"1px solid buttonface"});
              });
    $("td.out").on("click",function(e){
        var $label=$(e.target).closest("label");
        var $tdout=$(e.target).closest("td.out");
        if($label.length==0){
            overlib(week_util.template(data_date,data_hour+":00:00"),STICKY);
            week_bind_button();
        }else{
            var tid=$label.attr("data-id");
            var data_hour=$tdout.find("div").attr("data-hour");
            var data_date=$tdout.find("div").attr("data-date");
            var task=task_data[tid];
            overlib(week_util.template(data_date,task.time,task.duration,task.title,task.info,task.id),STICKY);
            week_bind_button();
        }
    });
}
var week_bind_button=function(){
    $("button.del").on("click",function(e){
        var tid=$(e.target).closest("div.data").attr("data-id");
        $.post("/api/del_task",{id:tid},function(data){
            if(data.fail){
                alert("del fail");
            }else{
                delete task_data[tid];
                week_bind_task();
            }
        });
        nd();
        nd();
    });

    $("button.update").on("click",function(e){
        var tid=$(e.target).closest("div.data").attr("data-id");
        var title=$("#overDiv input").val();
        var info=$("#overDiv textarea").val();
        var time=week_util.getTime();
        var duration=week_util.getDuration();
        $.post("/api/update_task", {
                    id:tid,
                    info:info,
                    title:title,
                    time:time,
                    duration:duration
               },
               function(data){
            if(data.fail){
                alert("update fail");
            }else{
                task_data[tid].title=title;
                task_data[tid].info=info;
                task_data[tid].time=time;
                task_data[tid].duration=duration;
                week_bind_task();
            }
        });
        nd();
        nd();
    });
    $("button.add").on("click",function(e){
        var time=week_util.getTime();
        var duration=week_util.getDuration();
        var date=$(e.target).closest("div.data").attr("data-date");
        var title=$("#overDiv input").val();
        var info=$("#overDiv textarea").val();
        $.post("/api/add_task",
               {
                   time:time,
                   duration:duration,
                   date:date,
                   info:info,
                   title:title,
                   groupid:selected_data.groupid
               },
               function(data){
            if(data.fail){
                alert("add fail");
            }else{
                task_data[data.id]={
                    id:data.id,
                    date:date,
                    time:time,
                    duration:duration,
                    info:info,
                    title:data.title,
                }
                week_bind_task();
            }
        });
        nd();
        nd();
    });
}
$(document).ready(function(){
    $(document).keydown(function(e){
        if(e.keyCode==27){
            nd();
            nd();
        }
    });

    $("div.container").on("click",function(e){
        var $tdout=$(e.target).closest("td.out");
        if($tdout.size()==0){
            nd();
            nd();
        }
    });
});
