var week_bind_task=function(){
    $(".task").html("");
    for(var id in task_data){
        var task=task_data[id];
        var hour=eval(task.time.split(":")[0]);
        var selector="div[data-date="+task.date+"][data-hour="+hour+"]";
        var label="<label data-id="+id+">"+task.title+"</label>"
        $(selector).html(label);
    }
    $("td.out").on("click",function(e){
        var $tdout=$(e.target).closest("td.out");
        var tid=$tdout.find("label").attr("data-id");
        var data_hour=$tdout.find("div").attr("data-hour");
        var data_date=$tdout.find("div").attr("data-date");
        if(tid){
            var task=task_data[tid];
            var titleInput='<input value='+task.title+'></input>';
            var infoInput='<textarea>'+task.info+'</textarea>';
            var divLeft='<div class="data" data-hour='+data_hour+
                ' data-date='+data_date+' data-id='+tid+">";
            var delButton='<button class="del">del</button>';
            var updateButton='<button class="update">update</button>';
            overlib(infoInput+divLeft+delButton+updateButton+"</div>",
                    STICKY,CAPTION,titleInput);
            week_bind_button();
        }else{
            var titleInput='<input></input>';
            var infoInput='<textarea></textarea>';
            var divLeft='<div class="data" data-hour='+data_hour+
                ' data-date='+data_date+' data-id='+tid+">";
            var addButton='<button class="add">add</button>';
            overlib(infoInput+divLeft+addButton+"</div>",
                    STICKY,CAPTION,titleInput);
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
                   title:title
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
                    title:title,
                }
                week_bind_task();
            }
        });
        nd();
        nd();
    });
}
var month_bind_task=function(){
    $(".task").html("");
    for(var id in task_data){
        var task=task_data[id];
        var hour=eval(task.time.split(":")[0]);
        var selector="div[data-date="+task.date+"]";
        var label="<label data-id="+id+">"+task.title+"</label><br/>";
        $(selector).append(label);
    }
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