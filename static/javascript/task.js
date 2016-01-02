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
        var data="";
        if(tid){
            var hour=time.split(":")[0];
            data='data-hour='+hour+' data-date='+date+' data-id='+tid;
            button='<button class="del">del</button>'+'<button class="update">update</button>';
        }else{
            data='data-hour='+hour+' data-date='+date;
            button='<button class="add">add</button>';
        }
        return _.template(week_util.templateHTML)({
            title:title,
            info:info,
            data:data,
            button:button
        });
    }
}
var week_bind_task=function(){
    selected_data.view_type="week";
    $(".task").html("");
    for(var id in task_data){
        var task=task_data[id];
        var hour=eval(task.time.split(":")[0]);
        var selector="div.task.week[data-date="+task.date+"][data-hour="+hour+"]";
        var label="<label data-id="+id+">"+task.title+"</label>"
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
        var $tdout=$(e.target).closest("td.out");
        var tid=$tdout.find("label").attr("data-id");
        var data_hour=$tdout.find("div").attr("data-hour");
        var data_date=$tdout.find("div").attr("data-date");
        if(tid){
            var task=task_data[tid];
            overlib(week_util.template(data_date,data_hour,task.title,task.info,task.id),STICKY);
            week_bind_button();
        }else{
            overlib(week_util.template(data_date,data_hour),STICKY);
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
        $.post("/api/update_task", {
                   id:tid,
                   info:info,
                   title:title
               },
               function(data){
            if(data.fail){
                alert("update fail");
            }else{
                task_data[tid].title=title;
                task_data[tid].info=info;
                week_bind_task();
            }
        });
        nd();
        nd();
    });
    $("button.add").on("click",function(e){
        var hour=$(e.target).closest("div.data").attr("data-hour");
        var date=$(e.target).closest("div.data").attr("data-date");
        var title=$("#overDiv input").val();
        var info=$("#overDiv textarea").val();
        $.post("/api/add_task",
               {
                   time:hour+":00:00",
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
                    time:hour+":00:00",
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