var analyse_util={
    templateHTML:"<tr><td><%=group1%></td>"+
        "<td><%=title1%></td>"+
        "<td><%=group2%></td>"+
        "<td><%=title2%></td>"+
        "<td><%=time%></td>"+
        "</tr>",
    template:function(dict){
        return _.template(analyse_util.templateHTML)(dict);
    },
    formatDatetime:function(dt){
        var datestr=dt.getFullYear()+"-"+dt.getMonth()+"-"+dt.getDate();
        var timestr=dt.getHours()+":"+dt.getMinutes()+":"+dt.getSeconds();
        return datestr+" "+timestr;
    },
    getDateTime:function(date,time){
        var dt=new Date();
        
        var dd=date.split("-");
        dt.setFullYear(dd[0]);
        dt.setMonth(dd[1]);
        dt.setDate(dd[2]);

        var tt=time.split(":");
        dt.setHours(tt[0]);
        dt.setMinutes(tt[1]);
        dt.setSeconds(tt[2]);
        return dt;
    },
    getDuration:function(time){
        var tt=time.split(":");
        tt=_.map(tt,function(i){
            return Number(i);
        });
        return (tt[0]*3600+tt[1]*60+tt[2])*1000;
    },
    check:function(t1,t2){
        var util=analyse_util;
        var s1=util.getDateTime(t1.date,t1.time).getTime();
        var e1=s1+util.getDuration(t2.duration);
        var s2=util.getDateTime(t2.date,t2.time).getTime();
        var e2=s2+util.getDuration(t2.duration);
        if(s1<e2 && s2<e1){
            var sc=Math.max(s1,s2);
            var ec=Math.min(e1,e2);
            var start=new Date();
            start.setTime(sc);
            var end=new Date();
            end.setTime(ec);
            return {
                start:start,
                end:end
            }
        }else{
            return 0;
        }
    },
    analyseDo:function(){
        var group_id2name={}
        _.each(group_data,function(group){
            group_id2name[group.groupid]=group.groupname;
        });
        var getGroupName=function(task){
            if(task.groupid){
                return group_id2name[task.groupid];
            }else{
                return "user";
            }
        }
        var task_array=[]
        _.each(user_task_data,function(task,taskid){
            task_array.push(task);
        });
        _.each(group_task_data,function(tasks,groupid){
            _.each(tasks,function(task,taskid){
                task_array.push(task);
            });
        });
        for(var i=0;i<task_array.length;i++){
            var task1=task_array[i];
            console.log(task1.title);
            for(var j=i+1;j<task_array.length;j++){
                var task2=task_array[j];
                var check=analyse_util.check(task1,task2);
                if(check!=0){
                    var startFmt=analyse_util.formatDatetime(check.start);
                    var endFmt=analyse_util.formatDatetime(check.end);
                    var name1=getGroupName(task1);
                    var name2=getGroupName(task2);
                    var html=analyse_util.template({
                        group1:name1,
                        title1:task1.title,
                        group2:name2,
                        title2:task2.title,
                        time:startFmt+"~~~"+endFmt
                    });
                    $("#analyseTable tbody").append(html);
                }
            }
        }
    }
}
$(document).ready(function(){
    analyse_util.analyseDo();
});