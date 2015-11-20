var group_calendar_util={
    bind:function(){
        $("input[name=CalendarGroup]").click(function(e){
            var $label=$(e.target).closest("label");
            var groupid=$label.attr("data-id");
            selected_data.groupid=Number(groupid)||undefined;
            if(groupid){
                selected_data.task_data=group_task_data[groupid];
            }else{
                selected_data.task_data=user_task_data;
            }
            
            if(selected_data.view_type=="week"){
                week_bind_task();
            }else if(selected_data.view_type=="month"){
                month_bind_task();
            }else{
                console.error("unknow view type");
            }
        });
    }
}
$(document).ready(function(){
    group_calendar_util.bind();
});